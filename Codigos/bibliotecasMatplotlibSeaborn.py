import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# gerar X, Y de pontos

x=[1,2,3,4,5,6,7,8,9,10]
y=[1,2,3,4,2,6,7,8,9,10]

# Plotar X,Y
plt.scatter(x,y)
#plt.show()

# gerar gráfico para o valor de Y sendo o quadrado do valor de X
x1=np.arange(-100,100,1)
#print(x1)

plt.plot(x1,x1**2)
#plt.show()

# cortar o eixo X
plt.plot(x1,(x1**2)-2000)
#plt.show()

# dados fabricados
dias=np.arange(1,31)
#print(dias)

vacinados=np.random.randint(0,100,30)
contagios=np.random.randint(0,700,30)

#print(vacinados)

#plotar grafico com dados fabricados

'''
#plt.style.use('classic')
#plt.style.use('dark_background')
plt.style.use('default')

plt.figure(figsize=(10,5)) #tamanho da imagem
plt.bar(dias, vacinados) #barras
#plt.plot(dias,contagios, 'r')
plt.ylabel('Vacinados por dia')
plt.show()
'''

# criar um dataframe com os dados fabricados

dados=pd.DataFrame(dias, columns=['Dias'])

dados['Contagios']=contagios
dados['Vacinados']=vacinados

#print(dados)

#plotar grafico a partir do pandas
#dados.plot(kind='bar', x='Dias', y='Vacinados')
#plt.show()

# biblioteca Seaborn

sns.barplot(data=dados, x='Dias', y='Contagios')
#sns.barplot(data=dados, x='Dias', y='Vacinados', color='r')
sns.lineplot(data=dados, x='Dias', y='Vacinados', color='r')
plt.show()