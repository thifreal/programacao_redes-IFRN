#Peça para o usuário digitar o nome do arquivo. Se ele existir, leia
#e conte a quantidade de palavras. Se não, exiba msg de erro
#coding: utf-8

x = input('Informe o nome de um arquivo de texto:')
total = 0
try:
    arq = open(x,'r')
    for linha in arq:
            a = linha
            b = list(a.split(' '))
            c = len(b)
            total = total + c
    print(' O arquivo contém %d palavras.'% total)
    arq.close()
except IOError:
    print("Arquivo invalido")
