<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Lista de Compras</title>
    <link rel="stylesheet" href="/static/css/lista.css">
    <link href="https://fonts.googleapis.com/css2?family=Caveat:wght@700&family=Quicksand:wght@500;700&display=swap" rel="stylesheet">
</head>
<body>
    <div class="bloco">
        <div class="ima"></div>

        <div class="topo">
            <h1>Lista de Compras</h1>

            <div class="usuario">
                Olá, {{usuario.nome}}
                <form action="/sair" method="post">
                     <button type="submit">Sair</button>
                </form>
            </div>
        </div>

        <div class="picote"></div>

        <div class="folha">
            <table>
            % for p in produtos:
                % if p.comprado:
                <tr class="item comprado">
                % else:
                <tr class="item">
                % end
                    <td class="nome">{{p.nome}}</td>
                    <td class="quantidade">{{p.quantidade}}</td>
                    <td class="situacao">
                        % if p.comprado:
                        <span class="etiqueta">comprado</span>
                        % else:
                        <span class="etiqueta">falta</span>
                        % end
                    </td>
                    <td class="acoes">
                        <form class="form-marcar" action="/marcar/{{p.id}}" method="post">
                        </form>
                        <form action="/editar/{{p.id}}" method="get">
                            <button type="submit">editar</button>
                        </form><form action="/excluir/{{p.id}}" method="post">
                            <button type="submit" class="excluir">excluir</button>
                        </form>
                    </td>
                </tr>
            % end
            </table>

            <form class="formulario" action="/adicionar" method="post">
                <input type="text" name="nome" placeholder="Produto">
                <input type="text" name="quantidade" placeholder="Quantidade">
                <button type="submit">+ Adicionar</button>
            </form>

            <div id="progresso">
                <div id="barra"></div>
            </div>
            <p id="texto-progresso"></p>
        </div>
    </div>

    <script src="/static/js/lista.js"></script>
</body>
</html>