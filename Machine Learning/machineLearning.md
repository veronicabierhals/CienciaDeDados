# Machine Learning

Biblioteca utilizada: scikit-learning <br>
https://scikit-learn.org/stable/

## **Computação Tradicional e ML**

**Computação tradicional**: programadores criam programas para que os computadores possam executar. <br>

**ML**: computadores criam seus próprios procedimentos a partir da observação sobre dados e seus resultados, ou sobre a estrutura e organização de um conjunto de dados.

____

**Machine Leaning**

Capacidade de computadores:
* aprenderem a realizar uma tarefa ao invés de serem programados para tal. <br>
* criarem um modelo (induzirem a uma função ou hipótese) que aprenderam com os dados. <br>

Os algoritmos de ML aprendem a induzir uma função ou hipótese capaz de resolver um problema a partir de dados que representam instâncias do problema a ser resolvido.

Indução de uma hipótese (ou aproximação de função) a partir da experiência passada. <br>

Deve ocorrer o desenvolvimento de métricas, a partir das quais as máquinas devem ser capazes de criar hipóteses e resolvê-las. <br>

Entender, a partir dos dados de entrada, como chegou-se na resposta, para sempre que forem inseridos novos dados, obtenha-se a mesma resposta.

Principais impulsionadores:
* uso de dados como evidência e para tomada de decisão
* contexto de Big Data

Ex.: baseado no perfil, na navegação e/ou na compra de um produto em um e-commerce, o sistema é capaz de recomendar um novo produto para o cliente (com a máxima capacidade de acerto que ele também vai adquiri-lo).

Conforme Amaral (2016) ML é a aplicação de técnicas computacionais com o objetivo de encontrar padrões ocultos em dados, ou seja características que não podem ser observadas tão claramente nos dados.

**Modelo ou Modelagem** <br>
Especificação de uma relação matemática (ou probabilística) entre diferentes variáveis.

___

## **Tipos**

### **Supervisionado (preditivo)**

Normalmente preditivo, traz um objetivo estabelecido. <br>

Os métodos recebem como entrada dados rotulados e usam esses dados e seus atributos para determinar um novo conjunto de dados desconhecidos. <br>

Passam por um treinamento, na qual o classificador aprenderá um determinado padrão de acordo com os dados utilizados para treinar o sistema.

Resolve problemas de:
**Regressão**: <br>
mapeiam um exemplo em um valor real e tenta aproximá-lo desse valor criando um novo. <br>
Ex.: prever o tempo de internação de um paciente no hospital.

**Classificação**: <br>
associa a descrição de um objeto a uma classe já existente.<br>
Ex.: determina a doença de um paciente pelos seus sintomas.

### **Não supervisionado (descritivo)**
Normalmente descritivo, quando o objetivo não está bem definido e temos o intuito de compreender melhor os dados para realizar agrupamento. <br>

Agrupam-se objetos de acordo com suas características criando associação entre eles. <br>

Resolve problemas de:
**Agrupamento (clustering)**: dados agrupados de acordo com sua similaridade. <br>

**Sumarização**: busca encontrar um descrição simples e compacta para um conjunto de dados. <br>

**Associação**: encontrar padrões frequentes de associações entre os atributos de um conjunto de dados.

### **Por reforço**
Quando as saídas não estão bem definidas e as respostas só podem ser aferidas após algumas execuções.

___

## **Hierarquia**

![HierarquiaML](../Arquivos/img/hierarquiaML.png)

## **Treino e Teste**

Após os dados já terem passado pelo pré-processamento, inicia-se uma dividão dos dados para que o algotimo possa ser treinado. <br>

Geralmente divide-se o conjunto de dados em torno de 8/2, 7/3 entre treiono e teste. <br>

Dados de:
* treino: utilizados para criar o modelo (treinar). <br>
* teste: verificar se o modelo realmente atende às expectativas.

## Conceitos
### **Overfitting**
Sobreajuste <br>
Quando se ajusta um modelo muito de perto às particularidades do conjunto de treinamento e obtém um modelo que funciona bem no conjunto de treinamento, mas não é capaz de generalizar para novos dados. <br>

### **Underfitting**
Subajuste <br>
Modelo simples demais. <br>
Modelos muito simples podenm não ser capazes de capturar todos os aspectos e variabilidade dos dados, saindo-se mal, mesmo no conjunto de treinamento. <br>
No treinamento já é possível identificar que o modelo não se adapta ao conjunto de dados. <br>
Se colocar dados diferentes ele tentará aproximar ao máximo aos dados de treinamento, sem fazer reajustes. <br>

![Underfitting x Overfitting](../Arquivos/img/underfittingOverfitting.png)

### **Viés**
(bias em inglês)<br>
Capacidade de um modelo em estabelecer a relação entre as variáveis e o objeto a ser predito. <br>

### **Variância**
Sensibilidade de um modelo. <br>
Modelos muito sensíveis ao treinamento, não são capazes de acertar os resultados nos dados do teste.

![Viés e Variância](.../)

### **Regularização**
Técnica utilizada para minimizar problemas de variância. <br>
Processo de penalização nos dados, de forma a minimizar o erro de generalização do modelo sem afetar muito o modelo baseado no treinamento.

## **Predição**

Análise preditiva, ou capacidade de oprever resultados e gerar insights futuros, com base em dados do passado e do presente, com o uso de machine learning e modelagem estatística. <br>

É usada pela maiores empresas do mundo para tomar decisões nos mais variados seguimentos e está atrelada a uma diversidade de aplicações e possibilidades. <br>

Tentar prever o que irá acontecer e antecipar-se. <br>

Analisar comportamentos e as ações que foram tomadas.

### **Processos de predição**

Quando se quer prever um evento com certa precisão, é necessário conhecer o passado e entebder a situação atual.

* Extrair os fatos que estão acontecendo no momento.
* Distinguir os fatos passados daqueles que acabaram de acontecer.
* Deduzir possíveis cenários (criar hipóteses) que poderiam ocorrer.
* Classificar os cenários (modelos de ML) de acordo com a probabilidade de acontecerem.

### **Pilares de predição**

A proporção varia de um negócio para o outro.

* Conhecimento do negócio;
* equipe de ciência de dados e tecnologia;
* dados.

### **Passos para realizar a predição**

* Carregar os dados.
* Escolher um algoritimo que realize a tarefa de predição.
* Treinar o modelo.
* Visualizar o modelo.
* Testar o modelo.
* Avaliar o modelo.

### **Como escolher o algoritmo**

É importante compreender a necessidade e as características dos projetos para decidir qual melhor algoritmo a ser utilizado. <br>

Quanto mais o ciêntista de dados se apropriar dos modelos existentes maior a capacidade de decisão. <br>

A escolha depende:
* tipo de modelo - supervisionado ou não supervisionado;
* dados que serão analisados;
* hipóteses levantadas;
* será uma regressão, classificação ou agrupamento.

Começar os primeiros estudos e projetos com algum tipo de algoritmo e identificar se ele atende à necessidades. <br>

Mudanças nos atributos (dados de entrada), diferentes técnicas de regularização, mudança nos parâmetros dos algoritmos podem apresentar resultados diferentes. <br>

É importante conhecer com profundidade tudo que um algoritmo pode entregar e quais são as características que impactam diretamente nos resultados.
