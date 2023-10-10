class Dao:
    def __init__(self):
        self.arquivo =  "Tarefas.txt"

    def AdicionarTarefa(self, tarefa):
        try:
            with open(self.arquivo, "a") as arquivo:
                arquivo.write(f"{tarefa}\n")
                return True

        except Exception as erro:
            print(f"Erro ao adicionar a tarefa: {erro}")

    def ListarTarefas(self):
            return self.lista
    
DAO = Dao()