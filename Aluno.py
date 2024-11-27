from Pessoa import Pessoa  # Importando a classe Pessoa para herança

class Aluno(Pessoa):  # A classe Aluno herda da classe Pessoa
    def __init__(self):
        super().__init__()  # Chama o construtor da classe base (Pessoa)
        self.mat = 0        # Atributo matrícula (não foi passado no construtor)
        self.curso = ""     # Atributo curso (não foi passado no construtor)

    def cancelar_matricula(self):
        print("Matrícula será cancelada")
    def pagar_mensalidade(self):
        print("o boleto de 550 foi pago")