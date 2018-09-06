import hashlib
import sys
import Art
Art.Banner()
#mude o texto em crypt = hashlib.sha1(b'exemplo'), para traduzir a criptografia

crypt = hashlib.sha1(b'hello')
new = crypt.hexdigest()
print(new)
i = 0
for x in new:
	i = i + 1
	print(x, i)
	print(end='[-]')
def arq():
	name = str(input("nome do arquivo.txt: "))
	if name != 'sair' or 'exit':
		arq = open(name, 'w')
		arq.writelines(new)
		arq.close()
		print("arquivo criado!")	
	return arq	
arq()
op = input('''
[-]Deseja Sair?
1 = Sim
2 = Não
: ''')
if op == '1':
	sys.exit('saindo...')
if op == '2':
	i = 0
	while True:
		arq()
		i = i + 1
		