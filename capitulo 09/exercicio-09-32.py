import sys
import os.path

if len(sys.argv) < 2:
    print("Digite o nome do arquivo ou diretório a verificar como parâmatro!")
    sys.exit(1)

nome = sys.argv[1]
if os.path.isdir(nome):
    print(f"O diretório {nome} existe.")
elif os.path.isfile(nome):
    print(f"O arquivo {nome} existe.")
else:
    print(f"{nome} não existe.")
