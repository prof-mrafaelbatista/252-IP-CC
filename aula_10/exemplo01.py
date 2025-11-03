vetor_jogos = [
    'Fifa 26',
    'FM26',
    'Roblox',
    'The Sims',
    'Valorant',
    'LOL',
    'Minecraft',
    'Batman'
]

qtd_letras = 0
indice = -1

for i in range(len(vetor_jogos)):
    if len(vetor_jogos[i]) > qtd_letras:
        qtd_letras = len(vetor_jogos[i])
        indice = i

print(vetor_jogos[indice])
print(f'A quantidade de caracteres é {qtd_letras}')