
def valida_entrada(mensagem, opções_válidas):
    opções = opções_válidas.lower()
    while True:
        escolha = input(mensagem)
        if escolha.lower() in opções:
            break
        print("Erro: opção inválida. Redigite.\n")
    return escolha


print(valida_entrada("Escolha uma opção:", "abcde"))
#
# Questão extra: o que acontece se o usuário digitar mais de uma opção?
# Por exemplo, ab.
