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

    def salvar(self):
        users = []
        for u in self.usuarios:
            users.append(vars(u))
        with open(self.caminho, "w", encoding="utf-8") as arquivo:
            json.dump(users, arquivo, indent=4, ensure_ascii=False)

    def cadastrar(self, usuario, senha, nome):
        for u in self.usuarios:
            if u.usuario == usuario:
                return False
        user = Usuario(usuario, senha, nome)
        self.usuarios.append(user)
        self.salvar()
        return True

    def existe(self, usuario):
        for u in self.usuarios:
            if u.usuario == usuario:
                return True
        return False


