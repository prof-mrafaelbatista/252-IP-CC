# Variáveis
lista_cantores = []

# Funções
def cadastrar_cantor(lcantores, nome, genero) -> list:
    # Dado organizado do cantor
    cantor = [nome, genero]
    # Adicionando cantor à lista
    lcantores.append(cantor)
    return lcantores


def listar_cantores(lcantores):
    try:

        for i in range(len(lcantores)):
            print(f'[{i+1}] - {lcantores[i][0]} - {lcantores[i][1]}')

    except Exception as e: # e de erro
        print(e)


def salvar_cantores(lcantores):
    with open("bd_cantores.txt", "a", encoding="utf-8") as arquivo:
        for i in range(len(lcantores)):
            arquivo.write(f'{lcantores[i][0]}, {lcantores[i][1]}\n')


def excluir_cantor(lcantores, indice):
    try:
        if 0 < indice <= len(lcantores):
            # Ajusta o índice para a base 0 da lista
            cantor_removido = lcantores.pop(indice - 1)
            print(f'Cantor "{cantor_removido[0]}" removido com sucesso!')
        else:
            print("Índice inválido. Nenhum cantor foi removido.")
    except Exception as e:
        print(f"Ocorreu um erro ao excluir: {e}")
    return lcantores


while True:
    print(""*50)
    print("SISTEMA DE GESTÃO DE CANTORES")
    print("" * 50)

    print('1 - Cadastrar Cantor')
    print('2 - Listar Cantores')
    print('3 - Salvar Cantores em Arquivo')
    print('4 - Carregar Cantores')
    print('5 - Alterar Cantor')
    print('6 - Excluir Cantor')
    print('0 - Sair do Sistema')

    op = int(input('Escolha a opção desejada: '))

    if op == 1:
        nome = input('Digite o nome do Cantor: ')
        genero = input('Digite o genero musical: ')
        lista_cantores = cadastrar_cantor(
            lista_cantores,
            nome,
            genero)
        print('Cadastrou um cantor')

    elif op == 2:
        listar_cantores(lista_cantores)
        print('Listou cantores')

    elif op == 3:
        salvar_cantores(lista_cantores)
        print('Salvou cantores')

    elif op == 6:
        if not lista_cantores:
            print("Não há cantores para excluir.")
        else:
            print("Qual cantor você deseja excluir?")
            listar_cantores(lista_cantores)
            try:
                indice_para_excluir = int(input("Digite o número do cantor a ser excluído: "))
                lista_cantores = excluir_cantor(lista_cantores, indice_para_excluir)
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

    elif op == 0:
        print('Saindo do Sistema')
        break
