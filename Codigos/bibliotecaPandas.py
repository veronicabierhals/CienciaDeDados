import pandas as pd
import numpy as np

# Series

s1 = pd.Series([1, 2, -5, 0])
print(s1)

print(s1.values)

print(s1.index)

s2 = pd.Series([1, 2, -5, 0], index=['a', 'b', 'c', 'd'])
print(s2)

print(s2.index)

s2['a'] = 1000
print(s2)

# comparação
s3 = s2[s2 > 0]
print(s3)

# algebra

print(s2*2)  # não altera o array

print(s2.isnull())

# dataframe

dados = {'estado': ['SP', 'MG', 'PR', 'SP', 'MG', 'PR'], 'ano': [
    2019, 2019, 2019, 2020, 2020, 2020], 'pop': [45.9, 21.2, 16.9, 46.6, 21.4, 17.3]}

df1 = pd.DataFrame(dados)

print(df1)

# consultar partes de um dataframe

print(df1.head(2))  # ver primeiros registros

print(df1.tail(2))  # ver últimos registros

print(df1.sample(2))  # ver valores aleatórios

# gerar um novo dataframe a partir do anterior

# define as sequencias que as colunas irão aparecer
df2 = pd.DataFrame(dados, columns=['ano', 'estado', 'pop'])

print(df2)

# consultar apenas uma coluna

print(df2['estado'])
# ou
print(df2.ano)

# consultar tipos das colunas
print(df2.dtypes)

# atribuir valores/ criar novas colunas

df2['estimativa'] = 50
print(df2)

df2['estimativa'] = np.arange(6)  # valor precisa ser = tamanho da coluna
print(df2)

# criar/copiar um dataframe a partir de um já existente
df3 = df2
print(df3)

# copiar apenas uma coluna de um dataframe já existente
df3 = df2['ano']
print(df3)

# gera uma nova coluna com o resultado
df2['nao Parana'] = df2.estado != 'PR'
print(df2)

# excluir coluna
del df2['nao Parana']
print(df2)

# consultar tamanho do dataframe linha/coluna
print(df2.shape)

# contar quantas linha/registros tem o dataframe
print(df2.shape[0])

# contar quantas colunas tem o dataframe
print(df2.shape[1])

# mostra o índice
print(df2.index)

# mostra as colunas
print(df2.columns)

# conta o número de registros
print(df2.count())

# alterar informações de uma dataframe já existente

# altera nomes colunas
df2.columns = ['Ano', 'Estado', 'Populacao', 'Estimativa']
print(df2)

# analisar valores das tabelas
print(df2.describe(include='all'))

# alterar valores dos dados
df2['Ano'] = df2['Ano']+2
print(df2)

# mostrar valores que ano seja maior que 2021
print(df2[df2['Ano'] > 2021])

# gerar nova tabela a partir de uma já existente com uma condição específica
df4 = df2[df2['Ano'] > 2021]
print(df4)

# retira parte de uma tabela para pesquisa em questão, sem alterá-la
print(df4.drop('Ano', axis='columns'))

# exclui definitivamente parte de uma tabela (inplace=True)
print(df2.drop('Ano', axis='columns', inplace=True))

# retira linhas de uma tabela para pesquisa em questão, sem alterá-la
print(df2.drop([0, 1]))

# propagação na exclusão definitiva, apaga os dados da tabela em questão (cópia) e da tabela de origem
dflinhas = df2
dflinhas.drop([0, 1], inplace=True)
print(dflinhas)
print(df2)

# consultar valores de uma linha
print(df2.iloc[0])

print(df2.iloc[1:3])  # mostra posição 1 e 2

print(df2.iloc[1:3, [1, 2]])  # mostra posição 1 e 2 das colunas 1 e 2

print(df2)
