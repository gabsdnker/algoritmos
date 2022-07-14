# 4.
import sys
i = 1
while i != (len(sys.argv)):
    arquivo = open(sys.argv[i], "r")
    while linha := arquivo.read():
        i += 1
        print(linha)
    arquivo.close()
