class Dao:
    def __init__(self):
        self.arquivo =  "Tarefas.txt"

    def AdicionarTarefa(self, tarefa):
        with open(self.arquivo, "a") as arquivo:
            arquivo.write(f"{tarefa}\n")
            return True

    def ListarTarefas(self):
            return self.lista
    
DAO = Dao()