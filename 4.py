class produto:
    def __init__(self, nome, preco):
        self.nome=nome
        self.preco=preco

class livro(produto):
    def __init__(self, nome, preco, autor):
        super().__init__(nome, preco)
        self.autor = autor

class eletronico(produto):
    def __init__(self, nome, preco, voltagem):
        super().__init__(nome, preco)
        self.voltagem = voltagem



p1 = livro('O lado feio do amor',  50.00, "Collen Houver")
print(p1.nome, p1.preco, p1.autor)