#Programa que apresente o maior e o menor elemento de uma lista de 10 elementos sem precisar ordenar.

list=[1,2,7,8,19,40,34,67,100,3]
max=list[0]              #o valor de max=1, pois o elemento da posição 0=1
min=list[0]              # o valor de min=1,  pois o elemento da posição 0=1

for i in list[1:]:       # loop para verificar os valores a partir da posição 1
    if i>max:            # condição para verificar se o número é maior que "max"
        max=i            # atribui o número como o maior
    else:
        if i<min:        # condição para verificar se o número é menor que "min"
            min=i        # atribui o número como o menor
    print(max)
    print(min)