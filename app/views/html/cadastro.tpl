<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Cadastrar</title>
    <link rel="stylesheet" href="/static/css/lista.css">
    <link href="https://fonts.googleapis.com/css2?family=Caveat:wght@700&family=Quicksand:wght@500;700&display=swap" rel="stylesheet">
</head>
<body>
    <div class="bloco">
        <div class="ima"></div>

        <div class="topo">
            <h1>Criar conta</h1>
        </div>

        <div class="picote"></div>

        <div class="folha">
            <form class="form-login" action="/cadastro" method="post">
                <label for="nome">Nome</label>
                <input type="text" id="nome" name="nome" required>
                <label for="usuario">Usuário</label>
                <input type="text" id="usuario" name="usuario" required>
                <label for="senha">Senha</label>
                <input type="password" id="senha" name="senha" required>
                <p class="erro">{{erro}}</p>
                <button type="submit">Cadastrar</button>
                <a href="/login" class="voltar">Voltar</a>
            </form>
        </div>
    </div>
</body>
</html>