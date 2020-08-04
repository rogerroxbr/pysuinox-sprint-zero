pares = open("pares.txt", "r")
saída = open("pares_invertido.txt", "w")

L = pares.readlines()
L.reverse()
for l in L:
    saída.write(l)

pares.close()
saída.close()

# Observe que lemos todas as linhas antes de fazer a inversão
# Esta abordagem não funciona com arquivos grandes
# Alternativa usando with:
#
# with open("pares.txt","r") as pares, open("pares_invertido.txt","w") as saída:
# L = pares.readlines()
# L.reverse()
# for l in L:
# saída.write(l)
