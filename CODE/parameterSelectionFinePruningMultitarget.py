# all necessary imports
import warnings
warnings.filterwarnings('ignore')
import h5py
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import backend as K
from keras.models import Model
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import pickle
########################################################################################################################
# useful utilities
########################################################################################################################
# load data
def data_loader(filepath):
    data = h5py.File(filepath, 'r')
    x_data = np.array(data['data'])
    y_data = np.array(data['label'])
    x_data = x_data.transpose((0, 2, 3, 1))
    return x_data, y_data


#from https: // stackoverflow.com / questions / 50151157 / keras - how - to - get - layer - index - when - already - know - layer - name)
def getLayerIndexByName(model, layername):
    for idx, layer in enumerate(model.layers):
        if layer.name == layername:
            return idx


########################################################################################################################
# define path for data and models
########################################################################################################################
data_path = "/Users/vahan/Desktop/NYUAD PhD PROGRAM/COURSES/EL-GY-9163 MACHINE LEARNING FOR CYBER-SECURITY/HW/HW3"
modelName  = "Multitarget"
datasetName = "sunglasses"
########################################################################################################################
# get the data and models
########################################################################################################################
clean_data_valid_filename = data_path+"/data/clean_validation_data.h5"
clean_data_test_filename = data_path + "/data/clean_test_data.h5"

if datasetName == "sunglasses":
    poisoned_data_test_filename = data_path+"/data/Multi-trigger Multi-target/sunglasses_poisoned_data.h5"
if datasetName == "lipstick":
    poisoned_data_test_filename = data_path+"/data/Multi-trigger Multi-target/lipstick_poisoned_data.h5"
if datasetName == "eybrows":
    poisoned_data_test_filename = data_path+"/data/Multi-trigger Multi-target/eybrows_poisoned_data.h5"


# load the data
cl_x_valid, cl_y_valid = data_loader(clean_data_valid_filename)

cl_x_test, cl_y_test = data_loader(clean_data_test_filename)
bd_x_test, bd_y_test = data_loader(poisoned_data_test_filename)

