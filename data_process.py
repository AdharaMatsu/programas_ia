import numpy as np
import csv

def create_Data(file_name):
    file = open(file_name, "r")
    dataset = []

    for line in file:
        temp = line.strip().split(",")
        dataset.append(temp)

        for e in range(len(dataset)):
            for i in range(0, 4):
                dataset[e][i] = float(dataset[e][i])

    return dataset
def toFloat(data):
    data_float = []
    for row in data:
        data_float.append(float(row))

    return data_float

def normalizar(dataset):
    dataT = list(zip (* dataset))
    for e in range(4):
        maxV = max(dataT[e])
        minV = min(dataT[e])
        for row in dataset:
            row[e] = 100 * (row[e] - minV) / (maxV - minV)

def estandarizacion(dataset):
    dataT = list(zip (* dataset))
    for e in range(4):
        dataT_float = toFloat(dataT[e])
        promedio = np.average(dataT_float)
        stdDev = np.std(dataT_float)
        for row in dataset:
            row[e] = (row[e] - promedio) / stdDev

def showCSV(dataset,filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for e in range(len(dataset)):
            writer.writerow(dataset[e])
if __name__ == '__main__':
    dataset = create_Data('iris.data')
    n = len(dataset)

    for row in dataset:
        row.pop(-1)
    estandarizacion(dataset)
    normalizar(dataset)
    showCSV(dataset,'irisData_process.csv')
