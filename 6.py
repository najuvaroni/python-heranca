class empregado:
    def __init__(self, nome, salario):
        self.nome=nome
        self.salario = salario

class gerente(empregado):
    def __init__(self,nome,salario, setor):

        super().__init__(nome,salario)
        self.setor = setor

g1 = gerente('Sarah', 5000, "gerente")
print(g1.nome,g1.salario)