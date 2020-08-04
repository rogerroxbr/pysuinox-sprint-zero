def valida_string(s, mín, máx):
    tamanho = len(s)
    return mín <= tamanho <= máx


print(valida_string("", 1, 5))
print(valida_string("ABC", 2, 5))
print(valida_string("ABCEFG", 3, 5))
print(valida_string("ABCEFG", 1, 10))
