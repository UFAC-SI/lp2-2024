import random

with open('pares.txt', 'w') as pares:
    with open('impares.txt', 'a') as impares:
        for i in range(1,101):
            x = random.randint(1,1000)
            if x % 2 == 0:
                pares.write(f'{x}\n')
            else:
                impares.write(f'{x}\n')
