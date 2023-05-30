import csv
import math as mat

def createData():
    file = open("iris.data", "r")
    data = []
    for line in file:
        temp = line.strip().split(",")
        data.append(temp)

        for e in range(len(data)):
            for i in range(0, 4):
                data[e][i] = float(data[e][i])
    return data

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

def sort(data):
    temp = [[0.0, '']]
    for y in range(0, len(data)):
        for z in range(y + 1, len(data)):
            if data[z][0] < data[y][0]:
                temp[0] = data[z]
                data[z] = data[y]
                data[y] = temp[0]

def frequency(data, k):
    f = [['Iris-virginica', 0], ['Iris-versicolor', 0], ['Iris-setosa', 0]]

    for a in range(k):
        if data[a][1] == 'Iris-virginica':
            f[0][1] += 1
        elif data[a][1] == 'Iris-versicolor':
            f[1][1] += 1
        else:
            f[2][1] += 1

    sort(f)
    return f

def showCSV(dataset,filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for e in range(len(dataset)):
            writer.writerow(dataset[e])

if __name__ == '__main__':
    exam = [6.4, 3.1, 5.5, 1.8]
    irisData = createData()

    data = knn(irisData,exam)
    freq = frequency(data, 5)

    print("Contador: ", freq)
    print(exam, ' -> ', freq[-1][0])

    showCSV(data, 'k_neighbors.csv')