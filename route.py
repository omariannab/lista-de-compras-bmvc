from app.controllers.application import Application
from bottle import Bottle, route, run, request, static_file
from bottle import redirect, template, response
from bottle.ext.websocket import GeventWebSocketServer, websocket
import json

app = Bottle()
ctl = Application()
conexoes = []

#-----------------------------------------------------------------------------
# Rotas:

@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./app/static')

@app.route('/helper')
def helper(info= None):
    return ctl.render('helper')


#-----------------------------------------------------------------------------
# Login e cadastro:

@app.route('/login')
def pagina_login():
    return ctl.render('login')

@app.route('/login', method='POST')
def fazer_login():
    usuario = request.forms.getunicode('usuario')
    senha = request.forms.getunicode('senha')
    codigo = ctl.auth.autenticar(usuario, senha)
    if codigo != None:
        response.set_cookie('sessao', codigo, max_age=3600, httponly=True)
        redirect('/listas')
    else:
        return ctl.login('Usuário ou senha incorretos.')

@app.route('/sair', method='POST')
def fazer_logout():
    codigo = request.get_cookie('sessao')
    ctl.auth.sair(codigo)
    response.delete_cookie('sessao')
    redirect('/login')

@app.route('/cadastro')
def pagina_cadastro():
    return ctl.render('cadastro')

@app.route('/cadastro', method='POST')
def fazer_cadastro():
    usuario = request.forms.getunicode('usuario')
    senha = request.forms.getunicode('senha')
    nome = request.forms.getunicode('nome')
    cadastro = ctl.auth.cadastrar(usuario, senha, nome)
    if cadastro == True:
        redirect('/login')
    else:
        return ctl.cadastro('Nome de usuário já existe.')


#-----------------------------------------------------------------------------
# Listas:

@app.route('/listas')
def pagina_listas():
    return ctl.render('listas')

@app.route('/listas', method='POST')
def criar_lista():
    usuario = ctl.usuario_atual()
    if usuario == None:
        redirect('/login')
    nome = request.forms.getunicode('nome')
    ctl.lr.criar(nome, usuario.usuario)
    redirect('/listas')

@app.route('/lista/<lista_id:int>')
def pagina_lista(lista_id):
    return ctl.lista(lista_id)

@app.route('/lista/<lista_id:int>/compartilhar', method='POST')
def compartilhar(lista_id):
    lista = ctl.acesso_lista(lista_id)
    usuario = request.forms.getunicode('usuario')
    if not ctl.auth.existe(usuario):
        return ctl.lista(lista_id, 'Esse usuário não existe.')
    if usuario in lista.participantes:
        return ctl.lista(lista_id, 'Essa pessoa já participa.')
    ctl.lr.adicionar_participante(lista_id, usuario)
    avisar(lista_id, {"tipo":"compartilhado", "usuario": usuario})
    redirect(f'/lista/{lista_id}')

@app.route('/lista/<lista_id:int>/remover', method='POST')
def remover(lista_id):
    lista = ctl.acesso_lista(lista_id)
    logado = ctl.usuario_atual()
    usuario = request.forms.getunicode('usuario')
    if usuario == lista.dono:
        return ctl.lista(lista_id, 'O dono não pode sair da lista.')
    if logado.usuario != lista.dono and usuario != logado.usuario:
        return ctl.lista(lista_id, 'Só o dono pode remover outra pessoa.')
    if usuario not in lista.participantes:
        return ctl.lista(lista_id, 'Essa pessoa não participa.')
    ctl.lr.remover_participante(lista_id, usuario)
    avisar(lista_id, {"tipo":"removido", "usuario": usuario})
    redirect(f'/lista/{lista_id}')

@app.route('/excluir_lista/<lista_id:int>', method="POST")
def excluir_lista(lista_id):
    lista = ctl.acesso_lista(lista_id)
    usuario = ctl.usuario_atual()
    if usuario.usuario == lista.dono:
        ctl.dr.excluir_da_lista(lista_id)
        ctl.lr.excluir_lista(lista_id)
    redirect('/listas')
    


#-----------------------------------------------------------------------------
# Produtos:

@app.route('/lista/<lista_id:int>/adicionar', method='POST')
def adicionar(lista_id):
    ctl.acesso_lista(lista_id)
    nome = request.forms.getunicode('nome')
    quantidade = request.forms.getunicode('quantidade')
    p = ctl.dr.adicionar(nome, quantidade, lista_id)
    avisar(p.lista_id, {"tipo":"adicionado", "produto_id": p.id, "nome": p.nome, "quantidade": p.quantidade, "comprado": p.comprado})
    redirect(f'/lista/{lista_id}')

@app.route('/marcar/<produto_id:int>', method='POST')
def marcar(produto_id):
    produto = ctl.acesso_produto(produto_id)
    ctl.dr.marcar(produto_id)
    avisar(produto.lista_id, {"tipo":"marcado", "produto_id": produto.id, "comprado": produto.comprado})
    redirect(f'/lista/{produto.lista_id}')

@app.route('/editar/<produto_id:int>')
def pagina_editar(produto_id):
    return ctl.editar(produto_id)

@app.route('/editar/<produto_id:int>', method='POST')
def salvar_editar(produto_id):
    produto = ctl.acesso_produto(produto_id)
    nome = request.forms.getunicode('nome')
    quantidade = request.forms.getunicode('quantidade')
    ctl.dr.editar(produto_id, nome, quantidade)
    avisar(produto.lista_id, {"tipo":"editado", "produto_id": produto.id, "nome": produto.nome, "quantidade": produto.quantidade})
    redirect(f'/lista/{produto.lista_id}')

@app.route('/excluir/<produto_id:int>', method='POST')
def excluir(produto_id):
    produto = ctl.acesso_produto(produto_id)
    ctl.dr.excluir(produto_id)
    avisar(produto.lista_id, {"tipo":"excluido", "produto_id": produto.id})
    redirect(f'/lista/{produto.lista_id}')

#-----------------------------------------------------------------------------
# WebSocket:

@app.route('/ws/<lista_id:int>', apply=[websocket])
def ligacao(ws, lista_id):
    conexoes.append((lista_id, ws))
    while True:
        mensagem = ws.receive()
        if mensagem is None:
            break
    conexoes.remove((lista_id, ws))

def avisar(lista_id, aviso):
    for num, ws in conexoes:
        if num == lista_id:
            texto = json.dumps(aviso)
            ws.send(texto)


#-----------------------------------------------------------------------------
# API:

@app.route('/api/produtos', method='POST')
def api_adicionar():
    if ctl.usuario_atual() == None:
        response.status = 401
        return "Faça login primeiro\n"
    else:
        nome = request.forms.getunicode('nome')
        quantidade = request.forms.getunicode('quantidade')
        ctl.dr.adicionar(nome, quantidade)
        return f"Produto {nome} adicionado\n"

@app.route('/api/produtos/<produto_id:int>', method='DELETE')
def api_excluir(produto_id):
    if ctl.usuario_atual() == None:
        response.status = 401
        return "Faça login primeiro\n"
    else:
        produto = ctl.dr.buscar(produto_id)
        if produto == None:
            response.status = 404
            return f"Produto {produto_id} não encontrado\n"
        ctl.dr.excluir(produto_id)
        return f"Produto {produto_id} excluído\n"


#-----------------------------------------------------------------------------


if __name__ == '__main__':

    run(app, host='0.0.0.0', port=8080, server=GeventWebSocketServer, debug=True)