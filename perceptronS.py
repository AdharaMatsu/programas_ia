def convertToInt(listConvert):
    for i in range(len(listConvert)):
        for j in range(len(listConvert[i])):
            listConvert[i][j] = int(listConvert[i][j])
    return listConvert


def readDataset(filename, inputs, outputs):
    file = open(filename, "r")
    for f in file:
        temp = f.strip().split(' ')

        inputs.append(temp[0:2])
        outputs.append(temp[2])
    inputs = convertToInt(inputs)
    for i in range(len(outputs)):
        outputs[i] = int(outputs[i])
    return inputs, outputs


def activacion(pesos, x, b):
    z = pesos * x
    if z.sum() + b > 0:
        return 1
    else:
        return -1


import numpy as np

X, Y = readDataset('separable.txt', [], [])
W = np.random.uniform(-1, 1, size=2)
b = np.random.uniform(-1, 1)

tasa_aprendizaje = 0.01

epoch = 100
error = -1
while error != 0:
    for i in range(len(X)):
        pred = activacion(W, X[i], b)
        error = Y[i] - pred
        W[0] += tasa_aprendizaje * X[i][0] * error
        W[1] += tasa_aprendizaje * X[i][1] * error

        b += tasa_aprendizaje * error
print('W: ', W, ' Bias: ', b)
print(activacion(W, [1, 2], b))
#   revisar por que da 1 ahora que se cambio el error
