# Faça um algoritmo para ler: número da conta do
# cliente, saldo, débito e crédito. Após, calcular
# e escrever o saldo atual
# (saldo atual = saldo - débito + crédito).
# Também testar se saldo atual for maior ou
# igual a zero escrever a mensagem
# 'Saldo Positivo', senão escrever a mensagem
# 'Saldo Negativo'.

num_conta = 987
saldo = 45
debito = 9480
credito = 400

saldo_atual = saldo - debito + credito

if saldo_atual >= 0:
    print('Saldo positivo!')
else:
    print('Saldo negativo!')