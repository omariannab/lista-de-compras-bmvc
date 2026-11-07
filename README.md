# Lista de Compras Compartilhada

**Nome:** Marianna Barbosa de Oliveira
**Matrícula:** 252014386

Projeto da disciplina de Orientação a Objetos (UnB), desenvolvido sobre a estrutura **BMVC** (Bottle + MVC) fornecida pelo professor.

## Sobre o projeto

Uma lista de compras compartilhada: cada pessoa tem sua conta, cria listas, adiciona produtos com quantidade, marca o que já foi comprado e pode compartilhar a lista com outras pessoas.

## Funcionalidades

### Nível 1 (BMVC I)

- Página da lista servida pelo Bottle, a partir do template `lista.tpl`.
- Tabela de produtos com nome, quantidade e situação.
- Ao clicar num produto, ele é marcado (ou desmarcado) como comprado: a linha fica riscada e a situação muda para "comprado".
- Barra de progresso e texto "X de Y itens comprados", que se atualizam a cada clique. Quando todos os itens são comprados, aparece "Tudo comprado!".

### Nível 2 (BMVC II)

- Produtos guardados em arquivo JSON (`produtos.json`), com classe `Produto` e controlador `DataRecord`.
- Adicionar, editar e excluir produtos pela página (formulários e página `editar.tpl`).

### Nível 3 (BMVC III)

- Cadastro de usuários e entrada com usuário e senha (`cadastro.tpl`, `login.tpl`), com sessão por cookie.
- Usuários guardados em `usuarios.json` (classe `Usuario`, controlador `Auth`).
- Rotas protegidas: sem usuário logado, o acesso é redirecionado para a página de entrada.
- Rotas de API para criar e excluir produtos pelo `curl` (`/api/produtos`).

### Além do enunciado: listas compartilhadas

- Página "Minhas listas" (`/listas`): mostra as listas em que a pessoa participa, com o dono e os participantes, e permite criar novas listas.
- Cada lista tem seus próprios produtos; só os participantes conseguem abrir a lista.
- Compartilhar a lista com outro usuário cadastrado (botão **+** ao lado das iniciais dos participantes).
- O dono pode remover participantes; quem não é dono pode sair da lista.
- Apenas o dono pode excluir a lista, e isso apaga também os produtos dela.
- Pedido de confirmação antes de excluir a lista, remover alguém ou sair da lista.
- Listas guardadas em `listas.json` (classe `Lista`, controlador `ListaRecord`).

## Tecnologias

- **Python** com o framework **Bottle** (servidor e rotas)
- **HTML** (templates `.tpl`)
- **CSS** (aparência)
- **JavaScript** (interação na página)
- **JSON** (armazenamento dos dados)

## Como executar

1. Instale o Bottle:
   ```
   sudo apt install python3-bottle
   ```
2. Na pasta raiz do projeto, rode:
   ```
   python3 route.py
   ```
3. Abra no navegador: **http://localhost:8080/login**

Também é possível executar com Docker:
```
docker build -t bmvci .
docker run -d -p 8080:8080 -v $(pwd):/app bmvci
```

## Arquivos do projeto

| Arquivo | Função |
|---|---|
| `route.py` | rotas da aplicação |
| `app/controllers/application.py` | controlador principal: confere usuário e permissão e escolhe a página |
| `app/controllers/auth.py` | cadastro, entrada, sessão e saída dos usuários |
| `app/controllers/listarecord.py` | leitura e gravação das listas (`listas.json`) |
| `app/controllers/datarecord.py` | leitura e gravação dos produtos (`produtos.json`) |
| `app/models/usuario.py`, `lista.py`, `produto.py` | classes dos dados |
| `app/controllers/db/*.json` | arquivos onde os dados ficam guardados |
| `app/views/html/login.tpl`, `cadastro.tpl` | páginas de entrada e cadastro |
| `app/views/html/listas.tpl` | página "Minhas listas" |
| `app/views/html/lista.tpl` | página de uma lista |
| `app/views/html/editar.tpl` | página de edição de produto |
| `app/static/css/lista.css` | o estilo das páginas |
| `app/static/js/lista.js` | a interação: marcar itens, progresso e painel de participantes |
