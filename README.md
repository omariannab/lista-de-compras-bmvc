## Lista de Compras Compartilhada

**Nome:** Marianna Barbosa de Oliveira
**Matrícula:** 252014386

Projeto de Orientação a Objetos feito com o BMVC (Bottle + MVC). Uma lista de compras em que cada produto pode ser marcado como comprado, com uma barra mostrando o progresso.

**Como executar:** rode `python3 route.py` e abra `http://localhost:8080/login`.

## Nível 2

Os produtos agora ficam salvos no arquivo `produtos.json` e a lista tem CRUD completo pela página:

- **adicionar** produtos pelo formulário;
- **marcar** como comprado clicando na linha;
- **editar** o nome e a quantidade;
- **excluir** produtos.

## Nível 3

O sistema tem dois recursos:

- **Portal** (`/login`): página de login com usuário e senha (modelo `Usuario`, verificado pela classe `Auth`).
- **Banco** (`/lista`): lista dos produtos cadastrados. Só abre para quem fez login; quem tenta entrar sem login é levado para o portal. É aqui que fica o **READ**.

Cada produto tem os atributos `id`, `nome`, `quantidade` e `comprado` (modelo `Produto`).

Usuários para teste:

| Usuário | Senha |
|---|---|
| mari | 191 |
| isa | 108 |

### CREATE e DELETE pelo cURL

O CREATE e o DELETE são feitos pelo terminal, com o cURL, nas rotas `/api/produtos`. Essas rotas exigem login, então o primeiro passo é entrar pelo cURL e guardar o cookie da sessão.

Com o servidor rodando, em outro terminal:

**1. Login** (salva o cookie no arquivo `cookies.txt`):
```bash
curl -c cookies.txt -d "usuario=mari&senha=191" localhost:8080/login
```

**2. CREATE** (adiciona um produto):
```bash
curl -b cookies.txt -d "nome=Feijão&quantidade=2" localhost:8080/api/produtos
```
Resposta: `Produto Feijão adicionado`

**3. DELETE** (exclui o produto pelo id):
```bash
curl -b cookies.txt -X DELETE localhost:8080/api/produtos/2
```
Resposta: `Produto 2 excluído`

O `-c` salva o cookie recebido no login e o `-b` envia esse cookie nos pedidos seguintes, para o servidor saber quem está logado.

**Respostas de erro:**

| Situação | Código | Resposta |
|---|---|---|
| Pedido sem login | 401 | `Faça login primeiro` |
| Id que não existe | 404 | `Produto 999 não encontrado` |

Depois de cada comando, o resultado aparece na página `/lista` (o READ).

> Ao reiniciar o servidor, as sessões são apagadas: é preciso fazer o login pelo cURL de novo.
