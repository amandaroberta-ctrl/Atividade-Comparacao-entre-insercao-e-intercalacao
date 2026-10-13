
import csv
import random
import time
from pathlib import Path
from statistics import mean

import matplotlib.pyplot as plt

from ordenacao import insercao, intercala


TAMANHOS = [5, 10, 20, 30, 50, 75, 100, 200, 500, 1000]
REPETICOES = 10
PASTA = Path(__file__).parent


def medir_tempo(funcao, lista):
    inicio = time.perf_counter()
    funcao(lista)
    fim = time.perf_counter()
    return fim - inicio


def contar_comparacoes_sorted(lista):
    class Numero:
        comparacoes = 0

        def __init__(self, valor):
            self.valor = valor

        def __lt__(self, outro):
            Numero.comparacoes += 1
            return self.valor < outro.valor

    valores = [Numero(x) for x in lista]
    Numero.comparacoes = 0
    sorted(valores)
    return Numero.comparacoes


def main():
    registros = []

    for n in TAMANHOS:
        print(f"Medindo listas de tamanho {n}...")

        for repeticao in range(1, REPETICOES + 1):
            lista = [random.randint(0, 10000) for _ in range(n)]

            tempo_insercao = medir_tempo(insercao, lista)
            tempo_intercala = medir_tempo(intercala, lista)
            tempo_sorted = medir_tempo(sorted, lista)

            _, comp_insercao = insercao(lista)
            _, comp_intercala = intercala(lista)
            comp_sorted = contar_comparacoes_sorted(lista)

            registros.append({
                "n": n,
                "repeticao": repeticao,
                "tempo_insercao": tempo_insercao,
                "tempo_intercala": tempo_intercala,
                "tempo_sorted": tempo_sorted,
                "comparacoes_insercao": comp_insercao,
                "comparacoes_intercala": comp_intercala,
                "comparacoes_sorted": comp_sorted,
            })

    arquivo_csv = PASTA / "dados.csv"

    with open(arquivo_csv, "w", newline="", encoding="utf-8") as arquivo:
        campos = list(registros[0].keys())
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(registros)

    resumo = []

    for n in TAMANHOS:
        grupo = [r for r in registros if r["n"] == n]

        resumo.append({
            "n": n,
            "tempo_insercao": mean(r["tempo_insercao"] for r in grupo),
            "tempo_intercala": mean(r["tempo_intercala"] for r in grupo),
            "tempo_sorted": mean(r["tempo_sorted"] for r in grupo),
            "comparacoes_insercao": mean(
                r["comparacoes_insercao"] for r in grupo
            ),
            "comparacoes_intercala": mean(
                r["comparacoes_intercala"] for r in grupo
            ),
            "comparacoes_sorted": mean(
                r["comparacoes_sorted"] for r in grupo
            ),
        })

    # Gráfico de tempo
    plt.figure(figsize=(9, 5))
    plt.plot(
        TAMANHOS,
        [r["tempo_insercao"] for r in resumo],
        marker="o",
        label="Inserção",
    )
    plt.plot(
        TAMANHOS,
        [r["tempo_intercala"] for r in resumo],
        marker="o",
        label="Merge Sort",
    )
    plt.plot(
        TAMANHOS,
        [r["tempo_sorted"] for r in resumo],
        marker="o",
        label="sorted()",
    )
    plt.xlabel("Tamanho da lista")
    plt.ylabel("Tempo médio (segundos)")
    plt.title("Tempo médio dos algoritmos")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(PASTA / "grafico_tempo.png")
    plt.close()

    # Gráfico de comparações
    plt.figure(figsize=(9, 5))
    plt.plot(
        TAMANHOS,
        [r["comparacoes_insercao"] for r in resumo],
        marker="o",
        label="Inserção",
    )
    plt.plot(
        TAMANHOS,
        [r["comparacoes_intercala"] for r in resumo],
        marker="o",
        label="Merge Sort",
    )
    plt.plot(
        TAMANHOS,
        [r["comparacoes_sorted"] for r in resumo],
        marker="o",
        label="sorted()",
    )
    plt.xlabel("Tamanho da lista")
    plt.ylabel("Número médio de comparações")
    plt.title("Comparações médias")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(PASTA / "grafico_comparacoes.png")
    plt.close()

    print("\n===== RESULTADOS MÉDIOS =====")
    print(
        "n | Inserção (s) | Merge (s) | sorted (s) "
        "| Comp. Inserção | Comp. Merge | Comp. sorted"
    )

    for r in resumo:
        print(
            f'{r["n"]:4} | '
            f'{r["tempo_insercao"]:.8f} | '
            f'{r["tempo_intercala"]:.8f} | '
            f'{r["tempo_sorted"]:.8f} | '
            f'{r["comparacoes_insercao"]:.1f} | '
            f'{r["comparacoes_intercala"]:.1f} | '
            f'{r["comparacoes_sorted"]:.1f}'
        )

    # Descobre o primeiro tamanho em que Merge Sort vence a inserção.
    vencedores_tempo = [
        r["n"] for r in resumo
        if r["tempo_intercala"] < r["tempo_insercao"]
    ]

    vencedores_comp = [
        r["n"] for r in resumo
        if r["comparacoes_intercala"] < r["comparacoes_insercao"]
    ]

    print("\nPrimeiro tamanho em que Merge Sort é mais rápido:")
    print(min(vencedores_tempo) if vencedores_tempo else "Não ocorreu")

    print("Primeiro tamanho em que Merge Sort faz menos comparações:")
    print(min(vencedores_comp) if vencedores_comp else "Não ocorreu")

    print("\nArquivos criados:")
    print(arquivo_csv)
    print(PASTA / "grafico_tempo.png")
    print(PASTA / "grafico_comparacoes.png")


if __name__ == "__main__":
    main()
