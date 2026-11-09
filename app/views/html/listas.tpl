<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Minhas listas</title>
    <link rel="stylesheet" href="/static/css/lista.css">
    <link href="https://fonts.googleapis.com/css2?family=Caveat:wght@700&family=Quicksand:wght@500;700&display=swap" rel="stylesheet">
</head>
<body>
    <div class="bloco">
        <div class="ima"></div>

        <div class="topo">
            <h1>Minhas listas</h1>

            <div class="usuario">
                Olá, {{usuario.nome}}
                <form action="/sair" method="post">
                    <button type="submit">Sair</button>
                </form>
            </div>
        </div>

        <div class="picote"></div>

        <div class="folha">
            % for l in listas:
            <div class="item-lista">
                <a class="info" href="/lista/{{l.id}}">
                    <div class="nome-lista">
                        <span class="titulo-lista">{{l.nome}}</span>
                        <span class="dono">Dono: {{l.dono}}</span>
                    </div>
                    <small>Participantes ({{len(l.participantes)}}): {{', '.join(l.participantes)}}</small>
                </a>

                % if l.dono == usuario.usuario:
                    <form action="/excluir_lista/{{l.id}}" onsubmit="return confirm('Excluir a lista {{l.nome}}?')" method="post">
                        <button class="excluir_lista" type="submit" class="excluir_lista">Excluir</button>
                    </form>
                % end
            </div>
            % end

            % if len(listas) == 0:
                <p class="vazio">Você ainda não tem listas.</p>
            % end

            <form class="formulario" action="/listas" method="post">
                <input type="text" name="nome" placeholder="Nome da nova lista" required>
                <button type="submit">+ Criar</button>
            </form>
        </div>
    </div>
</body>
</html>