# **KNN (K-Nearest Neighbors)**

Também chamado de K-Vizinhos mais Próximos. <br>

Há variações de aplicações para o algoritmo na biblioteca Scikit-Learn. <br>
https://scikit-learn.org/stable/modules/neighbors.html#nearest-neighbors <br>

Pode ser utilizado para:
* **classificação** - a máquina diz a que grupo determinado registro faz parte, dentro de um contexto de negócio;
* **regressão** - fornece um número/valor, por exemplo o valor de mercado de uma determinada casa que será colocada à venda.

É um dos modelos preditivos mais semples que existem. <br>
Não possui premissas matemáticas e não requer nenhum tipo de maquinário pesado.

Requisitos:
* noção de distância;
* premissa de que pontos que estão perto um do outro são similares.

## **Funcionamento**

O KNN determina pontos para cada registro e estabelece unidades de distância entre esses pontos.

Medidas de distância utilizadas:
* Distância Euclidiana
* Distância de Hamming
* Distância de Manhattan
* Distância de Markowski

Posteriormente, para cada ponto ele calcula a distância entre os K vizinhos mais próximos. Procure sempre usar um K ímpae. E de acordo com os mais próximos ele é capaz de decidir sobre o novo ponto. <br>

![exemplo KNN](../Arquivos/img/exemploKNN.png)

