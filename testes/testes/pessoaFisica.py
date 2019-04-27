from pessoa import Pessoa

class PessoaFisica(Pessoa):
	cpf = ""

	def __init__(self, cpf, **kwargs):
		super(PessoaFisica, self).__init__(**kwargs)
		self.cpf = cpf

	def aniver(self):
		self.idade = self.idade + 1
		print("Agora: "+ str(self.idade) +" anos.")

pf = PessoaFisica(nome="Gustavo", idade=33, cpf="123.456.789-01")
print("Nome: ", pf.nome)
print("Idade: ", pf.idade)
print("Cpf: ", pf.idade)
pf.aniver()
pf.parar()