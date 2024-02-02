# **Pré-Processamento de Dados**

**Objetivo principal:** <br>
melhorar a qualidade dos dados e procurar eliminar elementos que podem criar um falso resultado no processamento dos dados.

**Objetivos secundários:** <br>
ajustar os dados para um uso mais adequado, modelando-o para que possa ser processado.

Normalmente vem antes da análise exploratória. <br>
Preparação dos dados para a fase de processamento. <br>
Antecede ao uso dos modelos de machine learning. <br>
É importante ter a ideia do todo do projeto . <br>
Verificar os tipos de dados que serão utilizados. <br>

Os dados podem conter ruídos, imperfeições, valores incorretos ou inconsistentes. <br>
Podem ser duplicados ou ausentes. <br>
Os atributos podem ser independentes ou correlacionados. <br>

O conjunto de dados  pode representar poucos ou muitos objetos, que podem ter uma pequena ou grande quantidade de atributos. <br>

Conjunto de objetos: conjunto de registros, tabela ou planilha. <br>

Atributos: são as variáveis, em tabelas são seus campos e em planilhas as colunas.

___

## **Integração**
Dados podem ser oriundos de diversas fontes, de diversos conjuntos de dados e em determinada situação precisam ser integrados. <br>

Deve-se atentar: atributos correspondentes, com nomes diferentes em bases distintas; informações correspondentes em bases numéricas diferentes ou moedas diferentes. <br>

É necessário compreender quais são os atributos necessários de cada objeto. <br>

Elevado número de atributos pode comprometer o desempenho dos algoritmos de machine learning.

## **Eliminação manual de atributos**

* Atributos:
    * iguais em diferentes bases.
    * que contém o mesmo valor para todos os objetos (ex: atributo cidade, se está analisando dados de uma mesma cidade).
* Anonimização de uma base (retirar os nomes das pessoas).
* Análises preditivas: atributo que não contribui para a estimativa de um valor.

___

## **Amostragem de dados**
Muitos algoritmos de ML tem dificuldades em lidar com um números grandes de objetos, levando à saturação de memória e necessidade de ampliar a escala horizontal da estrutura física. <br>

Quanto mais dados são utilizados, mmelhor tende a ser o modelo e menor a eficiência computacional. <br>

**Amostra progressiva:** começa com uma precisão continua a melhorar, até atingir um ponto que não há mais evolução

___

## **Dados desbalanceados**
Momentos em que dados de um subconjunto de uma determinada classe aparecem cokm frequência maior que nas outras clases. <br>

O desbalanceamento afeta o desempenho de alguns algoritmos de machine learning, de forma que favoreçam a classificação da classe marjoritária. <br>

Técnicas:
* redefinição do tamanho do conjunto de dados;
* utilizar diferentes custos de classificação;
* indução de um modelo para uma classe;
* classificação com apenas uma classe;
* treinar dados separadamente por classe.

___

## **Qualidade dos dados**

Dados que impactam negativamente os resultados de uma análise:
* ruidosos: possuem erros ou valores que são diferentes do esperado;
* inconsistentes: não combinam ou contradizem valores de outros do mesmo objeto;
* redundantes: atributos com valores repetidos no mesmo objeto;
* incompletos: com ausência de valores para parte dos dados.

As deficiências podem ser causadas:
* por problemas nos equipamentos que coletam os dados;
* na transmissão ou armazenamento;
* no preenchimento manual;
* processos de integração.

_____

### **Dados incompletos**

Causas da ausência de valores em atributos:
* não foi considerado importante (ou não era obrigatório) quando os dados foram coletados;
* desconhecimento do valor do atributo no preenchimento dos valores do objeto;
* distração no preenchimento;
* inexistência do valor para o atributo em alguns registros;
* problema com equipamento utilizado na coleta.

