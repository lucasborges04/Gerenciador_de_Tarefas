import json

#Arquivo JSON que irá armazenar as tarefas
ARQUIVO_TAREFAS = "tarefas.json"

def ler_tarefas():
    try:
        with open(ARQUIVO_TAREFAS, "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO_TAREFAS, "w") as arquivo:
        json.dump(tarefas, arquivo, indent=4)
