# 3
arquivo = input("Arquivo: ")

try:
    f = open(arquivo, "r")
    linhas = f.readlines()
    ultimas = linhas[-10:]
    for i in ultimas:
        print(i)
    f.close()

except FileNotFoundError:
    print("Erro! Arquivo não existe")
