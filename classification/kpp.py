import math as mt
import numpy as np
import pandas as pd
import collections as clt


class KPP():

    """
        Model k plus proche voisin
    """

    predict = []

    def __init__(self) -> None:
        self.predict = []

    def KPlusProcheVoisin(self, data: pd.DataFrame, compare : pd.DataFrame, K: int):

        rows, cols = data.shape
        rowsC, colsC = compare.shape
        resultat = []
        for i in range(rows):
            distances = []
            for j in range(rowsC):
                diff = np.array(data.iloc[i, :]) - np.array(compare.iloc[j,:cols])
                distance = np.sqrt(np.square(diff))
                distances.append((distance, compare.iloc[j, colsC]))
            distances = sorted(distances, key= lambda a: a[0])
            k_class = []
            for i in range(K):
                k_class.append(distances[i][1])
            cla = dict(clt.Counter(k_class))
            cla = sorted(cla.items(), key = lambda x:x[1], reverse= True)
            resultat.append(cla[0][1])
        return resultat


    def occurrence(self, data: list, predict: list):
        return sum(np.array(data) == np.array(predict))


