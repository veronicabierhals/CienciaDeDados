import numpy as np

dados=np.random.rand(2,3)
print(dados)

# tipo de dados

print(dados.dtype)

# tamanho e quantidade

print(dados.shape)

# dimensão

print(dados.ndim)

lista=[1,2,5,7.8,1.25]
dados2=np.array(lista)
print(dados2)

lista2=[[1,2,3,4],[4,3,2,1]]
dados3=np.array(lista2)
print(dados3)

dadozero=np.zeros(10)
print(dadozero)

dadozero2=np.zeros((2,3))
print(dadozero2)

dadosum=np.ones(5)
print(dadosum)

dadosseq=np.arange(10)
print(dadosseq)

dadosseq2=np.arange(0,20,2)
print(dadosseq2)

print(dadosseq2.dtype)

dadosseqf=dadosseq.astype(np.float64)
print(dadosseqf)

print(dadosseqf.dtype)

# aritméticas com arrays

dados4=np.array([[1,2,3],[4,5,6]])
print(dados4)

print(dados4*dados4)
print(dados4-dados4)
print(1/dados4)

dados5=dados4+dados4
print(dados5)

print(dados4)

print(dados5>dados4)

# indexação

print(dadosseq)
print(dadosseq[5])

print(dadosseq[3:6])

dadosseq[3:6]=20
print(dadosseq)

fatiadados=dadosseq[2:4]
print(fatiadados)

fatiadados[1]=2000
print(fatiadados)

fatiadados[:]=333
print(dadosseq)


# copiar dados

fatia2=dadosseq[2:4].copy()
print(fatia2)

fatia2[:]=111
print(fatia2)

print(dadosseq)

# array com mais de uma dimensão

dados6=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(dados6)

print(dados6[1,2]) #linha, coluna

# máscaras
print(dadosseq)

mascara=(dadosseq<100)
print(mascara)

dadosseq[dadosseq<20]=888
print(dadosseq)

# transposição
dados7=np.arange(15).reshape((3,5))
print(dados7)

dados8=dados7.T #inverte linha e coluna
print(dados8)

# multiplicação de matrizes com dots
matrizes=np.dot(dados7.T,dados7)
print(matrizes)