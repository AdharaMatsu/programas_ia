def readDataset(filename, inputs, outputs):
    files = open(filename, "r")
    for line in files:
        temp = line.strip().split(",")
        inputs.append(temp[0:4])
        outputs.append([temp[4]])
    return inputs, outputs


def convertToFloat(listConvert):
    for i in range(len(listConvert)):
        for j in range(len(listConvert[i])):
            listConvert[i][j] = float(listConvert[i][j])
    return listConvert


def convertInt(listConvert):
    for i in range(len(listConvert)):
        for j in range(len(listConvert[i])):
            listConvert[i][j] = int(listConvert[i][j])
    return listConvert


def activation(x_row, weight):
    Z = 0
    for r in range(len(x_row)):
        Z = Z + (x_row[r] * weight[r])
    return Z


import random as rnd

X, Y = readDataset('iris.csv', [], [])
X = convertToFloat(X)
Y = convertInt(Y)
Y = [e[0] for e in Y]

W = [rnd.uniform(-1, 1) for _ in range(4)]
bias = rnd.uniform(-1, 1)

learning_rate = 0.01
#epoch = 1
mse = 1

while mse != 0:
    sum_error = 0
    for i in range(len(X)):
        Yin = activation(X[i], W)
        Yin = Yin + bias
        error = Y[i] - Yin
        W[0] = W[0] + learning_rate * error * X[i][0]
        W[1] = W[1] + learning_rate * error * X[i][1]
        W[2] = W[2] + learning_rate * error * X[i][2]
        W[3] = W[3] + learning_rate * error * X[i][3]

        bias += (learning_rate * error) # *-1
        sum_error += error ** 2

    if mse == sum_error:
        break

    mse = sum_error
    #epoch += 1

X_test, Y_test = readDataset('iris.csv', [], [])
X_test = convertToFloat(X_test)
Y_test = convertInt(Y_test)
Y_test = [e[0] for e in Y_test]

cont = 0
for i in range(len(X_test)):
    Y_ob = activation(X_test[i], W)
    if (Y_ob < 0 and Y_test[i] == 0) or (0 < Y_ob < 1 and Y_test[i] == 1) or (1 < Y_ob < 2 and Y_test[i] == 2):
        cont += 1

print('Efectividad: ', cont / len(X_test) * 100)
