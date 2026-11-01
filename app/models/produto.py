class Produto:
    def __init__(self, id, nome, quantidade, comprado=False):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade
        self.comprado = comprado