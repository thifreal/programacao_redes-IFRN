#coding: utf-8
#Questão 01

frase = input("Insira a frase a ser tratada: ")
c = input("Insira o caracter a ser contado:")
print(str(frase.count(c)) + ' ocorrencia(s) do caractere "' + c + '" na frase.')

#Questão 02
frase2 = input("Insira a frase a ser tratada: ")
qtdvog = sum(frase2.count(i) for i in 'aeiouAEIOU')
print(str(qtdvog) + ' vogais na frase')

#Questão 03
palavra = input("Insira a palavra a ser tratada: ")
testp = palavra[::-1]
if (palavra == testp):
    print('É palíndromo')
else:
    print('Não é palíndromo')

#Questão 04
frase3 = input("Insira a frase a ser tratada: ")
frase3 = frase3.split()
ordem = (sorted(frase3))
ordem_s = ' '.join(ordem)
print(ordem_s)

#Questão 05
nome = input("Ponha o nome completo: ")
nome = nome.split()
print(nome[-1] + ', ' + nome[0])
