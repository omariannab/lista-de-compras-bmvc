## Lista de Compras Compartilhada

**Nome:** Marianna Barbosa de Oliveira
**Matrícula:** 252014386

Projeto de Orientação a Objetos feito com o BMVC (Bottle + MVC). Uma lista de compras em que cada produto pode ser marcado como comprado, com uma barra mostrando o progresso. Cada pessoa tem sua conta, cria suas listas e pode compartilhá-las com outras pessoas.

**Como executar:** rode `python3 route.py` e abra `http://localhost:8080/login`.

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

## Listas compartilhadas

- Cada usuário vê só as listas em que participa (`/listas`) e pode criar novas.
- Cada lista tem um dono e participantes. O dono compartilha a lista com outro usuário pelo botão **+**.
- O dono pode remover participantes; quem não é dono pode sair da lista.
- Só o dono pode excluir a lista, o que apaga também os produtos dela.
- Antes de excluir a lista, remover alguém ou sair da lista, o sistema pede confirmação.
- As listas ficam salvas em `listas.json` (modelo `Lista`).
