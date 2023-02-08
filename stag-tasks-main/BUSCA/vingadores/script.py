import os

"""
Encontre a Joia do Espaço.

Agora você é um vingador.

“Em os Vingadores - Ultimato, Banner, Lang, Rogers e Stark viajam no tempo para Nova Iorque durante o ataque de Loki em 2012. No Sanctum Sanctorum, Banner convence a Anciã a lhe dar a Joia do Tempo, depois de prometer devolver as múltiplas Jóias aos seus devidos pontos no tempo. Na Torre Stark, Rogers recupera a Joia da Mente dos agentes adormecidos da Hidra após batalhar consigo mesmo de 2012, mas a tentativa de Stark e Lang de roubar a Joia do Espaço falha…”

O seu objetivo é encontrar quem escapou com a jo	ia e então recuperá-la, para isso você deve usar os seus poderes de programador para localizá-lo e recuperar a jóia.

Em uma estrutura de pastas/diretórios há uma pasta com o nome do vilão e dentro da mesma está um arquivo que representa a joia da espaço.

Utilize a linguagem python para desenvolver um algoritmo que percorra a pasta/diretório raiz, verifique o que é pasta/diretório ou o que é arquivo.
Lembrando que o nome do vilão está representado por uma pasta.
Após encontrar a pasta que representa o vilão, o algoritmo deverá percorrê-la e retornar o nome do arquivo o qual representa a joia do espaço.

Linguagem de programação: Python

Biblioteca: os

métodos/funções:

os.scandir() -> escaneia o diretório
is_dir() -> verifica se é diretório
is_file() -> verifica se é arquivo
name -> retorna o nome de um arquivo

Utilize laço de repetição for e estrutura de decisão if e else.
"""

"""
Etapa 1: percorrer o diretório raiz;

Etapa 2: identificar o que é diretorio e o que não é;

Etapa 3: após identificar os diretórios, percorrer o diretório com o nome Loki e retornar o nome do arquivo com o nome 'joia_do_espaco.'
"""

# o método scandir() torna um diretório em um objeto iterável, de modo que é possível percorrê-lo como se fosse uma lista.
raiz = os.scandir()

# etapa 1:  percorrendo o diretório raiz
for elemento in raiz:
    # para cada elemento no diretório raiz...
    # imprimindo o nome de cada elemento
    # print(elemento.name)
    
    # etapa 2:  identificando o que é diretório e o que não é
    # o método is_dir() retorna true quando 'identifica' um diretório
    
    # criar uma lista que receberá tudo o que for diretório
    diretorios = []
    
    # se o elemento for um diretório
    if elemento.is_dir() == True:
        
        # adicione o elemento a lista diretorios
        diretorios.append(elemento)
        
        # imprimindo a lista de diretorios
        # print(diretorios)
        
        # etapa 3:  percorrer o diretório com nome Loki e retornar o nome do arquivo com o nome da joia.
        # para isso é preciso encontrá-lo
        for diretorio in diretorios:
            # para cada diretório na lista diretórios...
            if diretorio.name == 'Loki':
                # se o nome do diretório for Loki
                # imprimir o nome do diretório
                # print(diretorio.name)
                
                # convertendo o diretório em uma lista para poder percorrê-lo
                loki = os.listdir(diretorio)
                
                # percorrendo o diretório loki e retornando o nome do arquivo
                for arquivo in loki:
                    # para cada arquivo em loki
                    # imprimir nome do arquivo
                    print(arquivo)
            
        
    
    
    