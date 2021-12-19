# all necessary imports
import warnings
import numpy as np
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt
import pickle
import matplotlib.font_manager as font_manager
########################################################################################################################
# useful utilities
########################################################################################################################
# load results

########################################################################################################################
# define path for data and models
########################################################################################################################
data_path = "/"
#modelName  = "Multitarget"
#datasetName = "sunglasses"

modelNames = ["Sunglasses", "anonymous1","Multitarget"]
datasetNames = ['sunglasses','lipstick','eyebrows']

modelName  = "Multitarget"
datasetName = 'eyebrows'

if modelName  == "Sunglasses":
    dataPathLoc = modelName
    titleModelName = 'sunglasses_bd'
if modelName  == "anonymous1":
    dataPathLoc = modelName
    titleModelName = 'anonymous_1_bd'
if modelName  == "Multitarget":
    dataPathLoc = modelName +"_"+datasetName+"_"
    titleModelName = 'multi-target '+datasetName


allPercentChannelsRemovedArray = np.zeros((5,61))
allCleanAccuracyValidArray = np.zeros((5,61))
allCleanAccuracyTestArray = np.zeros((5,61))
allAttackSuccessRateTestArray = np.zeros((5,61))

for l,lr in enumerate([1e-2, 1e-3, 1e-4, 1e-5, 1e-6]):
    with open(data_path + "/RESULTS/REPORTS/totalPercentChannelsRemoved" + dataPathLoc + str("%0.6f" % lr) + '.p',
              'rb') as fp:
        totalPercentChannelsRemoved = pickle.load(fp)
        allPercentChannelsRemovedArray[l, :] =totalPercentChannelsRemoved

    with open(data_path + "/RESULTS/REPORTS/totalCleanAccuracyValid" + dataPathLoc + str("%0.6f" % lr) + '.p',
              'rb') as fp:
        totalCleanAccuracyValid = pickle.load(fp)
        allCleanAccuracyValidArray[l, :] = totalCleanAccuracyValid
    with open(data_path + "/RESULTS/REPORTS/totalCleanAccuracyTest" + dataPathLoc + str("%0.6f" % lr) + '.p', 'rb') as fp:
        totalCleanAccuracyTest=pickle.load(fp)
        allCleanAccuracyTestArray[l, :] = totalCleanAccuracyTest

    with open(data_path + "/RESULTS/REPORTS/totalAttackSuccessRateTest" + dataPathLoc + str("%0.6f" % lr) + '.p', 'rb') as fp:
        totalAttackSuccessRateTest=pickle.load(fp)
        allAttackSuccessRateTestArray[l, :] = totalAttackSuccessRateTest

    ########################################################################################################################
    # plot clean accuracy and attack success rate line plots
    ########################################################################################################################
    fig, axs = plt.subplots(figsize=(10, 5))
    xticks = [str("%.0f" % (x * 100)) for x in totalPercentChannelsRemoved]
    xticks = np.asarray(xticks)[list(range(0, 61, 3))]
    axs.set_yticks(np.arange(0, 101, 10))
    axs.set_xticks(np.arange(0, 1.001, 0.05))
    axs.set_xticklabels(xticks, rotation=90)
    axs.tick_params(axis='x', labelsize=14)
    axs.tick_params(axis='y', labelsize=14)
    axs.set_ylabel('Rate', fontsize=16)
    axs.set_xlabel('Percent of channels removed', fontsize=16)
    axs.set_xlim([0, 1])
    axs.plot(totalPercentChannelsRemoved, totalCleanAccuracyTest, 'b-', linewidth=2,
             label="clean classification accuracy")
    axs.plot(totalPercentChannelsRemoved, totalAttackSuccessRateTest, 'r-', linewidth=2, label='attack success rate')
    font = font_manager.FontProperties(size=14)
    axs.legend(loc='best', prop=font)
    plt.grid()
    fig.tight_layout()
    if modelName == "Multitarget":
        figPathLoc = modelName + "_" + datasetName
    else:
        figPathLoc = modelName
    plt.savefig(data_path +"/RESULTS/FIGURES/totalAccuracySr_" + figPathLoc + "_test_" + "0_" + str("%0.6f" % lr).split('.')[1] + ".pdf")


########################################################################################################################
# plot clean test accuracy heatmap
########################################################################################################################


fig, axs = plt.subplots(nrows=5, ncols=1, figsize=(12,2.5), gridspec_kw={'hspace': 0, 'wspace': 0})
fig.canvas.draw()

xticks = [str("%.1f" % (x*100)) for x in totalPercentChannelsRemoved]

im=axs[0].imshow(np.asarray([allCleanAccuracyTestArray[-1,:]]),  cmap='coolwarm', interpolation='nearest', aspect='auto',vmin=0, vmax=100)
axs[0].set_xticks([], minor=False)
axs[0].set_yticks([0], minor=False)
axs[0].set_yticklabels(['$10^{-6}$'])
axs[0].spines['top'].set_visible(False)
axs[0].spines['bottom'].set_visible(False)

axs[1].imshow(np.asarray([allCleanAccuracyTestArray[-2,:]]),  cmap='coolwarm', interpolation='nearest', aspect='auto',vmin=0, vmax=100)
axs[1].set_xticks([], minor=False)
axs[1].set_yticks([0], minor=False)
axs[1].set_yticklabels(['$10^{-5}$'])
axs[1].spines['top'].set_visible(False)
axs[1].spines['bottom'].set_visible(False)

