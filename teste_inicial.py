from ordenacao import insercao, intercala

numeros = [5, 2, 4, 1]

resultado_insercao, comp_insercao = insercao(numeros)
resultado_intercala, comp_intercala = intercala(numeros)

print("Lista original:", numeros)
print("Insercao:", resultado_insercao)
print("Comparacoes da insercao:", comp_insercao)
print("Intercalacao:", resultado_intercala)
print("Comparacoes da intercalacao:", comp_intercala)

assert resultado_insercao == [1, 2, 4, 5]
assert resultado_intercala == [1, 2, 4, 5]

print("Os dois algoritmos funcionaram!")
