from Aluno import Aluno 
from Pessoa import Pessoa
from Professor import Professor
from Funcionario import Funcionario
from Bolsista import Bolsista
class main:
    bolsista1=Bolsista()
    bolsista1.nome="Luan"
    bolsista1.idade=18
    bolsista1.sexo="Masculino"
    bolsista1.pagar_mensalidade()

    funcionario1=Funcionario()
    funcionario1.nome="Agileu"
    funcionario1.idade=42
    funcionario1.sexo="Masculino"
    funcionario1.setor="Limpeza"
    funcionario1.trabalhando=False
    print(funcionario1.nome)
    print(funcionario1.idade)
    print(funcionario1.sexo)
    print(funcionario1.setor)
    funcionario1.mudar_trabalho(False)
    print(funcionario1.trabalhando)
    







    professor1=Professor()
    professor1.nome="Denis"
    professor1.idade=25
    professor1.sexo="Masculino"
    professor1.especialidade="TI"
    professor1.salario=2000
    print(professor1.nome)
    print(professor1.idade)
    print(professor1.sexo)
    print(professor1.especialidade)
    print(professor1.salario)
    professor1.recebeaumento(200)
    print(professor1.salario)
    aluno1= Aluno()
    aluno2=Aluno()
    pessoa1=Pessoa()
    pessoa1.nome="João"
    print(pessoa1.nome)
    aluno1.nome="Maria"
    aluno1.idade=22
    aluno1.sexo="Feminino"
    aluno1.mat=2446
    aluno1.curso="Formação em Python"
    aluno2.nome="Luis"
    print(aluno2.nome)

    aluno1.cancelar_matricula()
    print(aluno1.nome)
    print(aluno1.idade)
    print(aluno1.sexo)
    print(aluno1.mat)