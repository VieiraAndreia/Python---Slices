#Exemplo de como uma slice funciona
#Uma slice copia o conteudo da lista, por isso o resultado será 1.

list1=[1]         
list2=list1[:]          #o simbolo [:] é usado para copiar todos os elementos da lista

list1[0]=2

print(list2)