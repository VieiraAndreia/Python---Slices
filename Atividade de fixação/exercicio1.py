#Programa que ordena uma lista de 10 números em ordem crescente (buble sort) e despois apresente como resultado a lista em ordem decrescente usando slices.


list=[1,2,7,8,19,40,34,67,100,3]

#algoritmo buble sort
for i in range(len(list)-1):                  # "len(list)-1" ordena o elemento até o penúltimo número
    for j in range(i+1,len(list)):            #  percorre os elementos que não foram ordenados ainda
        if list[i]>list[j]:                   #  if usado para comparar os elementos
            list[i],list[j]=list[j],list[i]   #  se o if for verdadeiro troca-se a posição 
#slice
print(list[::-1])                             #os dois pontos fazem com que a busca comece da esquerda