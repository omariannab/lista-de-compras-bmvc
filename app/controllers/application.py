from bottle import template, request, redirect
from app.controllers.datarecord import DataRecord
from app.controllers.auth import Auth

class Application():

    def __init__(self):
        self.dr = DataRecord()
        self.auth = Auth()
        self.pages = {
            'lista': self.lista,
            'login': self.login
        }

    def render(self,page):
       content = self.pages.get(page, self.helper)
       return content()

    def helper(self):
        return template('app/views/html/helper')

    def lista(self):
        usuario = self.usuario_atual()
        if usuario == None:
            redirect('/login')
        return template('app/views/html/lista', produtos=self.dr.produtos, usuario=usuario)

    def editar(self, id):
        usuario = self.usuario_atual()
        if usuario == None:
            redirect('/login')
        produto = self.dr.buscar(id)
        return template('app/views/html/editar', produto=produto)

    def login(self, erro=''):
        return template('app/views/html/login', erro=erro)

    def usuario_atual(self):
        codigo = request.get_cookie('sessao')
        return self.auth.logado(codigo)