for i in range(1000, 2001):
    if (i % 11) == 5:
        print(f'O valor é {i}')

numero = 1000
contador = 0
while numero <= 2000:
    if (numero % 11) == 5:
        print(f'O valor é {numero}')
        contador += 1
    numero += 1

print(f'No While {contador} números '
      f'são divisíveis por 11 com resto 5')