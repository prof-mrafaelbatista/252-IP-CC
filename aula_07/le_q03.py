import time

investimento = 1000

print(f'O valor inicial do '
      f'investimneto é {investimento:.2f}')

for ano in range(3):
    print(f'Resultados do ano {ano + 1}')
    investimento = investimento * 1.05

    mensagem = f'R$ {investimento:.2f}\n'
    # Crie o arquivo invest.txt
    with open('invest.txt', 'a', encoding='utf-8') as file:
        file.write(mensagem)
        print(mensagem)

    time.sleep(2)