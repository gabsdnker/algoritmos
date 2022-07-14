# 10.
arquivo = input("Fonte: ")


def frequenciaLetras(arquivo):
    with open(arquivo, "r") as fonte:
        while x := fonte.readline():
            lista_letras = []
            for letra in x:
                a = letra.lower()
                if a.isalpha() == True:
                    lista_letras.append(a)
                alfabeto = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}

            dicionario = {}
            n = 0
            for letra in alfabeto:
                for item in lista_letras:
                    if letra == item:
                        n += 1
                dicionario[letra] = ((n/len(lista_letras)))
                n = 0
            lista = []
            for valor in sorted(dicionario):
                lista.append("{0:2}:{1:6.2%}".format(valor, dicionario[valor]))
            return(lista)


lista = (frequenciaLetras(arquivo))

for item in lista:
    print(item)
