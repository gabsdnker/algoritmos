# 6. 
arquivo = input("Arquivo: ")

with open(arquivo, "r") as fonte:
    maior_len = 0
    maior_palavra = ""
    palavra = ""
    lista_palavras = []
    while t:= fonte.readline():
        for letra in t:
            if letra != "\n" and letra != " ":
                palavra = palavra + letra       
                if len(palavra) > len(maior_palavra):
                    maior_palavra = palavra
                    lista_palavras.clear()
                    lista_palavras = [maior_palavra]
                    maior_len = len(maior_palavra)
                elif len(palavra) == len(maior_palavra):
                    lista_palavras.append(palavra) 
            else:        
                palavra = ""
    fonte.close()

print("Lista das palavras com maior tamanho: ",lista_palavras)
print("Maior tamanho: ",maior_len)    