import sys

if len(sys.argv) < 2:
    print("\nUso: e09-10.py arquivo1 [arquivo2 arquivo3 arquivoN]\n\n\n")
    sys.exit(1)

saída = open("saida_unica.txt", "w", encoding="utf-8")
for nome in sys.argv[1:]:
    arquivo = open(nome, "r", encoding="utf-8")
    for linha in arquivo:
        saída.write(linha)
    arquivo.close()
saída.close()
