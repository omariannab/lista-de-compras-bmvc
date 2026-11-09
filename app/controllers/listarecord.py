import json
from app.models.lista import Lista

class ListaRecord:
    def __init__(self):
        self.caminho = "app/controllers/db/listas.json"
        self.ler()

    def ler(self):
        try:
            with open(self.caminho, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
            self.listas = []
            for d in dados:
                self.listas.append(Lista(**d))
        except FileNotFoundError:
           self.listas = []

    def salvar(self):
        dados = []
        for l in self.listas:
            dados.append(vars(l))
        with open(self.caminho, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    def criar(self, nome, dono):
        maior = 0
        for l in self.listas:
            if l.id > maior:
                maior = l.id
        novo_id = maior + 1
        nova_lista = Lista(novo_id, nome, dono,[dono])
        self.listas.append(nova_lista)
        self.salvar()

    def listas_do_usuario(self, login):
        resultado = []
        for l in self.listas:
            if login in l.participantes:
                resultado.append(l)
        return resultado

    def buscar(self, lista_id):
        for l in self.listas:
            if l.id == lista_id:
                return l
        return None

    def adicionar_participante(self, lista_id, usuario):
        lista = self.buscar(lista_id)
        lista.participantes.append(usuario)
        self.salvar()

    def remover_participante(self, lista_id, usuario):
        lista = self.buscar(lista_id)
        lista.participantes.remove(usuario)
        self.salvar()

    def excluir_lista(self, lista_id):
        restantes = []
        for l in self.listas:
            if l.id != lista_id:
                restantes.append(l)
        self.listas = restantes
        self.salvar()
