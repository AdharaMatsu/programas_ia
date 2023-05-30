import csv
import math as mat


def KNN(dataEntrenamiento, dataPrueba):
    data = []
    for e in range(len(dataEntrenamiento)):
        cont = 0
        i = 0
        while i < 4:
            cont = cont + ((dataEntrenamiento[e][i] - dataPrueba[i]) ** 2)
            i = i + 1
        data.append(((str(mat.sqrt(cont))).split()) + ((dataEntrenamiento[e][4]).split()))

        for x in range(len(data)):
            data[x][0] = float(data[x][0])
    return data


def copyPrueba():
    file = open("prueba.csv", "r")

    data = []

    for line in file:
        temp = line.strip().split(",")
        data.append(temp)

        for e in range(len(data)):
            for i in range(0, 4):
                data[e][i] = float(data[e][i])
    return data


def search(position, caso):
    C = copyPrueba()
    if C[position][4] == caso[0][1]:
        return 'Si'
    else:
        return 'No'

def sort(data):
    temp = [[0.0, '']]
    for y in range(0, len(data)):
        for z in range(y + 1, len(data)):
            if data[z][0] < data[y][0]:
                temp[0] = data[z]
                data[z] = data[y]
                data[y] = temp[0]
def splitValidation(entrenamiento, prueba):
    cont = 0
    for e in range(len(prueba)):
        caso = KNN(entrenamiento, prueba[e])
        sort(caso)
        if search(e, caso) == 'Si':
            cont = cont + 1
    ef = efectividad(cont, len(prueba))
    return ef


def efectividad(cont_Si, n_casos):
    return cont_Si / n_casos * 100

data_entrenamiento = []
data_prueba = []

file = open("entrenamiento.csv", "r")

for line in file:
    temp = line.strip().split(",")
    data_entrenamiento.append(temp)

    for e in range(len(data_entrenamiento)):
        for i in range(0, 4):
            data_entrenamiento[e][i] = float(data_entrenamiento[e][i])

file = open("prueba.csv", "r")

for line in file:
    temp = line.strip().split(",")
    data_prueba.append(temp)

    for e in range(len(data_prueba)):
        for i in range(0, 4):
            data_prueba[e][i] = float(data_prueba[e][i])
print('Efectividad: ', splitValidation(data_entrenamiento,data_prueba))

