class Pessoa:
	nome = ""
	idade = 0

	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade

	def caminhar(self):
		print("A Pessoa esta caminhando")

	def parar(self):
		print("A pessoa parou")

#p = Pessoa("Gustavo", 33)
#print("Nome: ", p.nome)
#print("idade: ", p.idade)
#p.caminhar()
#p.parar()