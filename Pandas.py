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

#localizar valores de linhas, para colunas usar a notação de df['A']
df.loc['B']
df.loc['B',0]
df.loc[['A','B'],[0,1]]

#localizar por indices de numpy
df.iloc[1]
df.iloc[1:2,0:1]
df.iloc[0:2,0:2]

#criação de df
df1 = pd.DataFrame(np.random.randn(5,4), index='A B C D E'.split(), columns='W X Y Z'.split())
#print(df1)

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

# print('\t')
# print(df1[(df1['W']>0) & (df1['Y']<0)]) #duas condicionais com lógica E
# print(df1[(df1['W']>0) | (df1['Y']<0)]) #duas condicionais com lógica OU

#df1.reset_index() #reseta os indices para números e cria uma coluna "index" na qual estão os índices em letras

col = 'A1 B2 C3 D4 E5'.split()

df1['COD'] = col

df1.set_index('COD', inplace=True) #muda o índice do df para a coluna determinada

#indice multinivel do df

outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside)) #cria lista de tuplas em que cada valor de outside é colocado com o correspondente em inside
hier_index = pd.MultiIndex.from_tuples(hier_index) #cria hierarquia de index

df3 = pd.DataFrame(np.random.randn(6,2), index=hier_index, columns=[('A B').split()])

#df3.loc['G1'].loc[1]) #procurar os valores no grupo 1 na linha 1 (retorna uma series)

# df3.index.names=['Group', 'Number'] #da nomes aos índices do df
# print(df3)

# df3.xs(1, level='Number') #cross section, melhor que o loc pq posso ignorar os níveis externos

#dados ausentes

d = {'A':[1,2,np.nan], 'B':[5,np.nan,np.nan], 'C':[1,2,3]}
df4 = pd.DataFrame(d)
# print(df4)
# print('\t')

#df4.dropna() #exclui o eixo que possui NaN

#df4.dropna(thresh=2) #exclui eixos com o numero NaNs especificado

#df4.fillna(value=1) #substitui NaN pelo valor

#df4['A'].fillna(value=df4['A'].mean()) # mean() --> média

#df4.fillna(method='ffill') #foward fill -> preenche com os dados anteriores

#group by

data = {'Empresa':('GOOG GOOG MSFT MSFT FB FB').split(),
        'Nome':('Sam Charlie Amy Vanessa Carl Sarah').split(),
        'Venda':[200,120,340,124,243,350]}

df5 = pd.DataFrame(data)
print(df5)
print('\t')

group = df5.groupby('Empresa') #variavel que possui o agrupamento
#group.sum() #retorna df com a soma dos valores correspondentes aos agrupamentos
#group.mean() #retorna df com a média dos valores correspondentes aos agrupamentos

#group.describe() #aponta uma serie de metodos pre aplicados

#group.sum().loc['GOOG'] #mostra um valor específico correspondente a soma de valores de GOOG