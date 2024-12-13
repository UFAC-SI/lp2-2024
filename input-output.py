while True:
    try:
        inteiro = int(input('Digite um inteiro: '))
        try:
            real = float(input('Digite um real: '))
            break
        except ValueError as var:
            print('Digite um real válido!')
    except ValueError as vai:
        print('Digite um inteiro válido!')
print(f'{inteiro:.3f} {real:.3f}')