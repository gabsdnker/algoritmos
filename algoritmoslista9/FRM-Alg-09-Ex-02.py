# 2
arquivo = input("Arquivo: ")

try:
    f = open(arquivo, "r")
    for i in range(10):
        print(f.readline())
    f.close()

except FileNotFoundError:
    print("Erro! Arquivo não existe")