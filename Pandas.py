import numpy as np
import pandas as pd

#séries
labels = ['a', 'b', 'c']
lista = [10,20,30]
arr = np.array(lista)
d = {'a':10, 'b':20, 'c':30}

series = pd.Series(data=lista, index=labels) #data poderia ser lista ou arr nesse caso

series1 = pd.Series([sum, print, len])

series2 = pd.Series([1,2,3,4], index=['EUA', 'ALEMANHA', 'URSS', 'JAPÃO'])
series3 = pd.Series([1,2,3,4], index=['EUA', 'ALEMANHA', 'ITÁLIA', 'JAPÃO'])

#series2 + series3 soma os dados e onde indices diferentes retornam NaN

#-------------------------------------------------------------------------------------------------------#

np.random.seed(101) #os mesmos numeros são gerados em qualquer computador

#criação do dataframe
df = pd.DataFrame(np.random.randn(5,4), index='A B C D E'.split())    #split() ---> lista a partir de uma string

#criação de coluna no df
df['novo'] = df[0] + df[1]

print(df)

#tirar itens do dataframe
#df = df.drop('novo', axis=1) #eixo de referencia axis=0 (indices)

#ou

df.drop('novo', axis=1, inplace=True)

#localizar valores 
df.loc['B']
df.loc['B',0]
df.loc[['A','B'],[0,1]]

#localizar por indices de numpy
df.iloc[1]
df.iloc[1:2,0:1]
df.iloc[0:2,0:2]