Comparação de Algoritmos de Ordenação

Envolvidos no projeito;
- Amanda Roberta Bandeira Santos
- Antonio Roberto da Silva Santos

Este projeto compara dois algoritmos de ordenação: Insertion Sort (ordenação por inserção) e Merge Sort. Também compara seus resultados com a função `sorted()` do Python.
São analisados o tempo de execução e o número de comparações para diferentes tamanhos de listas.

- Insertion Sort: organiza os elementos inserindo cada valor na posição correta.
- Merge Sort: divide a lista em partes menores, ordena essas partes e depois as intercala.
- `sorted()`: função pronta do Python utilizada como referência de desempenho.

Foram utilizados tamanhos de lista de 5, 10, 20, 30, 50, 75, 100, 200, 500 e 1000 elementos, com 10 repetições para cada tamanho.

Principais resultados;

- O Merge Sort apresentou menos comparações que a inserção em todos os tamanhos testados.
- O Merge Sort foi mais rápido em vários tamanhos, especialmente nas listas maiores.
- A função `sorted()` apresentou o menor tempo em todos os tamanhos medidos.
- A inserção pode ser útil para listas pequenas ou quase ordenadas.

Os resultados detalhados, tabelas, gráficos e conclusões estão no arquivo `RELATORIO.md`.
