n_clientes = int(input('Quantos clientes? '))

soma_notas = 0

for cliente in range(n_clientes):
    nota = int(input('Digite sua nota: '))
    # Acumulador
    soma_notas += nota
    print(f'O cliente {cliente} deu a nota {nota}')

print(f'O total das notas é: {soma_notas}')