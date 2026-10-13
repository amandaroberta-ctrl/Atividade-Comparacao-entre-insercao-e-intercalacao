Comparando algoritmos de Ordenação em Dupla:

- Amanda Roberta Bandeira Santos
- Antonio Roberto da Silva Santos

Neste trabalho vamos comparar os algoritmos de ordenação por inserção (Insertion Sort) e Merge Sort, analisando o tempo de execução e a quantidade de comparações realizadas. Também foi feita uma comparação com a função sorted() da linguagem Python.

Foram utilizadas listas de números inteiros gerados aleatoriamente, com os seguintes tamanhos: 5, 10, 20, 30, 50, 75, 100, 200, 500 e 1000 elementos.
Cada tamanho foi testado 10 vezes. Os tempos apresentados correspondem à média das execuções. Também foram contabilizadas as comparações entre os valores feitas por cada algoritmo.

Resultados de tempo;

| Tamanho | Inserção (s) | Merge Sort (s) | `sorted()` (s) |
| 5 | 0.00000336 | 0.00001129 | 0.00000095 |
| 10 | 0.00000556 | 0.00001671 | 0.00000124 |
| 20 | 0.00001621 | 0.00003740 | 0.00000208 |
| 30 | 0.00006620 | 0.00006308 | 0.00000295 |
| 50 | 0.00008720 | 0.00012115 | 0.00000452 |
| 75 | 0.00020200 | 0.00018776 | 0.00000861 |
| 100 | 0.00039070 | 0.00027155 | 0.00001177 |
| 200 | 0.00177113 | 0.00060655 | 0.00002160 |
| 500 | 0.00873793 | 0.00125520 | 0.00004899 |
| 1000 | 0.03691555 | 0.00278029 | 0.00009720 |

A ordenação por inserção apresentou bons resultados nas listas pequenas. O Merge Sort foi mais rápido nos tamanhos 30, 75, 100, 200, 500 e 1000, mas não no tamanho 50. 
Mas, o primeiro tamanho em que ele foi mais rápido foi 30, sem que isso represente uma vitória contínua em todos os tamanhos seguintes.
Para listas grandes, o Merge Sort apresentou uma vantagem expressiva. No tamanho 1000, levou aproximadamente 0,00278 segundo, enquanto a inserção levou aproximadamente 0,03692 segundo.
A função `sorted()` foi a mais rápida em todos os tamanhos testados.

Resultados das comparações;

| Tamanho | Inserção | Merge Sort | `sorted()` |
| 5 | 7,9 | 7,0 | 9,2 |
| 10 | 30,7 | 22,5 | 23,2 |
| 20 | 118,5 | 64,1 | 64,7 |
| 30 | 245,4 | 110,4 | 112,9 |
| 50 | 626,7 | 220,0 | 217,6 |
| 75 | 1.429,3 | 373,8 | 373,9 |
| 100 | 2.563,9 | 544,2 | 537,0 |
| 200 | 10.224,1 | 1.283,6 | 1.270,2 |
| 500 | 62.662,9 | 3.848,2 | 3.827,7 |
| 1000 | 248.753,4 | 8.714,4 | 8.657,0 |

O Merge Sort realizou menos comparações que a inserção em todos os tamanhos analisados. A diferença aumentou conforme o tamanho das listas cresceu.
No tamanho 1000, a inserção realizou em média 248.753,4 comparações, enquanto o Merge Sort realizou 8.714,4.
Esse comportamento está relacionado à complexidade dos algoritmos: a inserção possui comportamento quadrático no caso médio e no pior caso, enquanto o Merge Sort apresenta crescimento da ordem de n log n.

Comparação com `sorted()` do Python;

A função `sorted()` foi mais rápida em todos os tamanhos testados. Ela utiliza um algoritmo de ordenação já implementado e otimizado na própria linguagem Python.
Entretanto, essa comparação não é totalmente justa para decidir qual dos dois algoritmos implementados é melhor, pois `sorted()` utiliza uma implementação diferente, otimizada e integrada à linguagem. Ela serve como referência prática de desempenho, mas não substitui a comparação direta entre inserção e Merge Sort.
O número de comparações de `sorted()` foi contado por meio de uma classe que contabiliza as operações de comparação entre os valores.

Em quais situações usar cada algoritmo?

Ordenação por inserção: é uma opção adequada para listas pequenas ou quase ordenadas, pois pode realizar poucas operações quando os elementos já estão próximos das posições corretas.

Merge Sort: é mais adequado para listas maiores, pois seu crescimento de comparações é muito menor que o da inserção conforme a quantidade de elementos aumenta.

`sorted()` do Python: é uma boa escolha em programas reais quando se deseja ordenar dados usando uma função pronta, prática e otimizada.

Conclusão(Final);

Os experimentos mostraram que não existe um único resultado de tempo que explique todos os tamanhos de listas. A inserção foi competitiva nas listas pequenas, enquanto o Merge Sort demonstrou vantagem nas listas maiores, apesar de pequenas oscilações nas medições.
Em quantidade de comparações, o Merge Sort foi melhor em todos os tamanhos testados. A função `sorted()` apresentou os menores tempos e serve como referência de uma solução pronta e otimizada.
Conclui-se que a escolha do algoritmo depende do tamanho e das características dos dados, além da finalidade do programa.
