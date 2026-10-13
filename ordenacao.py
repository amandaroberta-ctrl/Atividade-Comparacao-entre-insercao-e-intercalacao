
def insercao(lista):
    valores = lista.copy()
    comparacoes = 0

    for i in range(1, len(valores)):
        atual = valores[i]
        j = i - 1

        while j >= 0:
            comparacoes += 1

            if valores[j] > atual:
                valores[j + 1] = valores[j]
                j -= 1
            else:
                break

        valores[j + 1] = atual

    return valores, comparacoes
