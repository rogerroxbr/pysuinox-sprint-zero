import sqlite3
from contextlib import closing

with sqlite3.connect("precos.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        nome = input("Digite o nome do produto a alterar o preço: ")

        cursor.execute('''select * from preços
                          where nome = ?''', (nome,))

        resultado = cursor.fetchone()
        if resultado:
            print("Nome: {0:30s} Preço: {1:6.2f}".format(*resultado))
            novo_preço = input("Digite o novo preço: ")
            cursor.execute('''update preços
                              set preço = ?
                              where nome = ?''', (novo_preço, nome))
        else:
            print("Não encontrado.")