Técnicas:
* eliminar objetos com valores ausentes: essa alternativa normalmente é descartada quando poucos atributos do objeto têm valores ausentes;
* definir e preencher manualmente os valores para atributos com valores ausentes;
* usar métodos ou heurística para automaticamente definir valores para atributos com valores ausentes.
    * é importante definir um valor onde saiba-se que era um valor ausente anteriormente;
    * utilizar média, moda ou mediana dos valores conhecidos;
    * definir um indutor baseado em outros atributos.
___

### **Dados inconsistentes**

Dados que possuem valores conflitantes em seus atributos. <br>
Uso de escalas diferentes para a mesma medida. <br>

Quando relações entre atributos são claramente conhecidas (valores correlacionados direa ou indiretamente).
___

### **Dados redundantes**

Objeto muito semelhante a outro no mesmo conjunto de dados. <br>

Quando pode ser deduzido a partir do valor de um ou mais atributos. Dois ou mais atributos estão correlacionados quando apresentam um perfil de variação semelhante para os diferentes objetos. <br>

Pode criar a falsa sensação de que um perfil de objeto é mais importante que os demais, induzindo o modelo de análise. <br>

**Eliminar as redundâncias:**
* eliminação dos objetos semelhantes;
* combinação dos valores dos atributos dos objetos semelhantes.

### **Dados com ruídos**

Contêm objetos que, aparentemente, não pertencem a distribuição que gerou os dados analisados. <br>

Variância ou erro aleatório no valor gerado de um atributo. <br>

Um indicador de presença de ruído é a existência de outliers.
Valores que estão além dos limites aceitáveis ou são muito diferentes dos demais valores observados para o esmo atributo. <br>

**Técnicas para detecção e remoção de ruídos**

Encestamento: suavisam o valor de um atributo. Primeiro os valores são ordenados, depois são divididos em faixas, e eses valores são substituídos por uma média ou mediana. <br>

Agrupamento: valores que não formarem grupos são considerados ruidosos ou outliers. <br>

Regressão ou classificação: procuram determinar um valor verdadeiro para um outlier.

## **Tranformação de dados**

Várias técnicas de machine learning estão limitadas à manipulação de valores em determinados tipos, alguns algoritmos estão restritos a valores numéricos, outros a valores qualitativos. <br>

Em várias situações, a depender do modelo de machine learning utilizado, será necessário converter dados qualitativos a numéricos ou vice-versa. <br>

Valores qualitativos nominais ou ordinais podem ser tratados de forma diferente. <br>

Ex.: Redes Neurais Artificiais e Support Vector Machines lidam apenas com valores numéricos.

Situações em que é necessária transformação de valor numérico para outro valor numérico, para evitar que um atributo predomine sobre o outro:
* limites inferior e superior de valores dos atributos são muito diferentes;
* vários atributos estão em escalas diferentes.
* normalização por amplitude -> redefinindo uma nova escala de valores com limites máximo e mínimo;
* padronização -> definição de valor central e um valor de espelhamento para todos os atributos.

### **Redução da dimensionalidade**

Tamanho horizontal do seu objeto, ou seja, a quantidade de atributos que um determinado objeto tem. <br>

Exs.: em análise de imagens cada pixel representa um atributo; nos estudos de genética os dados dos gener apresentam milhares de atributos. <br>

Grandes quantidades de atributos inviabilizam o processo. <br>

**Redução de atributos**
* melhora o desempenho;
* reduz o curso operacional;
* torna os resultados masi compreensíveis.

**Técnicas utilizadas**
* **Agregação**: substituem atributo originais por novos atributos formados pela combinação de grupos.
    * Técnica mais conhecida: Análise de Componentes Principais (PCA).
        * descorrelaciona estatisticamente os exemplos, reduzindo a dimensionalidade do conjunto de dados original pela eliminação das redundâncias.
        * Áreas como biologia, finanças e medicina evitam agregar atributos, pois consideram os dados originais importantes para o processo de interpretação dos resultados.

* **Seleção de atributos**: mantêm uma parte dos atributos originais e descartam os demais atributos.
    * Técnicas automáticas para avaliar qualidade ou desempenho de um subconjunto de atributos:
        * abordagem embutida;
        * abordagem baseada em filtro;
        * wrapper.


