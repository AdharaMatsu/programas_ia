#   codigo para dividir dataset para validacion dividida y para knn con 95%
import csv
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

data = readData()
cont = 0

entrenamiento = []
prueba = []

for e in range(len(data)):
    if cont < 35:
        entrenamiento.append(data[e])
    elif cont >= 35:
        prueba.append(data[e])

    if cont == 50:
        cont = 0
    else:
        cont = cont + 1

with open('entrenamiento.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for e in range(len(entrenamiento)):
        writer.writerow(entrenamiento[e])

# for e in range(len(prueba)):
#    prueba[e].pop(4)


with open('prueba.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for e in range(len(prueba)):
        writer.writerow(prueba[e])
