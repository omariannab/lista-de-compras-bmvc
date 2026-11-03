## Lista de Compras Compartilhada

**Nome:** Marianna Barbosa de Oliveira
**Matrícula:** 252014386

Projeto de Orientação a Objetos feito com o BMVC (Bottle + MVC). Uma lista de compras em que cada produto pode ser marcado como comprado, com uma barra mostrando o progresso.

**Como executar:** rode `python3 route.py` e abra `http://localhost:8080/lista`.

## Nível 2

Os produtos agora ficam salvos no arquivo `produtos.json` e a lista tem CRUD completo pela página:

- **adicionar** produtos pelo formulário;
- **marcar** como comprado clicando na linha;
- **editar** o nome e a quantidade;
- **excluir** produtos.

## Nível 3

A lista agora tem login: só quem entra com usuário e senha consegue ver e mexer nos produtos. Quem tenta abrir a lista sem login é levado para a página de entrada.

Usuários para teste:

| Usuário | Senha |
|---|---|
| mari | 191 |
| isa | 108 |

Para entrar, abra `http://localhost:8080/login`.
