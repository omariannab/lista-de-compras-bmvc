<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Lista de Compras</title>
    <link rel="stylesheet" href="/static/css/lista.css">
    <link href="https://fonts.googleapis.com/css2?family=Caveat:wght@700&family=Quicksand:wght@500;700&display=swap" rel="stylesheet">
</head>
<body data-usuario="{{usuario.usuario}}" data-dono="{{lista.dono}}">
    <div class="bloco">
        <div class="ima"></div>

        <div class="topo">
            <div class="titulo">
                <h1>{{lista.nome}}</h1>
                <div class="pessoas">
                % for pessoa in lista.participantes:
                    <span class="bolinha" title="{{pessoa}}">{{pessoa[0].upper()}}</span>
                 % end
                    <span class="bolinha mais" id="botao-mais">+</span>
                    <div class="painel" id="painel">
                        <div class="lista-participantes">
                            % for pessoa in lista.participantes:
                                <form class="linha-pessoa" action="/lista/{{lista.id}}/remover" onsubmit="return confirm('Remover {{pessoa}} da lista?')" method="post">
                                    {{pessoa}} <input type="hidden" name="usuario" value="{{pessoa}}">
                                    % if usuario.usuario == lista.dono and pessoa != lista.dono:
                                        <button type="submit" class="remover">Remover</button>
                                    % end
                                </form>
                            % end
                        </div>
                        <form action="/lista/{{lista.id}}/compartilhar" method="post">
                            <input type="text" name="usuario" placeholder="Compartilhar com..." required>
                            <button type="submit">Adicionar</button>
                        </form>
                    </div>
                </div>
                <p class="erro">{{erro}}</p>
            </div>

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
                <tr class="item comprado" data-id="{{p.id}}">
                % else:
                <tr class="item" data-id="{{p.id}}">
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

            <form class="formulario" action="/lista/{{lista.id}}/adicionar" method="post">
                <input type="text" name="nome" placeholder="Produto">
                <input type="text" name="quantidade" placeholder="Quantidade">
                <button type="submit">+ Adicionar</button>
            </form>

            <div id="progresso">
                <div id="barra"></div>
            </div>
            <p id="texto-progresso"></p>

            <div class="rodape-lista">
                <a href="/listas" class="voltar">Minhas listas</a>

                % if usuario.usuario != lista.dono:
                    <form class="sair-lista" action="/lista/{{lista.id}}/remover" onsubmit="return confirm('Sair da lista {{lista.nome}}?')" method="post">
                        <input type="hidden" name="usuario" value="{{usuario.usuario}}">
                        <button type="submit" class="excluir_lista">Sair da lista</button>
                    </form>
                % end
            </div>
            
        </div>
    </div>

    <script src="/static/js/lista.js"></script>
</body>
</html>