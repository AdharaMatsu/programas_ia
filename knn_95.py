import math as mat

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
    sort(data)
    f = [['Iris-virginica', 0], ['Iris-versicolor', 0], ['Iris-setosa', 0]]

    for e in range(0,k):
        if data[e][1] == 'Iris-virginica':
            f[0][1] += 1
        elif data[e][1] == 'Iris-versicolor':
            f[1][1] += 1
        else:
            f[2][1] += 1

    return f

def efectividad(dataset_freq, data_prueba):
    cont = 0
    for e in range(len(dataset_freq)):
        lista_ordenada = sorted(dataset_freq[e], key=lambda x: x[1])
        if lista_ordenada[2][0] == data_prueba[e][4]:
            cont = cont + 1

    print(cont,'/',str(len(data_prueba)))
    print(cont/len(data_prueba)*100)

if __name__ == '__main__':
    '''''
    irisData = create_Data("iris.data")

    entrenamiento = []
    prueba = []

    large = int(len(irisData)*0.80)

    for e in range(len(irisData)):
        if e >= large:
            prueba.append(irisData[e])
        else:
            entrenamiento.append(irisData[e])
    '''
    entrenamiento = create_Data('entrenamiento.csv')
    prueba = create_Data('prueba.csv')
    vector_freq = []

    for e in prueba:
        vector = knn(entrenamiento,e)
        vector_freq.append(frequency(vector, 7))

    efectividad(vector_freq, prueba)
