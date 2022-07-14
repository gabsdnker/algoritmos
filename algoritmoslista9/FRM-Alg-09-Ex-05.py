# 5.
entrada = input("Entrada: ")
saida = input("Saída: ")

indice = 0
with open(entrada, "r") as fonte, open(saida, "w") as destino:
    while t:= fonte.readline():
        indice += 1
        destino.write(f"{indice}: {t}")