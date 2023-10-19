from Model import *
from Dao import *
import os

with open ("tarefas.txt", "a") as arquivo:
    arquivo.write("ID - Tarefa\n")

class ControllerAdicionarTarefa():
    def __init__(self, tarefa):

        try:
            if tarefa == "":
                print("Digite uma tarefa válida.")
            
            else:
            
                try:
                    self.tarefa = tarefa
                    if TODO.AdicionarTarefa(self.tarefa) == True:
                        print("Tarefa adicionada.")
                    else:
                        print("Algum problema foi encontrado.")

                except Exception:
                    print("Digite uma tarefa válida.")
        
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