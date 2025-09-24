ouro = float(input('Digite a qtd de ouro: '))
ferro = float(input('Digite a qtd de ferro: '))
liga = ouro + ferro
perc = ferro / liga

# perc >= 0.7 and perc <= 1.0
if 0.7 <= perc <= 1.0:
    msg = f'A sua armadura terá {perc:.2f} de Ferro'

# perc > 0.0 and perc < 0.7
elif 0.0 < perc < 0.7:
    msg = f'Sem sucesso. Apenas {perc:.2f} de Ferro'

else:
    msg = 'Valores inválidos!'

print(msg)

with open('atividade12.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write(msg + '\n')
