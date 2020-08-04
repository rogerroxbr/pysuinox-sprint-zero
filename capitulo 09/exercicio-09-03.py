# Assume que pares e ímpares contém apenas números inteiros
# Assume que os valores em cada arquivo estão ordenados
# Os valores não precisam ser sequenciais
# Tolera linhas em branco
# Pares e ímpares podem ter número de linhas diferentes


def lê_número(arquivo):
    while True:
        número = arquivo.readline()
        # Verifica se conseguiu ler algo
        if número == "":
            return None
        # Ignora linhas em branco
        if número.strip() != "":
            return int(número)


def escreve_número(arquivo, n):
    arquivo.write(f"{n}\n")


pares = open("pares.txt", "r")
ímpares = open("ímpares.txt", "r")
pares_ímpares = open("pareseimpares.txt", "w")
npar = lê_número(pares)
nímpar = lê_número(ímpares)
while True:
    if npar is None and nímpar is None:  # Termina se ambos forem None
        break
    if npar is not None and (nímpar is None or npar <= nímpar):
        escreve_número(pares_ímpares, npar)
        npar = lê_número(pares)
    if nímpar is not None and (npar is None or nímpar <= npar):
        escreve_número(pares_ímpares, nímpar)
        nímpar = lê_número(ímpares)

pares_ímpares.close()
pares.close()
ímpares.close()
