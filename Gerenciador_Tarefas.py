import json

#Arquivo JSON que irá armazenar as tarefas
ARQUIVO_TAREFAS = "tarefas.json"

def carregar_tarefas():
    try:
        with open(ARQUIVO_TAREFAS, "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO_TAREFAS, "w") as arquivo:
        json.dump(tarefas, arquivo, indent=4)

def adicionar_tarefas():
    titulo = input("Digite o tiítulo da tarefa: ")
    descricao = input("Digite a descrição da tarefa: ")

    nova_tarefa_criada = {"titulo": titulo, "descricao": descricao, "concluida": False}

    tarefas = carregar_tarefas()
    tarefas.append(nova_tarefa_criada)
    salvar_tarefas(tarefas)
    print("Tarefa adicionada com sucesso!")

def listar_tarefas():
    tarefas = carregar_tarefas()
    
    if(not tarefas):
        print("Nenhuma tarefa encontrada.")
        print("Sua lista de tarefas está vazia.")
        return
    
    print("\n===== Lista de Tarefas =====")

    for indice, tarefa in enumerate(tarefas):
        status = "✔ Concluída" if tarefa["concluida"] else "❌ Pendente"
        print(f"{indice}, {tarefa["titulo"]} - {status}")
        print(f"Descrição: {tarefas["descricao"]}\n")

def concluir_tarefa():
    tarefas = carregar_tarefas()
    listar_tarefas()
    try:
        indice = int(input("Digite o número da tarefa para marcar como concluída: "))

        if(1 <= indice <= len(tarefas)):
            tarefas["indice"]["concluida"] = True
            salvar_tarefas(tarefas)
            print("Tarefa marcada como concluída!")
        else:
            print("Número inválido.")
    
    except ValueError:
        print("Digite um número válido.")