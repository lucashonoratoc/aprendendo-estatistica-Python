import numpy as np
import pandas as pd
from math import ceil

população = 150
amostra = 15

k = ceil(população / amostra)

r = np.random.randint(low = 1, high = k + 1, size = 1)

acumulador = r[0]
sorteados = []
for i in range(amostra):
        sorteados.append(acumulador)
        acumulador += k
        
base = pd.read_csv('iris.csv')

base_final = base.loc[sorteados]