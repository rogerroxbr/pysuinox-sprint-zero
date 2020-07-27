T = [-10, -8, 0, 1, 2, 5, -2, -4]
# A escolha do primeiro elemento é arbitrária, poderia ser qualquer elemento válido
mínima = T[0]
máxima = T[0]
soma = 0
for e in T:
    if e < mínima:
        mínima = e
    if e > máxima:
        máxima = e
    soma = soma + e
print(f"Temperatura máxima: {máxima} °C")
print(f"Temperatura mínima: {mínima} °C")
print(f"Temperatura média: {soma / len(T)} °C")
