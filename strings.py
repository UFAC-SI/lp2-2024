str = 'Este é um texto transformado!'
tabela = str.maketrans('aeo', '130', 'x')
tabela2 = str.maketrans({'E':'3', '!':None, 'a':'@', 'o':'0'})
print(tabela)
print(tabela2)
print(str.translate(tabela))
print(str.translate(tabela2))