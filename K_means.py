import math
import random as rand

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

def PrintToFile(dataset, G):
    file = open("Resultado.txt", "w")

    for i in range(len(dataset)):
        file.write("\t".join([str(x) for x in dataset[i]]) + "\t" + str(G[i]) + "\n")
    file.close()
def InitializeC(list_ds, list_dsT):
    C = [[0 for j in range(len(list_ds[0]))] for i in range(k)]

    for i in range(len(C)):
        for j in range(a):
            maxV = math.ceil(max(list_dsT[j]))
            minV = math.floor(min(list_dsT[j]))
            #C[i][j] = rand.randint(minV, maxV)
            C[i][j] = rand.uniform(minV, maxV)

    return C
def distf(dsRow, CRow):
    global a
    sum = 0
    for j in range(a):
        sum += (dsRow[j] - CRow[j]) ** 2
    return sum


def encuentraGrupos():
    modEnGrupo = False
    for i in range(len(G)):
        distMin = 99999999
        lMin = -1

        for l in range(k):
            dist = distf(dataset[i], C[l])

            if dist < distMin:
                distMin = dist
                lMin = l

        if G[i] != lMin:
            modEnGrupo = True
            G[i] = lMin

    return G, modEnGrupo


def actualizarCentroides():
    cont = [0 for i in range(k)]

    for i in range(n):
        cont[G[i]] += 1
        for j in range(a):
            C[G[i]][j] += dataset[i][j]

    for i in range(k):
        for j in range(a):
            if cont[i] == 0:
                C[i][j] = 0
            else:
                C[i][j] /= cont[i]

    return C

if __name__ == '__main__':
    continuar = True
    #dataset = create_Data('iris.data')
    dataset = create_Data('irisData_process.csv')
    n = len(dataset)

    rand.seed(1234)

    for row in dataset:
        row.pop(-1)
    dsT = list(zip(*dataset))
    a = len(dataset[0])

    k = 3
    C = InitializeC(dataset, dsT)

    G = [-1 for x in range(n)]

    max_iteraciones = 20
    iteraciones = 0

    while continuar and iteraciones < max_iteraciones:
        continuar = False
        G, continuar = encuentraGrupos()
        C = actualizarCentroides()
        iteraciones += 1

    freq = [0,0,0]
    for e in G:
        if e == 0:
            freq[0] = freq[0] + 1
        elif e == 1:
            freq[1] = freq[1] + 1
        else:
            freq[2] = freq[2] + 1
    sum = 0
    print(freq)
    for e in freq:
        if e > 50:
           sum += 50
        else:
            sum += e
    print(sum,'/',str(150))
    print(sum/150*100)
    PrintToFile(dataset,G)
