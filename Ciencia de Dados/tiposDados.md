# **Tipos de dados**

## **Estruturados**
Possuem formato e comprimento definidos (nomes, datas, grupos de palavras).

Conjunto de dados definidos a partir de um esquema formalmente definido.

Ex: dados armazenados em banco de dados relacionais, estrutura XML regida por um documento XSD, dados de planilhas com clareza estrutural; dados oriundos de sensorese equipamentos (desde que com uma estrutura de metadados bem definidas).

___

## **Semi-estruturados**
Estrutura implícita e flexível, geralmente um meio termo entre a estruturação e a falta total de estruturação.

Mesmo a estrutura não sendo rígida, a existência mínima de uma estrutura implícita facilita a gestão dos dados.
Ex: arquivos tabulares em planilhas (formatos TSV e CSV), arquivos XML, conteúdos Web acompanhados de tags.

___

## **Não estruturados**
Não tem estrutura definida

A extração de informações nesses conjuntos de dados torna-se complexa do ponto de vista computacional.

Ex: áudios, vídeos,  documentos em formato texto, imagens (e fotos), dados de mídias sociais, etc.

___

## **Quantidade**

### **Quantitativo ou numérico**
Valores numéricos.
Podem ser ordenados e usados em operações aritméticas.

**Continuas**: normalmente representadas por valores que podem assumir um número infinito de valores.
Geralmente resultados de medidadas (por instrumento).
Atributos que representam peso, tamanho, distância.

**Discretas**: normalmente representadas por valores que contêm um número finito ou infinito contável de valores.
Casos de atributos contáveis são valores (0/1), idade, número de peças com defeito.

**Intercalar**: valores dentro de um intervalo, sem zero absoluto.
Normalmente representado por um diagrama histograma ou poligonos de frequência.
Medidada de tendência central: média.
Ex: temperatura, datas de um calendário.

**Racional**: com zero absoluto.
Quantidade de vezes que uma pessoa foi ao hospital (o zero é parâmetro).
Medidada de tendência central: média geométrica.

___

## **Qualidade**

### **Qualitativo, simbólico ou categórico**
Pequeno, médio e grande.
Podem ter valores ordenados, mas nunca receberem operações aritméticas.

**Nominais**: valores são nomes diferentes, carregando a menor quantidade de informação possível.
Não exite relação de ordem entre seus valores.
Normalmente representado por um diagrama de barras, de linha ou de pizza.
Medidada de tendência central: moda.
Ex: CPF, RG, cor dos olhos, sexo.

**Ordinais**: os valores refletem uma ordem das categorias representadas, desta forma operadores de comparação (menor, maior) podem ser utilizados.
Normalmente representado por um diagrama boxplot.
Medidada de tendência central: mediana.
Ex: escolaridade, patente familiar, classificação no campeonato.
___

## **Escalar**
Dado único.
Representa um dado que não é um array (vetor ou matriz) ou objeto (dict).

