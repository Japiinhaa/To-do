from Model import *
from Dao import *
import os

class ControllerAdicionarTarefa():
    def __init__(self, tarefa):
        self.tarefa = tarefa

        try:

            if DaoAdicionarTarefa(self.tarefa) == True:
                print("Tarefa adicionada.")
            else:
                print("Algum problema foi encontrado.")

        except Exception:
            print("Digite uma tarefa válida.")


class ControllerExcluirTarefa():
    def __init__(self, excluir):
        self.excluir = excluir

        try:
            if TODO.RemoverTarefa(self.excluir) == True:
                excluir_convert = int(self.excluir)
                excluir_convert -= 1
                print("Tarefa removida.")
                    
            else:
                print("Algum problema foi encontrado.")

        except Exception as erro:
                print("Digite um número válido. Esta tarefa não existe.")

class ControllerListarTarefa():
    def __init__(self):
        tarefas = DAOListarTarefas()

        for i in range(len(tarefas)):
                print(f"{i+1} - {tarefas[i]}")