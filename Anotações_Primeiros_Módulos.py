#funções lambda
#para elevar os numeros de uma lista ao quadrado pode ser usada uma função lambda, afim de encurtar o código
l = [1,2,3,4,5,6]

print(list(map(lambda var: var**2, l)))

#uma função lambda também pode ser usada para criar condicionais booleanas
print(list(filter(lambda var: var%2==0, l)))