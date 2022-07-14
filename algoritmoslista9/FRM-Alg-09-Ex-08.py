# 8
def buscaReversa(arquivo):
    dicionario, maior = frequenciaPalavras(arquivo)
    palavrasfrequentes = {""}
    for item in dicionario:
        if dicionario[item] == maior:
            palavrasfrequentes.add(item)
    palavrasfrequentes.remove("")
    return palavrasfrequentes


def frequenciaPalavras(arquivo):
    with open(arquivo, "r") as fonte:
        dicionario = {}
        palavra = ""
        maior = 0
        while x := fonte.readline():
            for letra in x:
                a = letra.lower()
                if a.isalpha() == True:
                    palavra = palavra + a
                elif len(palavra) > 0:
                    if palavra in dicionario:
                        i = dicionario[palavra]
                        dicionario[palavra] = i + 1
                        if dicionario[palavra] > maior:
                            maior = dicionario[palavra]
                    else:
                        dicionario.update({palavra: 1})
                    palavra = ""
    fonte.close()
    return dicionario, maior


def main():
    arquivo = input("Arquivo: ")
    print(buscaReversa(arquivo))


if __name__ == "__main__":
    main()
