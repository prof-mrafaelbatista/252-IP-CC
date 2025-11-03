clubes = [
    'Vasco',
    'Flamengo',
    'Fluminense',
    'Botafogo',
    'Maricá'
]

pesquisar = input('Digite o nome do seu clube: ')

for i in range(len(clubes)):

    if pesquisar.upper() == clubes[i].upper():
        print('Achei!!!')