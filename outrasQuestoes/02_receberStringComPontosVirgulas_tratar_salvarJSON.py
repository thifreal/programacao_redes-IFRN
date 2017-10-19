#coding: utf-8
'''
Usuario insere produtos e preços usando ; entre eles
programa salva e monta via exemplo:
Entrada: produto1;10;produto2;654
Saida: <produto1>:R$<10>
	   <produto2>:R$<654>
Atualmente sem usar dicionários
'''
import json
entrada = input("Insira os dados no padrão csv: ")
entrada2 = entrada.split(';')
entrada3 = list()
for i in entrada2:
	if i.isdigit():
		entrada3 += '<'+i+'>@'
	else:
		entrada3 += '<'+i+'>:R$'
entrada3 = ''.join(entrada3)
entrada3 = entrada3.split('@')
entrada3.pop() #remoção forçada, alterar posteriormente
print(entrada)
print(entrada2)
print(entrada3)
arquivo = open('tst.json', 'w')
json.dump(entrada3, arquivo, indent=4)

arquivo.close()
