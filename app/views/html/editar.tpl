<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Editar produto</title>
    <link rel="stylesheet" href="/static/css/lista.css">
    <link href="https://fonts.googleapis.com/css2?family=Caveat:wght@700&family=Quicksand:wght@500;700&display=swap" rel="stylesheet">
</head>
<body>
    <div class="bloco">
        <div class="ima"></div>

        <div class="topo">
            <h1>Editar produto</h1>
        </div>

        <div class="picote"></div>

        <div class="folha">
            <form class="formulario" action="/editar/{{produto.id}}" method="post">
                <input type="text" name="nome" value="{{produto.nome}}">
                <input type="text" name="quantidade" value="{{produto.quantidade}}">
                <button type="submit">Salvar</button>
            </form>
            <a class="voltar" href="/lista">← voltar</a>
        </div>
    </div>
</body>
</html>