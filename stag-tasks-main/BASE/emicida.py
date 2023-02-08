# encoding=utf-8

"""
    Desafio:

    No diretório base existe um arquivo main.txt e nele está registrado um texto.

    O desafio criar um algoritmo que extraia o texto deste arquivo e o tranfira para um novo arquivo com extensão .txt

    Dica: utilize as técnicas dos algoritmos anteriores para encontrar o arquivo que está no diretório data.
"""

# imports
import os

# 1. Obtendo o caminho exato da pasta em que o arquivo emicida.py está salvo
#aula muito boa https://www.youtube.com/watch?v=AvUG8wZMh_E

caminho = os.getcwd()

print(caminho)
# saída: C:\Users\m913685\Documents\repos\stag-tasks\BASE

# 2. Dentro do diretório BASE há uma pasta com o nome data na qual há um arquivo main.txt
# buscando pelo pasta data
for dirs, folders, files in os.walk(caminho):
    # se em dirs houver uma pasta com nome data, percorrer esta pasta
    # se em file existir algum com o nome de main.txt ele será salvo em uma variável de nome data
    #print(dirs)
    #print(folders)
    #print(files)
    for file in files:
        if file == 'main.txt':
            data1 = 'main.txt'
# anotacoes para que o programa leia somente as informaçoes de um arquivo ultilize .read 
# ex: email = arquivo.read
# ou readlines -- > para arquivo maiores 
#ex: with open('mensagem.txt', 'r')as arquivo:
        #mensagem = arquivo.readlines()
#para criar um novo arquivo:
    #with open('nova_senha.txt', 'w')as arquivo: 


novoCaminho = caminho + '\\data\\main.txt'
with open (novoCaminho,'r') as read:
    texto = read.read()
    print(texto)
criandoPasta = 'Novo Diretorio/'
if(not os.path.exists(criandoPasta)):
     os.mkdir(criandoPasta)
     

with open (f'{criandoPasta}\\novoTexto.txt','w') as arquivo1:
    arquivo1.write(texto)

nome = ' walcy'
sobreNome= 'Junior'

nomeCompleto = f'{nome} {sobreNome}' 