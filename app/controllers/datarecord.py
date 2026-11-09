import json
from app.models.produto import Produto

class DataRecord:
    def __init__(self):
        self.caminho = "app/controllers/db/produtos.json"
        self.ler()

    def ler(self):
        try:
            with open(self.caminho, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
            self.produtos = []
            for d in dados:
                self.produtos.append(Produto(**d))
        except FileNotFoundError:
            self.produtos = []

    def salvar(self):
        dados = []
        for p in self.produtos:
            dados.append(vars(p))
        with open(self.caminho, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    def adicionar(self, nome, quantidade, lista_id):
        maior = 0
        for p in self.produtos:
            if p.id > maior:
                maior = p.id
        novo_id = maior + 1
        novo_produto = Produto(novo_id, nome, quantidade, lista_id)
        self.produtos.append(novo_produto)
        self.salvar()
        return novo_produto

    def editar(self, produto_id, nome, quantidade):
        for p in self.produtos:
            if p.id == produto_id:
                p.nome = nome
                p.quantidade = quantidade
        self.salvar()

    def marcar(self, produto_id):
        for p in self.produtos:
            if p.id == produto_id:
                if p.comprado == True:
                    p.comprado = False
                else:
                    p.comprado = True
        self.salvar()

    def excluir(self, produto_id):
        restantes = []
        for p in self.produtos:
            if p.id != produto_id:
                restantes.append(p)
        self.produtos = restantes
        self.salvar()

    def buscar(self, produto_id):
        for p in self.produtos:
            if p.id == produto_id:
                return p
        return None

    def produtos_da_lista(self, lista_id):
        resultado = []
        for p in self.produtos:
            if p.lista_id == lista_id:
                resultado.append(p)
        return resultado

    def excluir_da_lista(self, lista_id): #Para poder excluir a lista
        restantes = []
        for p in self.produtos:
            if p.lista_id != lista_id:
                restantes.append(p)
        self.produtos = restantes
        self.salvar()