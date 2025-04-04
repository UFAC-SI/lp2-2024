arquivo = open('teste.txt', 'a', encoding='utf-8')
arquivo.write('\nCom mais uma linha de verdade!')
for i in range(5):
    arquivo.write(f'\nLinha {i}:-> Mais uma linha.')
arquivo.close()
leitura = open('teste.txt') #Padrão é modo leitura
#conteudo = leitura.read()
#print(conteudo)
#Segunda forma de fazer leitura
linha = leitura.readline()
while linha != '':
    print(linha, end='')
    linha = leitura.readline() #Incremento do laço
print('Fim da leitura!')
leitura.close()