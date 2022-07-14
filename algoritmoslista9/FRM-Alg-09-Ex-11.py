# 11.

from curses.ascii import isalpha
import sys


def dicionario():
    dicionario = {}
    palavra = ""
    with open(sys.argv[1], "r") as palavras:
        while linhas := palavras.readline():
            for letra in linhas:
                if letra.isalpha() == True:
                    palavra = palavra + letra
                elif len(palavra) > 0:
                    dicionario.update({palavra: 0})
                    palavra = ""
        palavras.close()
    return dicionario


def corretor():
    dic = dicionario()
    erros = {""}
    palavra = ''
    with open(sys.argv[2], "r") as fonte:
        while linhas := fonte.readline():
            for letra in linhas:
                letra = letra.lower()
                if letra.isalpha() == True:
                    palavra = palavra + letra
                elif len(palavra) > 0:
                    if palavra not in dic:
                        erros.add(palavra)
                    palavra = ""
        erros.remove("")
    return erros


def main():
    try:
        print("Palavras com erro: ")
        for item in corretor():
            print(item, end="; ")
    except IndexError:
        print("Argumento inválido")


if __name__ == '__main__':
    main()
