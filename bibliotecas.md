# Bibliotecas

## NumPy
Numerical Python. <br>
https://numpy.org/doc/stable/index.html <br>

Uma das principais bibliotecas para processamento numérico.<br>
A maioria dos pacotes de processamento com funcionalidades científicas utiliza objetos array do NumPy.<br>
Muito utilizado para array e array multidimensional com operações aritméticas rápidas, sem uso de laços, além de muitos recursos.

### Funcionalidades

* operações rápidas em vetores para tratamento, limpeza, geração de subconjuntos, transformações e outros processamentos;
* operações para gerar ordenações, unicidade e operações de conjuntos;
* estatisticas descritivas, agregação e sintetização de dados;
* expressões lógicas condicionais na forma de expressão ao invés de usar laços com desvios;
* manipulação de dados em grupos (agregação, transformação e aplicação de funções);
* eficaz para lidar com arrays de dados muito grandes;
* adequda para trabalhar com dados homogêneos e arrays.


### ndarray
https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy-ndarray <br>

* permite realizar operações matemáticas em blocos inteiros, com sintaxe semelhante a operações realizadas com dados escalares
* todos os elementos de um ndarray são do mesmo tipo;
* por meio do atributo _shape_ é possível saber a dimensão do objeto
* e o _dtype_ permite saber o tipo de dado do array.
* principais tipos: ponto flutuante, complexo, inteiro, booleano, string e objeto
* é possível mais de duas dimensões.

## Pandas
Panel Data <br>
https://pandas.pydata.org/docs/

* Suas pricipais funções estão atreladas ao uso de dados multidimensionais.
* Uma das principais ferramentas para limpeza e análise de dados.
* Projetada para trabalhar com dados tabulares e geterogêneos.
* Estruturas fundamentais: _Series_ e _Dataframe_

### Series
* Objetos do tipo array unidimensional contendo uma sequência de valores e um array associado de rótulos (labels) de dados chamado índice.
* A representação de strings de uma Series mostra índices à esquerda e valores à direita.
* Pode-se ter rótulos nos índices.

### Dataframe
* Representa uma tabela de dados retangulares.
* Contém uma coleção ordenada de colunas, em que cada uma pode ter um tipo de valor diferente (boolenao, string, numérico, entre outros).
* Tem índice tanto para linha quanto para coluna, podendo ser imaginado como um dicionário (dict)de Series, todos compartilhando o mesmo índice.
* Capacidade de trabalhar com vários tipos de dados como se fosse uma tabela do banco de dados.

### leitura de arquivos

* **read_csv**: lê dados que utilizam vírgula como delimitador, o arquivo pode vir de um arquivo ou de um endereço URL;

* **read_excel**: lê dados tabulares de um arquivo Excel XLS ou XLSX;

* **read_html**: lê as tabelas que estão em um arquivo HTML especificado;

* **read_json**: lê dados de uma representação em string JSON.

## Scikit-Learn
https://scikit-learn.org/stable/ <br>

* Biblioteca de aprendizado máquina de código aberto que oferece suporte ao aprendizado supervisionado e não supervisionado.
* Fornece ferramentas para ajuste de modelo, pré-processamento de dados, seleção e avaliação de modelo, entre outros utilitários.
* Construída em NumPy, SciPy e Matplotlib.
* Oferece datasets que podem ser utilizados para realizar testes e aprender a utilizá-la:
    * Bosto House-Prices Dataset.
    * Breast Cancer Dataset.
    * Diabetes Dataset.
    * Digits Dataset.
    * Oris Dataset.

## MatPlotLib e Seaborn
* Fazem parte de um conjunto de bibliotecas open source paea visualização de dados. Para geração de gráficos.
* Vantagens: praticidade, visual mais bonito, diversidade de possibilidades (detalhes), configurações automáticas, entre outros.

### MatPlotLib
* É a base para grande parte de outras bibliotecas.
* É uma das mais completas.
* Muitas configurações precisam ser feitas manualmente, com linhas de programação.
* Apresenta gráficos mais crus.

### Seaborn
* É baseada na MatPlotLib.
* Conjunto de parâmetros que se autoconfiguram, para se adaptar ao conjunto de dados e muitas informações não precisam ser explicitadas, pois já estão configuradas.
