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

#print(df)

#tirar itens do dataframe
#df = df.drop('novo', axis=1) #eixo de referencia axis=0 (indices)

#ou

df.drop('novo', axis=1, inplace=True) #inplace substitui o df original pelo df criado 

#localizar valores 
df.loc['B']
df.loc['B',0]
df.loc[['A','B'],[0,1]]

#localizar por indices de numpy
df.iloc[1]
df.iloc[1:2,0:1]
df.iloc[0:2,0:2]

#criação de df
df1 = pd.DataFrame(np.random.randn(5,4), index='A B C D E'.split(), columns='W X Y Z'.split())
print(df1)

#teste condicional de df
df2 = df1>0
#print(df2)

#print(df1[df2]) #retorna df testado pela condicional 

#print('\t')
#print(df1[df1['Z']>0]) #retorna df somente com as linhas onde Z > 0

#print('\t')
#print(df1[df1['Z']>0]['Y']) #retorna a coluna Y somente com as lihas nas quais Z > 0

#print('\t')
#print(df1[df1<0]['W']) #retorna a coluna W com resultados negativos e resultados positivos mostrados como NaN

#print('\t')
#print(df1[(df1['W']>0) & (df1['Y']<0)]) #duas condicionais com lógica E
#print(df1[(df1['W']>0) | (df1['Y']<0)]) #duas condicionais com lógica OU

#df1.reset_index() #reseta os indices para números e cria uma coluna "index" na qual estão os índices em letras

col = 'A1 B2 C3 D4 E5'.split()

df1['COD'] = col

df1.set_index('COD', inplace=True) #muda o índice do df para a coluna determinada