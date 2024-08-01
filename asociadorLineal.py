# CHECAR CODIGO PARA ASOCIADOR LINEAL

import numpy as np
def readDataset(filename, inputs, outputs):
    files = open(filename, "r")
    for line in files:
        temp = line.strip().split(",")
        inputs.append(temp[0:4])
        outputs.append([temp[4]])
    return inputs, outputs

if __name__ == '__main__':
    X_train, Y_train = readDataset('iris.csv', [], [])
    Y = np.zeros((len(X_train), 3))

    for lines in range(len(Y_train)):
        if Y_train[lines] == ['0']:
            Y[lines,0] = 1
        elif Y_train[lines] == ['1']:
            Y[lines, 1] = 1
        elif Y_train[lines] == ['2']:
            Y[lines, 2] = 1

    X = np.array(X_train, dtype=float)

    X_pseudo = np.linalg.pinv(X)
    W = np.dot(X_pseudo, Y)

    X_test, Y_test = readDataset('iris.csv',[],[])

    X_new = np.array(X_test, dtype=float)
    prediction = np.dot(X_new, W)

    for i in range(len(Y_test)):
        print(prediction[i],'  -  ', Y_test[i])

