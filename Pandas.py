import numpy as np
import pandas as pd

# séries
# labels = ['a', 'b', 'c']
# lista = [10,20,30]
# arr = np.array(lista)
# d = {'a':10, 'b':20, 'c':30}

# series = pd.Series(data=lista, index=labels) #data poderia ser lista ou arr nesse caso

# series1 = pd.Series([sum, print, len])

# series2 = pd.Series([1,2,3,4], index=['EUA', 'ALEMANHA', 'URSS', 'JAPÃO'])
# series3 = pd.Series([1,2,3,4], index=['EUA', 'ALEMANHA', 'ITÁLIA', 'JAPÃO'])

# series2 + series3 soma os dados e onde indices diferentes retornam NaN

# -------------------------------------------------------------------------------------------------------#

# np.random.seed(101) #os mesmos numeros são gerados em qualquer computador

# criação do dataframe
# df = pd.DataFrame(np.random.randn(5,4), index='A B C D E'.split())    #split() ---> lista a partir de uma string

# criação de coluna no df
# df['novo'] = df[0] + df[1]

# print(df)

# tirar itens do dataframe
# df = df.drop('novo', axis=1) #eixo de referencia axis=0 (indices)

# ou

# df.drop('novo', axis=1, inplace=True) #inplace substitui o df original pelo df criado 

# localizar valores de linhas, para colunas usar a notação de df['A']
# df.loc['B']
# df.loc['B',0]
# df.loc[['A','B'],[0,1]]

# localizar por indices de numpy
# df.iloc[1]
# df.iloc[1:2,0:1]
# df.iloc[0:2,0:2]

# criação de df
# df1 = pd.DataFrame(np.random.randn(5,4), index='A B C D E'.split(), columns='W X Y Z'.split())
# print(df1)

# teste condicional de df
# df2 = df1>0
# print(df2)

# print(df1[df2]) #retorna df testado pela condicional 

# print('\t')
# print(df1[df1['Z']>0]) #retorna df somente com as linhas onde Z > 0

# print('\t')
# print(df1[df1['Z']>0]['Y']) #retorna a coluna Y somente com as lihas nas quais Z > 0

# print('\t')
# print(df1[df1<0]['W']) #retorna a coluna W com resultados negativos e resultados positivos mostrados como NaN

# print('\t')
# print(df1[(df1['W']>0) & (df1['Y']<0)]) #duas condicionais com lógica E
# print(df1[(df1['W']>0) | (df1['Y']<0)]) #duas condicionais com lógica OU

# df1.reset_index() #reseta os indices para números e cria uma coluna "index" na qual estão os índices em letras

# col = 'A1 B2 C3 D4 E5'.split()

# df1['COD'] = col

# df1.set_index('COD', inplace=True) #muda o índice do df para a coluna determinada

# indice multinivel do df

# outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
# inside = [1, 2, 3, 1, 2, 3]
# hier_index = list(zip(outside, inside)) #cria lista de tuplas em que cada valor de outside é colocado com o correspondente em inside
# hier_index = pd.MultiIndex.from_tuples(hier_index) #cria hierarquia de index

# df3 = pd.DataFrame(np.random.randn(6,2), index=hier_index, columns=[('A B').split()])

# df3.loc['G1'].loc[1]) #procurar os valores no grupo 1 na linha 1 (retorna uma series)

# df3.index.names=['Group', 'Number'] #da nomes aos índices do df
# print(df3)

# df3.xs(1, level='Number') #cross section, melhor que o loc pq posso ignorar os níveis externos

# dados ausentes

# d = {'A':[1,2,np.nan], 'B':[5,np.nan,np.nan], 'C':[1,2,3]}
# df4 = pd.DataFrame(d)
# print(df4)
# print('\t')

# df4.dropna() #exclui o eixo que possui NaN

# df4.dropna(thresh=2) #exclui eixos com o numero NaNs especificado

# df4.fillna(value=1) #substitui NaN pelo valor

# df4['A'].fillna(value=df4['A'].mean()) # mean() --> média

# df4.fillna(method='ffill') #foward fill -> preenche com os dados anteriores

# group by

# data = {'Empresa':('GOOG GOOG MSFT MSFT FB FB').split(),
#         'Nome':('Sam Charlie Amy Vanessa Carl Sarah').split(),
#         'Venda':[200,120,340,124,243,350]}

# df5 = pd.DataFrame(data)
# print(df5)
# print('\t')

# group = df5.groupby('Empresa') #variavel que possui o agrupamento
# group.sum() #retorna df com a soma dos valores correspondentes aos agrupamentos
# group.mean() #retorna df com a média dos valores correspondentes aos agrupamentos

# group.describe() #aponta uma serie de metodos pre aplicados

# group.sum().loc['GOOG'] #mostra um valor específico correspondente a soma de valores de GOOG

# mesclar, juntar e concatenar

# dtf1 = pd.DataFrame(['A0 B0 C0 D0'.split(),
#                 'A1 B1 C1 D1'.split(),
#                 'A2 B2 C2 D2'.split(),
#                 'A3 B3 C3 D3'.split()],
#                 columns='A B C D'.split())

