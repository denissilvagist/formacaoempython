from Pessoa import Pessoa
class Funcionario(Pessoa):
    def __init__(self):
        super().__init__()
        setor =""
        trabalhando= True
    def mudar_trabalho(self,trabalhando):
        self.trabalhando=not self.trabalhando