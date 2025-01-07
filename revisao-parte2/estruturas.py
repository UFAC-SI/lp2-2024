def soma_e_maior(lista):
    conjunto = set(lista)
    soma = sum(conjunto)
    maior = max(conjunto)
    return soma, maior

print(soma_e_maior([1,2,2,3,3,4,4,5]))

def contar_palavras(texto):
    dicionario1 = {}
    dicionario2 = {}
    #1ª forma com laço iterativo
    for palavra in texto.split():
        if palavra in dicionario1.keys():
            dicionario1[palavra] += 1
        else:
            dicionario1[palavra] = 1
        # 2ª forma com laço iterativo sem if e else
        dicionario2[palavra] = dicionario2.setdefault(palavra,0) + 1

    # 3ª forma com dict-comprehension
    dicionario3 = {palavra: texto.split().count(palavra) for palavra in set(texto.split())}

    return f'{dicionario1}\n{dicionario2}\n{dicionario3}'
texto = 'Teste para a contagem de palavras para a prova'
print(contar_palavras(texto))