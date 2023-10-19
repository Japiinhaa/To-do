class DAOAdicionarTarefa():
    def __init__(self, idtarefa, tarefa):
        with open(self.arquivo, "a") as arquivo:
            arquivo.write(idtarefa)
            arquivo.write(" - ")
            arquivo.write(tarefa)
            arquivo.write("\n")
            print("Tarefa foi adicionada.")

class DAOListarTarefas():
        def __init__(self):
            with open("tarefas.txt", "r") as arquivo:
                linhas = arquivo.readlines()
                cont = -1
                for tarefas in linhas:
                    cont += 1
                    print(f"{cont} - {tarefas}")
            
        