import json
import uuid
from app.models.usuario import Usuario

class Auth:
    def __init__(self):
        self.caminho = "app/controllers/db/usuarios.json"
        self.logados = {}
        self.ler()

    def ler(self):
        with open(self.caminho, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        self.usuarios = []
        for d in dados:
            self.usuarios.append(Usuario(**d))

    def autenticar(self, usuario, senha):
        for u in self.usuarios:
            if u.usuario == usuario and u.senha == senha:
                codigo_user = str(uuid.uuid4())
                self.logados[codigo_user] = u
                return codigo_user
        return None

    def logado(self, codigo):
        if codigo in self.logados:
            return self.logados[codigo]
        return None

    def sair(self, codigo):
        if codigo in self.logados:
            del self.logados[codigo]

