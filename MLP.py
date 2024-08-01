import csv
import random as rnd
import math
def convertTo(dataset, type):
    for row in range(len(dataset)):
        for column in range(len(dataset[row])):
            if type:
                dataset[row][column] = float(dataset[row][column])
            else:
                dataset[row][column] = int(dataset[row][column])
    return dataset
def convertToInt(dataset):
    for e in range(len(dataset)):
        dataset[e] = int(dataset[e])
    return dataset
def readCSV(filename, input, output):
    file = open(filename, "r")
    for info in file:
        temp = info.strip().split(',')
        output.append(temp.pop(-1))
        input.append(temp)
    return convertTo(input,1), convertToInt(output)

rnd.seed(42)
X, Y = readCSV('prueba.csv', [], [])
inputLayer = len(X)
hiddenLayer = 2

def createWeightMatrix(input, hidden, state):
    matrix = [[[] for _ in range(hidden)] for _ in range(input)]
    if state:
        for i in range(input):
            for j in range(hidden):
                matrix[i][j] = [rnd.uniform(-1, 1), rnd.uniform(-1, 1),rnd.uniform(-1, 1),rnd.uniform(-1, 1)]
    else:
        for i in range(input):
            for j in range(hidden):
                matrix[i][j] = [rnd.uniform(-1, 1)]
    return matrix

W = createWeightMatrix(inputLayer, hiddenLayer,  1)
print('W1: ', W)

bias = rnd.uniform(-1, 1)
learning_rate = 0.01

def activation(input, w_row, sizeColumn, X_new, Z=0):
    for e in range(sizeColumn):
        column = [f[e] for f in w_row]
        for i in range(len(column)):
            for j in range(len(column[i])):
                Z = Z + input[i][j] * column[i][j]
        F = 1/(1+(math.e**((-1)*Z)))
        X_new.append(F)
    return X_new

X_hidden = activation(X, W, len(W[0]), [])
print('Hidden Layers: ', X_hidden)
outputLayer = 3
W2 = createWeightMatrix(hiddenLayer, outputLayer, 0)
print('W2: ', W2)
Z = 0
Yin = []
for i in range(len(W2[0])):
    column_actual = [row[i] for row in W2]
    for j in range(len(column_actual)):
        Z = Z + column_actual[j][0] * X_hidden[j]
    sigm = 1 / (1 + (math.e ** ((-1) * Z)))
    Yin.append(sigm)
print(Yin)

