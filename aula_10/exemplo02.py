import time
matriz = [
    [1, 2, 3], # 0
    [4, 5, 6], # 1
    [7, 8, 9], # 2
    [10, 11, 12]
]

for linha in range(len(matriz)):
    print(matriz[linha])

    for coluna in range(len(matriz[linha])):
        print(matriz[linha][coluna])
        time.sleep(1)

    time.sleep(2)