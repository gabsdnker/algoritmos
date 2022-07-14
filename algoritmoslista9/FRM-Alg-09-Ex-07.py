# 7
def frequenciaLetras(arquivo):
    with open(arquivo, "r") as fonte:
        while x:=fonte.readline():
            lista_letras = []
            for letra in x:
                a = letra.lower()
                if a.isalpha() == True:
                    lista_letras.append(a)
                alfabeto = set(lista_letras)

            dicionario = {}
            n = 0
            for letra in alfabeto:
                for item in lista_letras:
                    if letra == item:
                        n += 1
                dicionario[letra] = ((n/len(lista_letras)))
                n = 0
            lista = []
            for valor in sorted(dicionario, key = dicionario.get, reverse=True):
                lista.append("{0:2}:{1:6.0%}".format(valor, dicionario[valor]))
            return lista
    
def main():
    arquivo = input("Arquivo: ")
    lista = (frequenciaLetras(arquivo))            
    for item in lista:
        print(item)
    
if __name__ == "__main__":
    main()