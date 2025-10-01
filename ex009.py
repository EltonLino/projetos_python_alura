import os
tarefas = []

def menu_principal():
    os.system('cls')
    print("Bem-vindo ao Gerenciador de Tarefas!")
    print('''
    1. Adicionar tarefa
    2. Listar tarefas
    3. Remover tarefa
    4. Sair
    ''')

def adicionar_tarefa():
    os.system('cls')
    tarefa = input("Digite a tarefa que deseja adicionar: ")
    tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")
    input("Pressione Enter para continuar...")

def listar_tarefas():
    os.system('cls')
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("Tarefas cadastradas:")
        c = 1
        for tarefa in tarefas:
            print(f"{c}. {tarefa}")
            c += 1
    input("Pressione Enter para continuar...")

def remover_tarefa():
    os.system('cls')
    if not tarefas:
        print("Nenhuma tarefa para remover.")
        input("Pressione Enter para continuar...")
        return
    listar_tarefas()
    try:
        indice = int(input("Digite o número da tarefa que deseja remover: ")) - 1
        if 0 <= indice < len(tarefas):
            tarefa_removida = tarefas.pop(indice)
            print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
    input("Pressione Enter para continuar...")

menu_principal()
resposta = input("Escolha uma opção: ") 
while resposta != '4':
    if resposta == '1':
        adicionar_tarefa()
    elif resposta == '2':
        listar_tarefas()
    elif resposta == '3':
        remover_tarefa()
    else:
        print("Opção inválida. Tente novamente.")
    
    menu_principal()
    resposta = input("Escolha uma opção: ")

print("Saindo do Gerenciador de Tarefas. Até logo!")
