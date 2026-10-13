
from ordenacao import insercao

numeros = [1, 2, 3, 4]

resultado, comparacoes = insercao(numeros)

print("Lista original:", numeros)
print("Lista ordenada:", resultado)
print("Número de comparações:", comparacoes)
