<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Lista de Compras</title>
    <link rel="stylesheet" href="/static/css/lista.css">
</head>
<body>
    <h1>Lista de Compras Compartilhada</h1>

    <p>
        Organize as compras da casa de forma simples e prática.
        Adicione os produtos que estão faltando, acompanhe a lista
        e marque os itens conforme forem comprados.
    </p>

<table>
    <tr>
        <th>Produto</th>
        <th>Quantidade</th>
        <th>Situação</th>
    </tr>

    <tr class="item comprado">
      <td>Leite</td>
      <td>2 caixas</td>
      <td>Comprado</td>
    </tr>

    <tr class="item">
      <td>Detergente</td>
      <td>2 unidades</td>
      <td>Falta comprar</td>
    </tr>

</table>

<div id="progresso">
    <div id="barra"></div>
</div>
<p id="texto-progresso"></p>

<script src="/static/js/lista.js"></script>

</body>

</html>
