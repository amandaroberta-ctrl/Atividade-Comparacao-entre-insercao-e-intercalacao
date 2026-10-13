from ordenacao import insercao, intercala

casos = [
    ("Lista vazia", []),
    ("Um elemento", [7]),
    ("Todos iguais", [3, 3, 3, 3]),
    ("Já ordenada", [1, 2, 3, 4, 5]),
    ("Ordem inversa", [5, 4, 3, 2, 1]),
]

for nome, lista in casos:
    esperado = sorted(lista)

    resultado_insercao, _ = insercao(lista)
    resultado_intercala, _ = intercala(lista)

    assert resultado_insercao == esperado, nome
    assert resultado_intercala == esperado, nome

print("Todos os testes passaram!")