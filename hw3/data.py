import pandas as pd
import numpy as np

def data():
    dataframe = pd.read_csv('./sgb-words.txt',header=None)
    words = np.array(dataframe)
    words = words.reshape((-1,))

    f = open("graph.txt", "r")
    lines = f.readlines()
    link = []
    for line in lines:
        linki = [int(x) for x in line.split(' ')]
        link.append(linki[1:])
    return words, link

def getBetweenness():
    f = open("betweenness.txt", "r")
    lines = f.readlines()
    betweenness = []
    for line in lines:
        betweennessi = [float(x) for x in line.split(' ')]
        betweenness.append(betweennessi[1:])
    return betweenness