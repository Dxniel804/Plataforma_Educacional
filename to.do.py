import os

tarefas = {}

def lean():
    print('════════════════════════════════════════════════ ♦️')

def criar_tarefa():
    print('-- Criar uma nova Tarefa --\n')
    title = input("Digite o título da tarefa: ")
    descricao = input("Digite a descrição da tarefa: ")
    tarefas[title] = descricao
    lean()
    print(f"Tarefa '{title}' criada com sucesso!")

    os.system("pause")
    os.system("cls")

def excluir_tarefa():
    print('-- Excluir uma Tarefa --\n')
    print('--> TAREFAS <--\n')
    
    for chave, valor in tarefas.items():
        print(f'Titulo: {chave}\nDescrição: {valor}')
        lean()
    print('Qual tarefa deseja EXCLUIR?')
    title = input("Digite o título da tarefa:")
    os.system('pause')
    os.system('cls')    
    if title in tarefas:
        del tarefas[title]
        print(f'Tarefa {title}, excluida com sucesso')

    os.system("pause")
    os.system("cls")

def editar_tarefa():
    print('-- Editar uma Tarefa --\n')
    visualizar_tarefa()

    os.system("pause")
    os.system("cls")

def visualizar_tarefa():
    print('-- Visualizar as Tarefas --\n')
    for chave, valor in tarefas.items():
        print(f'Titulo: {chave}\nDescrição: {valor}')
        lean()
    os.system("pause")
    os.system("cls")

def sair():
     print('SAINDO...')
     os.system('pause')
     os.system('cls')

def menu():
    while True:
        print('\nGERENCIADOR DE TAREFAS')
        lean()
        print('1 - Criar Tarefa')
        print('2 - Excluir Tarefa')
        print('3 - Editar Tarefa')
        print('4 - Visualizar Tarefa')
        print('5 - Sair')
        escolha = int(input('\n---> '))
        os.system('cls')
        
        if escolha == 1:
            criar_tarefa()

        elif escolha == 2:
            excluir_tarefa()

        elif escolha == 3:
            editar_tarefa()

        elif escolha == 4:
            visualizar_tarefa()

        elif escolha == 5:
            sair()

menu()

os.system('pause')