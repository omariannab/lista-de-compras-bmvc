from app.controllers.application import Application
from bottle import Bottle, route, run, request, static_file
from bottle import redirect, template, response


app = Bottle()
ctl = Application()


#-----------------------------------------------------------------------------
# Rotas:

@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./app/static')

@app.route('/helper')
def helper(info= None):
    return ctl.render('helper')


#-----------------------------------------------------------------------------
# Suas rotas aqui:

@app.route('/lista')
def lista():
    return ctl.render('lista')

@app.route('/adicionar', method='POST')
def adicionar():
    nome = request.forms.getunicode('nome')
    quantidade = request.forms.getunicode('quantidade')
    ctl.dr.adicionar(nome, quantidade)
    redirect('/lista')

@app.route('/excluir/<id:int>', method='POST')
def excluir(id):
    ctl.dr.excluir(id)
    redirect('/lista')

@app.route('/marcar/<id:int>', method='POST')
def marcar(id):
    ctl.dr.marcar(id)
    redirect('/lista')

@app.route('/editar/<id:int>')
def pagina_editar(id):
    return ctl.editar(id)

@app.route('/editar/<id:int>', method='POST')
def salvar_editar(id):
    nome = request.forms.getunicode('nome')
    quantidade = request.forms.getunicode('quantidade')
    ctl.dr.editar(id, nome, quantidade)
    redirect('/lista')

#-----------------------------------------------------------------------------


if __name__ == '__main__':

    run(app, host='0.0.0.0', port=8080, debug=True)
