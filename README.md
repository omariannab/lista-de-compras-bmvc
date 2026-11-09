## Lista de Compras Compartilhada

**Nome:** Marianna Barbosa de Oliveira
**Matrícula:** 252014386

Projeto de Orientação a Objetos feito com o BMVC (Bottle + MVC). Uma lista de compras em que cada produto pode ser marcado como comprado, com uma barra mostrando o progresso. Cada pessoa tem sua conta, cria suas listas e pode compartilhá-las com outras pessoas.

## Como executar

1. Instale o Bottle: `sudo apt install python3-bottle`
2. Instale o suporte a WebSocket: `pip install --break-system-packages bottle-websocket`
3. Na pasta do projeto, rode `python3 route.py`
4. Abra `http://localhost:8080/login` no navegador

## Tecnologias

- **Python** com o **Bottle** (servidor e rotas)
- **HTML** (templates `.tpl`), **CSS** e **JavaScript**
- **JSON** (os dados ficam salvos em arquivos)
- **WebSocket** com a biblioteca **bottle-websocket** (atualização em tempo real)

## Nível 1

- Página da lista servida pelo Bottle, com tabela de produtos (nome, quantidade e situação).
- Ao clicar num produto, ele é marcado (ou desmarcado) como comprado: a linha fica riscada.
- Barra de progresso e texto "X de Y itens comprados", que se atualizam a cada clique. Quando tudo está comprado, aparece "Tudo comprado!".

## Nível 2

Os produtos ficam salvos no arquivo `produtos.json` e a lista tem CRUD completo pela página:

- **adicionar** produtos pelo formulário;
- **marcar** como comprado clicando na linha;
- **editar** o nome e a quantidade;
- **excluir** produtos.

## Nível 3

O sistema tem controle de acesso de usuários:

- **Portal** (`/login`): página de entrada com usuário e senha (modelo `Usuario`, verificado pela classe `Auth`). Também é possível se cadastrar (`/cadastro`).
- **Banco** (`/listas`): página restrita, que mostra as listas do usuário. Quem tenta entrar sem estar logado é levado para o portal.

Cada produto tem os atributos `id`, `nome`, `quantidade`, `comprado` e `lista_id` (modelo `Produto`).

Usuários para teste:

| Usuário | Senha |
|---|---|
| mari | 191 |
| isa | 108 |

### CREATE e DELETE pelo cURL

O CREATE e o DELETE são feitos pelo terminal, com o cURL, nas rotas `/api/produtos`. Essas rotas exigem usuário logado, então o primeiro passo é entrar pelo cURL e guardar o cookie da sessão.

Com o servidor rodando, em outro terminal:

**1. Entrar** (salva o cookie no arquivo `cookies.txt`):
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

O `-c` salva o cookie recebido na entrada e o `-b` envia esse cookie nos pedidos seguintes, para o servidor saber quem está logado.

**Respostas de erro:**

| Situação | Código | Resposta |
|---|---|---|
| Pedido sem usuário logado | 401 | `Faça login primeiro` |
| Id que não existe | 404 | `Produto 999 não encontrado` |

Depois de cada comando, o resultado aparece na página da lista (o READ).

## Listas compartilhadas

- Cada usuário vê só as listas em que participa (`/listas`) e pode criar novas.
- Cada lista tem um dono e participantes. O dono compartilha a lista com outro usuário pelo botão **+**, que abre a lista de participantes.
- A página da lista mostra os participantes e quantos são.
- O dono pode remover participantes; quem não é dono pode sair da lista.
- Só o dono pode excluir a lista, o que apaga também os produtos dela.
- Antes de excluir a lista, remover alguém ou sair da lista, o sistema pede confirmação.
- Só os participantes conseguem abrir uma lista; quem não participa é levado de volta para `/listas`.
- As listas ficam salvas em `listas.json` (modelo `Lista`).

## Nível 4

A página da lista é atualizada em tempo real, sem precisar recarregar. Quando uma pessoa faz uma ação, as outras pessoas que estão com a mesma lista aberta veem a mudança na hora.

Aparecem ao vivo:

- produto **adicionado**, **marcado/desmarcado**, **editado** e **excluído** (a barra de progresso também se atualiza);
- pessoa **adicionada** à lista: a bolinha dela aparece no topo e a linha dela entra na lista de participantes (o botão Remover só aparece para o dono);
- pessoa **removida** da lista: a bolinha e a linha somem; quem foi removido é levado para `/listas`.

### Como funciona

- As ações continuam sendo feitas por HTTP (formulários). O WebSocket só serve para o servidor **avisar** as outras páginas abertas.
- Cada página da lista abre uma conexão WebSocket em `/ws/<id da lista>` (`lista.js`).
- O servidor guarda as conexões abertas (`conexoes`, em `route.py`). Depois de cada ação, a função `avisar` manda um aviso em JSON só para as conexões daquela lista, por exemplo `{"tipo": "marcado", "produto_id": 3, "comprado": true}`.
- O `lista.js` recebe o aviso (`onmessage`) e, conforme o `tipo` (`adicionado`, `marcado`, `editado`, `excluido`, `compartilhado`, `removido`), altera a página.

## Organização do código

| Arquivo | Função |
|---|---|
| `route.py` | rotas da aplicação e o WebSocket (`/ws/<id da lista>` e a função `avisar`) |
| `app/controllers/application.py` | controlador principal: confere o usuário e a permissão e escolhe a página |
| `app/controllers/auth.py` | cadastro, entrada, sessão e saída dos usuários |
| `app/controllers/listarecord.py` | leitura e gravação das listas |
| `app/controllers/datarecord.py` | leitura e gravação dos produtos |
| `app/models/` | classes `Usuario`, `Lista` e `Produto` |
| `app/controllers/db/` | arquivos JSON com os dados |
| `app/views/html/` | páginas: entrada, cadastro, minhas listas, lista e edição de produto |
| `app/static/` | CSS e JavaScript (`lista.js` recebe os avisos do WebSocket) |
