numero = int(input('Digite um número: '))

for i in range(1, 11):
    resultado = numero * i
    msg = f'{numero} x {i} = {resultado}'
    print(msg)

    with open('resultados.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(msg + '\n')