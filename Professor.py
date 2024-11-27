from Pessoa import Pessoa
class Professor(Pessoa):
    def __init__(self):
        super().__init__()
        especialidade=""
        salario=0.0

    def recebeaumento(self,aumento):
        self.salario=self.salario+aumento
