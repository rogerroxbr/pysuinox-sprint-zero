import sys

if len(sys.argv) != 3:
    print("\nUso: e09-14.py entrada saida\n\n\n")
    sys.exit(1)

entrada = sys.argv[1]
saida = sys.argv[2]

arquivo = open(entrada, "r", encoding="utf-8")
arq_saida = open(saida, "w", encoding="utf-8")
branco = 0

for linha in arquivo:
    # Elimina espaços a direita
    # Substitua por strip se também
    # quiser eliminar espaços a esquerda
    linha = linha.rstrip()
    linha = linha.replace("  ", "")  # Elimina espaços repetidos
    if linha == "":
        branco += 1  # Conta linhas em branco
    else:
        branco = 0   # Se a linha não está em branco, zera o contador
    if branco < 2:   # Não escreve a partir da segunda linha em branco
        arq_saida.write(linha+"\n")

arquivo.close()
arq_saida.close()