# dtf2 = pd.DataFrame(['A4 B4 C4 D4'.split(),
#                 'A5 B5 C5 D5'.split(),
#                 'A6 B6 C6 D6'.split(),
#                 'A7 B7 C7 D7'.split()],
#                 index='4 5 6 7'.split(),
#                 columns='A B C D'.split())

# dtf3 = pd.DataFrame(['A8 B8 C8 D8'.split(),
#                 'A9 B9 C9 D9'.split(),
#                 'A10 B10 C10 D10'.split(),
#                 'A11 B11 C11 D11'.split()],
#                 index='8 9 10 11'.split(),
#                 columns='A B C D'.split())

# print(dtf1)
# print('\t')
# print(dtf2)
# print('\t')
# print(dtf3)
# print('\t')

# quando dois dfs são concatenados, são colocados em sequência em um determinado eixo
# print(pd.concat([dtf1, dtf2, dtf3], axis=0)) #concatenação de dfs, o eixo de concatenação sempre deve ter o mesmo tamanho

# output:

#       A    B    C    D
# 0    A0   B0   C0   D0
# 1    A1   B1   C1   D1
# 2    A2   B2   C2   D2
# 3    A3   B3   C3   D3
# 4    A4   B4   C4   D4
# 5    A5   B5   C5   D5
# 6    A6   B6   C6   D6
# 7    A7   B7   C7   D7
# 8    A8   B8   C8   D8
# 9    A9   B9   C9   D9
# 10  A10  B10  C10  D10
# 11  A11  B11  C11  D11

# esquerda = pd.DataFrame({'key':'K0 K1 K2 K3'.split(),
#                 'A':'A0 A1 A2 A3'.split(),
#                 'B':'B0 B1 B2 B3'.split()})

# direita = pd.DataFrame({'key':'K0 K1 K2 K3'.split(),
#                 'C':'C0 C1 C2 C3'.split(),
#                 'D':'D0 D1 D2 D3'.split()})

# print(esquerda)
# print('\t')
# print(direita)
# print('\t')

# print(pd.merge(esquerda, direita, how='inner', on='key')) #junta dfs de acordo com um elemento em comum

# output:

#   key   A   B   C   D
# 0  K0  A0  B0  C0  D0
# 1  K1  A1  B1  C1  D1
# 2  K2  A2  B2  C2  D2
# 3  K3  A3  B3  C3  D3

# esq = pd.DataFrame({'A':'A0 A1 A2'.split(),
#                 'B':'B0 B1 B2'.split()},
#                 index='K0 K1 K2'.split(),)

# drt = pd.DataFrame({'C':'C0 C2 C3'.split(),
#                 'D':'D0 D2 D3'.split()},
#                 index='K0 K2 K3'.split())

# print(esq)
# print('\t')
# print(drt)
# print('\t')

# join junta dois dfs para unir valores em um único df uma vez que possui indices iguais
# print(esq.join(drt, how='outer')) #sem parametro how estaríamos usando apenas os índices do df "esq", usando o outer ele usa todos os índices dos dois preenchendo com NaN caso não haja informação

# output:

#       A    B    C    D
# K0   A0   B0   C0   D0
# K1   A1   B1  NaN  NaN
# K2   A2   B2   C2   D2
# K3  NaN  NaN   C3   D3

# operações entre dfs no pandas

# df = pd.DataFrame({'col1':[1,2,3,4],
#                 'col2':[444, 555, 666, 444],
#                 'col3':'abc def ghi xyz'.split()}) 
                
#o método split não converte str em int automaticamente

# print(df['col2'].unique()) #método unique retorna uma lista apenas de valores únicos do eixo selecionado
# print(df['col2'].nunique()) #método nunique retorna o número de valores únicos do eixo selecionado, mesma coisa que usar len(df[coluna].unique())

# print(df['col2'].value_counts()) #retorna um df com os itens do df inicial e o número de aparições na seção especificada

# def vezes2(x):
#         return x*2

# print(df['col1'].apply(vezes2)) #apply aplica funções preestabelecidas no df especificado

# print(df['col1'].apply(lambda x: x*2)) #apply também funciona com lambdas

# del df['col1'] #função de deletar colunas embutida no python

# print(df)

#df.columns retorna as colunas e df.index retorna os índices

# print(df.sort_values(by='col2')) #rearranja o df de acordo com os valores especificados

#df.isnull() retorna um df de booleanos indicando valores nulos

#pivot_table funciona como uma tabela dinamica (reordem de dados)

# df = pd.DataFrame({'A':'foo foo foo bar bar bar'.split(),
#                 'B':'one one two two one one'.split(),
#                 'C':'x y x y x y'.split(),
#                 'D':[1,2,3,5,4,1]}) 

# print(df.pivot_table(values='D', index=['A', 'B'], columns=['C']))

# output:

# C          x    y
# A   B
# bar one  4.0  1.0
#     two  NaN  5.0
# foo one  1.0  2.0
#     two  3.0  NaN