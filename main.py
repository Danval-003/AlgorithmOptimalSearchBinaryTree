import random
import time
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error


# Clase para definir un nodo de un árbol binario
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def OptimalBST(dataList, frequencyList):
    if len(dataList) == 0:
        return None
    if len(dataList) == 1:
        return Node(dataList[0])
    else:
        max_frequency = 0
        for i in range(len(frequencyList)):
            if frequencyList[i] > max_frequency:
                max_frequency = frequencyList[i]
        max_indices = [i for i, freq in enumerate(frequencyList) if freq == max_frequency]

        if len(max_indices) % 2 == 0:
            # Si hay un número par de índices máximos, devuelve el índice en la mitad del rango
            mid = max_indices[len(max_indices) // 2 - 1]
        else:
            # Si hay un número impar de índices máximos, devuelve el índice central
            mid = max_indices[len(max_indices) // 2]

        root = Node(dataList[mid])
        root.left = OptimalBST(dataList[:mid], frequencyList[:mid])
        root.right = OptimalBST(dataList[mid + 1:], frequencyList[mid + 1:])
        return root


def testTime(dataList, frequencyList):
    start = time.perf_counter()

    OptimalBST(dataList, frequencyList)

    end = time.perf_counter()

    print("Time: ", end - start)

    return end - start


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Prueba de tiempo
    dataTest = {}

    df2 = pd.read_csv('data2.csv')

    for i in range(len(df2)):
        tests = df2['test Array'][i].replace('[', '').replace(']', '').split(',')
        testsFrequency = df2['test Frequency'][i].replace('[', '').replace(']', '').split(',')
        testsFrequency = [float(i) for i in testsFrequency]
        tests = [int(i) for i in tests]
        dataTest[i] = testTime(tests, testsFrequency)

    # Crear un DataFrame con los datos
    # df = pd.read_csv('data.csv')
    df = pd.DataFrame(list(dataTest.items()), columns=['N', 'Time'])

    # df.to_csv('data.csv', index=False)

    # Graficar los datos
    plt.plot(df['N'], df['Time'])
    plt.xlabel('N')
    plt.ylabel('Time')
    plt.title('Time vs N')
    # Hacer una regresión lineal
    plt.plot(df['N'], df['Time'], 'o')
    m, b = np.polyfit(df['N'], df['Time'], 1)
    regression_line = m * df['N'] + b
    plt.plot(df['N'], regression_line)
    # calcular el error cuadrático medio
    r_squared = r2_score(df['Time'], regression_line)
    print('R^2 regresión lineal:', r_squared)
    mse = mean_squared_error(df['Time'], regression_line)
    print("Error cuadrático medio:", mse)

    plt.text(0.5, 0.9, f'$ lineal R^2 = {r_squared:.2f}$', ha='center', va='center', transform=plt.gca().transAxes, fontsize=12)
    # Hacer una regresión cuadrática
    plt.plot(df['N'], df['Time'], 'o')
    m, b, c = np.polyfit(df['N'], df['Time'], 2)
    cua_reg = m * df['N'] ** 2 + b * df['N'] + c
    plt.plot(df['N'], cua_reg)
    # calcular el error cuadrático medio de la regresión cuadrática
    r_squared = r2_score(df['Time'], cua_reg)
    print('R^2 regresión lineal:', r_squared)
    mse = mean_squared_error(df['Time'], cua_reg)
    print("Error cuadrático medio:", mse)

    plt.text(0.5, 0.7, f'$Quadratic R^2 = {r_squared:.2f}$', ha='center', va='center', transform=plt.gca().transAxes, fontsize=12)

    plt.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/