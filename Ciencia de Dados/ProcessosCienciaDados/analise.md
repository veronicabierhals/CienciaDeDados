# Análise de Dados

## **KDD**
Knowledge Discovery in Databases <br>
Processo de descoberta de conhecimento. <br>

Processo de várias estapas para identificação de padrões compreensíveis, válidos, novos e potencialmente úteis a partir de conjunto de dados.

Demonstração na pasta *Arquivos Colab* o arquivo `kdd`

**Etapas**
* não trivial: complexidade existente na execução e manutenção dos processos;
* interativo: relevância de possuir um elemento que controle o processo;
* iterativo: possibilidade de repetições em qualquer uma das etapas do processo;
* conhecimento útil: indicação de que o objetivo foi alcançado.

### Fases

![Fases KDD](../Arquivos/img/fasesKDD.png)

#### Seleção
Selecionar um conjunto ou subconjunto de dados que farão parte da análise. <br>
Fontes de dados: planilhas, banco de dados, datawarehouse. <br>
Formatos: estruturados, semiestruturados e não-estruturados. <br>

#### Pré-Processamento
Fazer a verificação da qualidade de dados. <br>
Tratamento de dados. <br>
Excessões e ruidos são removidos. <br>
Limpeza, correção, remoção de dados inconsistentes, identificação de dados ausentes, incompletos ou não íntegros.

#### Transformação
Aplicar técnicas de transformação de dados.
Normalização, agregação, criação de novos atributos, redução e sintetização dos dados. <br>
Identificar atributos úteis nos dados para alcançar os objetivos pretendidos.

#### Mineração de dados
Aplicação de algorítmos e técnicas para identificar padrões nos dados e verificar hipóteses. <br>
Geralmente as descobertas podem ser descritivas ou preditivas, com os seguintes objetivos:
* regressão: função que faça o mapeamento dos dados;
* clusterização: identificar um conjunto finito de categorias ou clusters;
* sumarização: buscar descrição compacta para subconjunto dos dados;
* dependências ou associações: identificar dependências significativas entre as variáveis;
* divergências: identificar alterações significativas a partir do valores medidos.

#### Interpretação
Avaliar o desempenho do modelo consolidando o conhecimento descoberto.
A validação pode ser feita baseada na análise de profissionais ou em comparação com dados coletados anteriormente.

___

## **AED**
Análise Exploratória de Dados

Tem como finalidade principal examinar os dados previamente à aplicação de qualquer técnica estatística.

É comum utilizar a análise descritiva, pois permite ao cientista de dados familiarizar-se com os dados e organizá-los para responder as questões do problema a ser resolvido.

Pode ser comparada as três primeiras fases do KDD e pode ser entendida como a primeira observação sobre dados.

Para realizá-la é preciso conhecer tecnicamente o que os seu dados representam e como são classificados.

## **Quantidade de variáveis**

### **Dados unidimensionais**
Univariados
Dados no qual se tem apenas uma coleção de números (um dado apenas).
É possível ter várias informação daquele mesmo dado.

Ex: média de minutos diários gastos no Instagram
- Inicialmente é necessário computar alguma estatística, como saber o dia que gastou    mais e menos minutos, a média de minutos diários, a soma total de minutos.

### **Dados multidimensionais**
Multivariados
Vários dados que podem ou não estarem relacionados.
Em muitos casos é importante conhecer cada dimensão individualmente, mas também dispersar os dados e entender a relação entre eles, se elas existirem.

Ex: sexo, idade, peso; quantidade de minutos e quantidade de posts.


