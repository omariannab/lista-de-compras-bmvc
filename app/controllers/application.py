from bottle import template, request, redirect
from app.controllers.datarecord import DataRecord
from app.controllers.auth import Auth
from app.controllers.listarecord import ListaRecord

class Application():
    def __init__(self):
        self.dr = DataRecord()
        self.auth = Auth()
        self.lr = ListaRecord()
        self.pages = {
            'login': self.login,
            'cadastro': self.cadastro,
            'listas': self.minhas_listas
        }

    def render(self,page):
       content = self.pages.get(page, self.helper)
       return content()

    def helper(self):
        return template('app/views/html/helper')

    def lista(self, lista_id, erro=''):
        lista = self.acesso_lista(lista_id)
        usuario = self.usuario_atual()
        produtos = self.dr.produtos_da_lista(lista_id)
        return template('app/views/html/lista', produtos=produtos, usuario=usuario, lista=lista, erro=erro)

    def editar(self, produto_id):
        produto = self.acesso_produto(produto_id)
        return template('app/views/html/editar', produto=produto)

    def login(self, erro=''):
        return template('app/views/html/login', erro=erro)

    def usuario_atual(self):
        codigo = request.get_cookie('sessao')
        return self.auth.logado(codigo)

    def cadastro(self, erro=''):
        return template('app/views/html/cadastro', erro=erro)

    def minhas_listas(self):
        usuario = self.usuario_atual()
        if usuario == None:
            redirect('/login')
        minhas = self.lr.listas_do_usuario(usuario.usuario)
        return template('app/views/html/listas', listas=minhas, usuario=usuario)

    def acesso_lista(self, lista_id):
        usuario = self.usuario_atual()
        if usuario == None:
            redirect('/login')
        lista = self.lr.buscar(lista_id)
        if lista == None or usuario.usuario not in lista.participantes:
            redirect('/listas')
        return lista

    def acesso_produto(self, produto_id):
        produto = self.dr.buscar(produto_id)
        if produto == None:
            redirect('/listas')
        self.acesso_lista(produto.lista_id)
        return produto