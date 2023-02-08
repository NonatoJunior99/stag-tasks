# encoding=utf-8
"""
    CRUD

    C - CREATE
    R - READ
    U - UPDATE
    D - DELETE

    CRUD é um acrônimo que representa as funções básicas em um programa ou sistema onde:

    C - CREATE - Criação de um registro de uma tabela de um banco de dados.

    R - READ - Leitura deste registro

    U - UPDATE - Edição deste registro

    D - DELETE - Exclusão do registro do banco de dados.

    Vamos simular o desenvolvimento de um CRUD tendo como base de dados um arquivo do tipo .txt

    Nele os registros serão criados, lidos, atualizados e deletados. 

    Desafio:

    Escreva um texto com 10 linhas e salve no arquivo.
"""

# 1 Definindo o nome do arquivo o qual será a base de dados
db = 'database.txt'

# 2 Criando um arquivo; em python a função open() recebe dois parâmetros: o caminho ou nome do arquivo, e se neste arquivo
# serão incluídos dados ou atualizados ou excluídos.

# 3 - w -> escrevendo - C - CREATE
with open(db, 'w') as create:
    create.write('texto 1')

# 4 - r -> lendo - R - READ
with open(db, 'r') as read:
    print(read.read())

# 5 - r+ ou a -> atualizando - U - UPDATE
with open(db, 'w') as update:
    update.write('Atualização')

with open(db, 'r') as read:
    print(read.read())

# 6 - D - DELETE
with open(db, 'w+') as delete:
    delete.seek(0)

with open(db, 'r') as read:
    print(read.read())