axs[2].imshow(np.asarray([allCleanAccuracyTestArray[-3,:]]),  cmap='coolwarm', interpolation='nearest', aspect='auto',vmin=0, vmax=100)
axs[2].set_xticks([], minor=False)
axs[2].set_yticks([0], minor=False)
axs[2].set_yticklabels(['$10^{-4}$'])
axs[2].spines['top'].set_visible(False)
axs[2].spines['bottom'].set_visible(False)
axs[2].set_ylabel('Learning Rate', fontsize = 14)

axs[3].imshow(np.asarray([allCleanAccuracyTestArray[-4,:]]),  cmap='coolwarm', interpolation='nearest', aspect='auto',vmin=0, vmax=100)
axs[3].set_xticks([], minor=False)
axs[3].set_yticks([0], minor=False)
axs[3].set_yticklabels(['$10^{-3}$'])
axs[3].spines['top'].set_visible(False)
axs[3].spines['bottom'].set_visible(False)

axs[4].imshow(np.asarray([allCleanAccuracyTestArray[-5,:]]),  cmap='coolwarm', interpolation='nearest', aspect='auto',vmin=0, vmax=100)
axs[4].set_xticks(np.array(range(0,61)), minor=False)
axs[4].set_xticklabels(xticks, rotation = 90)
axs[4].set_yticks([0], minor=False)
axs[4].set_yticklabels(['$10^{-2}$'])
axs[4].spines['top'].set_visible(False)

#plt.xlabel('Percent of channels removed', fontsize = 14)
plt.suptitle('Accuracy on the clean test data set for '+titleModelName +' model retrained with 10 epochs and different learning rates')
plt.subplots_adjust(left=0.07, bottom=0.3, right=0.94, top=None, wspace=None, hspace=None)
ax_x_start = 0.955
ax_x_width = 0.012
ax_y_start = 0.3
ax_y_height = 0.58
cbar_ax = fig.add_axes([ax_x_start, ax_y_start, ax_x_width, ax_y_height])
clb = fig.colorbar(im, cax=cbar_ax)
clb.mappable.set_clim(0.0,100.0)
clb.ax.set_title('', fontsize=14)  # title on top of colorbar
plt.savefig(data_path + "/RESULTS/FIGURES/cleanTestAccuracy" + dataPathLoc+".pdf")

########################################################################################################################
# plot attack success rate heatmap
########################################################################################################################
fig, axs = plt.subplots(nrows=5, ncols=1, figsize=(12,2.5), gridspec_kw={'hspace': 0, 'wspace': 0})
fig.canvas.draw()

xticks = [str("%.1f" % (x*100)) for x in totalPercentChannelsRemoved]

im=axs[0].imshow(np.asarray([allAttackSuccessRateTestArray[-1,:]]),  cmap='coolwarm', interpolation='nearest', aspect='auto',vmin=0, vmax=100)
axs[0].set_xticks([], minor=False)
axs[0].set_yticks([0], minor=False)
axs[0].set_yticklabels(['$10^{-6}$'])
axs[0].spines['top'].set_visible(False)
axs[0].spines['bottom'].set_visible(False)

axs[1].imshow(np.asarray([allAttackSuccessRateTestArray[-2,:]]),  cmap='coolwarm', interpolation='nearest', aspect='auto',vmin=0, vmax=100)
axs[1].set_xticks([], minor=False)
axs[1].set_yticks([0], minor=False)
axs[1].set_yticklabels(['$10^{-5}$'])
axs[1].spines['top'].set_visible(False)
axs[1].spines['bottom'].set_visible(False)

axs[2].imshow(np.asarray([allAttackSuccessRateTestArray[-3,:]]),  cmap='coolwarm', interpolation='nearest', aspect='auto',vmin=0, vmax=100)
axs[2].set_xticks([], minor=False)
axs[2].set_yticks([0], minor=False)
axs[2].set_yticklabels(['$10^{-4}$'])
axs[2].spines['top'].set_visible(False)
axs[2].spines['bottom'].set_visible(False)
axs[2].set_ylabel('Learning Rate', fontsize = 14)

axs[3].imshow(np.asarray([allAttackSuccessRateTestArray[-4,:]]),  cmap='coolwarm', interpolation='nearest', aspect='auto',vmin=0, vmax=100)
axs[3].set_xticks([], minor=False)
axs[3].set_yticks([0], minor=False)
axs[3].set_yticklabels(['$10^{-3}$'])
axs[3].spines['top'].set_visible(False)
axs[3].spines['bottom'].set_visible(False)

axs[4].imshow(np.asarray([allAttackSuccessRateTestArray[-5,:]]),  cmap='coolwarm', interpolation='nearest', aspect='auto',vmin=0, vmax=100)
axs[4].set_xticks(np.array(range(0,61)), minor=False)
axs[4].set_xticklabels(xticks, rotation = 90)
axs[4].set_yticks([0], minor=False)
axs[4].set_yticklabels(['$10^{-2}$'])
axs[4].spines['top'].set_visible(False)

plt.xlabel('Percent of channels removed', fontsize = 14)
plt.suptitle('Attack success rate on the backdoored test set for '+titleModelName +' model retrained with 10 epochs and different learning rates')
plt.subplots_adjust(left=0.07, bottom=0.3, right=0.94, top=None, wspace=None, hspace=None)
ax_x_start = 0.955
ax_x_width = 0.012
ax_y_start = 0.3
ax_y_height = 0.58
cbar_ax = fig.add_axes([ax_x_start, ax_y_start, ax_x_width, ax_y_height])
clb = fig.colorbar(im, cax=cbar_ax)
clb.mappable.set_clim(0.0,100.0)
clb.ax.set_title('', fontsize=14)  # title on top of colorbar
plt.savefig(data_path + "/RESULTS/FIGURES/attackSuccessRateTest" + dataPathLoc+".pdf")


