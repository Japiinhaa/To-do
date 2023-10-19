class Dao:
    def __init__(self):
        self.arquivo =  "Tarefas.txt"

    def DAOAdicionarTarefa(self, tarefa, idtarefa):
        with open(self.arquivo, "a") as arquivo:
            arquivo.write("ID Unico - Tarefas\n")
            arquivo.write(f"{idtarefa} - {tarefa}\n")
            return True

    def DAOListarTarefas(self):
        with open(self.arquivo, "r") as arquivo:
            tarefas = arquivo.readlines()
            return tarefas
        
DAO = Dao()