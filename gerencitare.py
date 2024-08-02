import os

tarefas = {}
numer = 1

def lean():
    print('════════════════════════════════════════════════ ♦️')

def criar_tarefa():
    print('-- Criar uma nova Tarefa --\n')
    title = input("Digite o título da tarefa: ")
    descricao = input("Digite a descrição da tarefa: ")
    tarefas[title] = descricao
    print(f"Tarefa '{title}' criada com sucesso!")
    numer += 1

    os.system("pause")
    os.system("cls")

def excluir_tarefa():
    print('-- Excluir uma Tarefa --\n')
    visualizar_tarefa(tarefas)
    print('Qual tarefa deseja EXCLUIR?')
    print(tarefas)
    os.system("pause")
    os.system("cls")

def editar_tarefa():
    print('-- Editar uma Tarefa --\n')

    os.system("pause")
    os.system("cls")

def visualizar_tarefa():
    print('-- Visualizar as Tarefas --\n')

    os.system("pause")
    os.system("cls")

def menu():
    while True:
        print('\nGERENCIADOR DE TAREFAS')
        lean()
        print('1 - Criar Tarefa')
        print('2 - Excluir Tarefa')
        print('3 - Editar Tarefa')
        print('4 - Visualizar Tarefa')
        escolha = int(input('\n---> '))
        
        if escolha == 1:
            criar_tarefa()

        elif escolha == 2:
            excluir_tarefa()

        elif escolha == 3:
            editar_tarefa()

        elif escolha == 4:
            visualizar_tarefa()
        else:
            print('Opção inválida. Tente novamente.')

menu()

os.system('pause')