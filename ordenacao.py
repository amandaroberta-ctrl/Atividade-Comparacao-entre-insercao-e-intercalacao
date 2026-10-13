
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


def intercala(lista):
    if len(lista) <= 1:
        return lista.copy(), 0

    meio = len(lista) // 2
    esquerda = lista[:meio]
    direita = lista[meio:]

    esquerda, comp_esq = intercala(esquerda)
    direita, comp_dir = intercala(direita)

    resultado = []
    i = 0
    j = 0
    comparacoes = comp_esq + comp_dir

    while i < len(esquerda) and j < len(direita):
        comparacoes += 1

        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado, comparacoes
