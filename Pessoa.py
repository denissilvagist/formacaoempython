class Pessoa:
    def __init__(self):
        self.nome = ""      # Atributo 'nome' do objeto
        self.idade = 0    # Atributo 'idade' do objeto
        self.sexo = ""      # Atributo 'sexo' do objeto

    def fazer_aniversario(self):
        self.idade += 1       # Incrementa a idade em 1