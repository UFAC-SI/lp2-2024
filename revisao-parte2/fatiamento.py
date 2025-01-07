def maiusculos(x):
    lista = []
    for i in x:
        if i.isupper():
            loc = x.index(i)
            lista.append(x[loc:loc+1])
    return ''.join(lista)

def maiusculos2(s):
    aux = ''
    for i in s:
        if i.isupper():
            aux += i
    return aux

def maiusculos3(s):
     return s.translate(str.maketrans('','','abcdefghijlmnopqrstuwxyzév!.? '))

def embaralhar(s, indices):
    # lista = []
    # for i in indices:
    #     lista.append(s[i])
    # return ''.join(lista)
    return ''.join([s[i] for i in indices])

frase = 'Python é Divertido!'
indices = [5,0,4,3,2,1]
print(frase[1::2])

print(maiusculos3(frase))
print(embaralhar(frase, indices))