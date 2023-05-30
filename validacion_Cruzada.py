import math as mat
def readData():
    file = open("iris.data", "r")

    data = []

    for line in file:
        temp = line.strip().split(",")
        data.append(temp)

        for e in range(len(data)):
            for i in range(0, 4):
                data[e][i] = float(data[e][i])
    return data
def sort(data):
    temp = [[0.0, '']]
    for y in range(0, len(data)):
        for z in range(y + 1, len(data)):
            if data[z][0] < data[y][0]:
                temp[0] = data[z]
                data[z] = data[y]
                data[y] = temp[0]

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
    sort(data)
    return data[0]


if __name__ == '__main__':
    number_folds = 10
    irisData = readData()
    cantidad_datos = int(len(irisData) / number_folds)
    cont = 0
    prueba = []
    for v in range(number_folds):
        prueba.extend(irisData[:cantidad_datos])
        del irisData[:cantidad_datos]

        for e in prueba:
            x = knn(irisData,e)
            if x[1] == e[4]:
                cont += 1
        while len(prueba) > 0:
            irisData.append(prueba.pop(0))

    print(cont,'/', str(150))
    print('Efectividad:', cont/150*100,'%')