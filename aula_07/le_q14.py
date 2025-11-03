while True:
    n1 = int(input('Digite o n1: '))
    n2 = int(input('Digite o n2: '))
    print('Digite + para somar')
    print('Digite - para subtrair')
    print('Digite * para multiplicar')
    print('Digite / para dividir')
    op = input('Digite a operação: ')

    match op:
        case '+':
            print(n1 + n2)
        case '-':
            print(n1 - n2)
        case '*':
            print(n1 * n2)
        case '/':
            print(n1 / n2)
        case _:
            print('Operador inválido!')