# 9.
def comentario(fo, de):
    with open(fo, "r") as fonte, open(de, "w") as destino:
        while t := fonte.readline(1):
            for letra in t:
                if letra != "#":
                    destino.write(letra)
        fonte.close()
        destino.close()
    return destino


def main():
    fonte = input("Fonte: ")
    destino = input("Destino: ")
    print(comentario(fonte, destino))


if __name__ == "__main__":
    main()