for lr in [1e-4,1e-5,1e-6,1e-2]:
    # load baseline model
    B = keras.models.load_model(data_path+"/models/multi_trigger_multi_target_bd_net.h5")
    B.load_weights(data_path+"/models/multi_trigger_multi_target_bd_weights.h5")

    # define the fine-pruned model (initally it is the same as the baseline)
    B_prime = keras.models.load_model(data_path+"/models/multi_trigger_multi_target_bd_net.h5")
    B_prime.load_weights(data_path+"/models/multi_trigger_multi_target_bd_weights.h5")


    ########################################################################################################################
    # define layers to prune
    ########################################################################################################################
    lastPoolLayerIdx = getLayerIndexByName(B, "pool_3")
    lastConvLayerIdx = getLayerIndexByName(B, "conv_3") # before the fc_1 and pool_3 there is conv_3

    ########################################################################################################################
    # get last max pooling layer's activations
    ########################################################################################################################
    # https://machinelearningmastery.com/how-to-visualize-filters-and-feature-maps-in-convolutional-neural-networks/
    tmpModel = Model(inputs=B.inputs, outputs=B.layers[lastPoolLayerIdx].output)
    tmpModel.summary()
    feature_maps_cl = tmpModel(cl_x_valid)

    # get the activations and sort them in an increasing order excluding empty layers
    avgActivationsByChannelsBeforeTrain = np.abs(np.mean(np.abs(feature_maps_cl),axis=(0, 1, 2)))
    allIdxToPrune = np.argsort(avgActivationsByChannelsBeforeTrain) # increasing  order

    idxToPrune = [i for i in allIdxToPrune if avgActivationsByChannelsBeforeTrain[i]!=0 ]

    lastConvLayerWeights = B_prime.layers[lastConvLayerIdx].get_weights()[0]
    lastConvLayerBiases  = B_prime.layers[lastConvLayerIdx].get_weights()[1]

    numDormantChannels=len(allIdxToPrune)-len(idxToPrune)
    print("number of dormant channels = ",numDormantChannels)

    numDormantChannels=len(allIdxToPrune)-len(idxToPrune)
    print(numDormantChannels)
    ########################################################################################################################
    # evaluate for dormant channels (i.e. the metrics at the beginning of pruning)
    ########################################################################################################################
    # evaluate the updated model accuracy on the clean test data
    cl_label_p_valid_orig = np.argmax(B_prime(cl_x_valid), axis=1)
    clean_accuracy_valid_orig = np.mean(np.equal(cl_label_p_valid_orig, cl_y_valid)) * 100
    print("Clean validation accuracy before modification: {0:3.6f}".format(clean_accuracy_valid_orig))

    # evaluate the updated model accuracy on the clean test data
    cl_label_p_test_orig = np.argmax(B_prime(cl_x_test), axis=1)
    clean_accuracy_test_orig = np.mean(np.equal(cl_label_p_test_orig, cl_y_test)) * 100

    # evaluate the updated model model attack success rate on the test data
    bd_label_p_test_orig = np.argmax(B_prime(bd_x_test), axis=1)
    asr_test_orig= np.mean(np.equal(bd_label_p_test_orig, bd_y_test)) * 100

    ########################################################################################################################
    # specify parameters (here we will be fine tuning the learning rate only)
    ########################################################################################################################
    #lr = 1e-3
    epochs  = 10
    batch_size = 32

    opt = tf.keras.optimizers.Adam(learning_rate=lr)
    ########################################################################################################################
    # perform fine pruning by removing a channel one in a time
    ########################################################################################################################
    totalPercentChannelsRemoved = np.zeros((61))
    totalCleanAccuracyValid = np.zeros((61))
    totalAttackSuccessRateValid = np.zeros((61))
    totalCleanAccuracyTest = np.zeros((61))
    totalAttackSuccessRateTest = np.zeros((61))
    percentValidationAccuracy = []

    iter = 0
    # before the fine pruning estimate the baseline clean validation/test accuracies:
    percentChannelsRemoved = 0 # no channel has been removed yet
    totalPercentChannelsRemoved[iter] = percentChannelsRemoved
    totalCleanAccuracyValid[iter] = clean_accuracy_valid_orig
    totalCleanAccuracyTest[iter] = clean_accuracy_test_orig
    totalAttackSuccessRateTest[iter] = asr_test_orig
    iter+=1

    for chIdx in allIdxToPrune:
        percentChannelsRemoved = iter / lastConvLayerWeights.shape[3]
        if chIdx in idxToPrune:  # if not dormant
            # remove one channel at a time
            lastConvLayerWeights[:, :, :, chIdx] = 0
            lastConvLayerBiases[chIdx] = 0

            # update weights and biases of the badnet
            B_prime.layers[lastConvLayerIdx].set_weights([lastConvLayerWeights, lastConvLayerBiases])

            B_prime.compile(optimizer=opt, loss='sparse_categorical_crossentropy', metrics=['accuracy'])
            print("Learning rate:", B_prime.optimizer.learning_rate.numpy())
            B_prime.fit(cl_x_valid, cl_y_valid, epochs=epochs, batch_size=batch_size)

            # evaluate the updated model predictions on the clean validation data
            cl_label_p_valid = np.argmax(B_prime(cl_x_valid), axis=1)
            clean_accuracy_valid = np.mean(np.equal(cl_label_p_valid, cl_y_valid)) * 100

            # evaluate the updated model accuracy on the clean test data
            cl_label_p_test = np.argmax(B_prime(cl_x_test), axis=1)
            clean_accuracy_test = np.mean(np.equal(cl_label_p_test, cl_y_test)) * 100

            # evaluate the updated model model attack success rate on the test data
            bd_label_p_test = np.argmax(B_prime(bd_x_test), axis=1)
            asr_test = np.mean(np.equal(bd_label_p_test, bd_y_test)) * 100
            K.clear_session()

            print(
                "Iteration = {0:3d}, channel removed = {1:3d}, percent channels removed = {2:3.6f}\nClean validation accuracy after modification: {3:3.6f}\n Clean test accuracy after modification: {4:3.6f}, attack success rate test =  {5:3.6f}".format(
                    iter, chIdx, percentChannelsRemoved * 100, clean_accuracy_valid, clean_accuracy_test, asr_test))
            totalPercentChannelsRemoved[iter] = percentChannelsRemoved
            totalCleanAccuracyValid[iter] = clean_accuracy_valid
            totalCleanAccuracyTest[iter] = clean_accuracy_test
            totalAttackSuccessRateTest[iter] = asr_test
        else:  # if dormant
            print(
                "Iteration = {0:3d}, channel removed = {1:3d}, percent channels removed = {2:3.6f}\nClean validation accuracy after modification: {3:3.6f}\n Clean test accuracy after modification: {4:3.6f}, attack success rate test =  {5:3.6f}".format(
                    iter, chIdx, percentChannelsRemoved * 100, clean_accuracy_valid_orig, clean_accuracy_test_orig, asr_test_orig))

            totalPercentChannelsRemoved[iter] = percentChannelsRemoved
            totalCleanAccuracyValid[iter] = clean_accuracy_valid_orig
            totalCleanAccuracyTest[iter] = clean_accuracy_test_orig
            totalAttackSuccessRateTest[iter] = asr_test_orig
        iter += 1

    # save the results:
    with open(data_path + "/RESULTS/REPORTS/totalPercentChannelsRemoved"+ modelName +"_"+datasetName+ "_"+str("%0.6f" % lr) + '.p', 'wb') as fp:
        pickle.dump(totalPercentChannelsRemoved, fp)

    with open(data_path + "/RESULTS/REPORTS/totalCleanAccuracyValid"+ modelName +"_"+datasetName+ "_"+str("%0.6f" % lr) + '.p', 'wb') as fp:
        pickle.dump(totalCleanAccuracyValid, fp)

    with open(data_path + "/RESULTS/REPORTS/totalCleanAccuracyTest" + modelName +"_"+datasetName+ "_"+str("%0.6f" % lr) + '.p', 'wb') as fp:
        pickle.dump(totalCleanAccuracyTest, fp)

    with open(data_path + "/RESULTS/REPORTS/totalAttackSuccessRateTest" + modelName +"_"+datasetName+ "_"+str("%0.6f" % lr) + '.p', 'wb') as fp:
        pickle.dump(totalAttackSuccessRateTest, fp)

