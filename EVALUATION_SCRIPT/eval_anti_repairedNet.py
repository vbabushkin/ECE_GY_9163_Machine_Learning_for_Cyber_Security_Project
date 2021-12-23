import keras
import sys
import numpy as np
import cv2

data_filename = str(sys.argv[1])
BadNet_filename = str(sys.argv[2])
Anti_RepairedNet_filename = str(sys.argv[3])


def image_loader(filepath):
    x_data = cv2.imread(filepath)
    x_data = cv2.cvtColor(x_data, cv2.COLOR_BGR2RGB)  # BGR -> RGB
    x_data = np.expand_dims(x_data,axis=0)  # add the singleton dimension to the input image to make it suitable for network
    return x_data


def main():
    BadNet = keras.models.load_model(BadNet_filename)
    Anti_RepairedNet = keras.models.load_model(Anti_RepairedNet_filename)

    x = image_loader(data_filename)

    yhat = np.argmax(BadNet(x), axis=1)[0]
    yhat_prime = np.argmax(Anti_RepairedNet(x), axis=1)[0]

    if yhat != yhat_prime:
        res = yhat
    else:
        res= 1283
    print(
        "Badnet predicted label: {0:>15d}\nAnti-Repaired Network predicted label: {1:>5d}\nGoodnet G predicted label: {2:>12d}".format(
            yhat, yhat_prime, res))
    return res

if __name__ == '__main__':
    main()
