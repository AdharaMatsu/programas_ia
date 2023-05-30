import math as mat
import csv
def create():
    dataset = []
    file = open("iris.data", "r")
    for line in file:
        temp = line.strip().split(",")
        dataset.append(temp)

        for e in range(len(dataset)):
            for i in range(0, 4):
                dataset[e][i] = float(dataset[e][i])
    return dataset
def knn(dataset, caso):
    data = []
    for e in range(len(dataset)):
        cont = 0
        i = 0
        while i < 4:
            cont = cont + ((dataset[e][i] - caso[i]) ** 2)
            i = i + 1
        data.append(((str(mat.sqrt(cont))).split()) + ((dataset[e][4]).split()))

    for x in range(len(data)):
        data[x][0] = float(data[x][0])

    return data
def showCSV(dataset,filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for e in range(len(dataset)):
            writer.writerow(dataset[e])

if __name__ == '__main__':
    data = create()
    archivo = create()

    while len(archivo) > 1:
        x = archivo.pop(0)

        vector = knn(archivo, x)

        if vector[0][1] != x[4]:
            c = data.pop(0)
    showCSV(data, 'wilson.csv')




