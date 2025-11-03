import time

n_maquinas = int(input('Quantidade de máquinas: '))

for maquina in range(n_maquinas):
    print(f'Máquina {maquina + 1} em operação')
    time.sleep(1)

print('-------')
fluxo = 1

while fluxo <= n_maquinas:
    print(f'Máquina {fluxo} em operação')
    fluxo += 1
    time.sleep(1)