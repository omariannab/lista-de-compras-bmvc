class Produto:
    def __init__(self, id, nome, quantidade, lista_id=1, comprado=False):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade
        self.lista_id = lista_id
        self.comprado = comprado
        