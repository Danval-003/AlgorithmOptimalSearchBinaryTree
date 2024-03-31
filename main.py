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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    OptimalBST([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
