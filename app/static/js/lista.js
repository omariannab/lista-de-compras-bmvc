const linhas = document.querySelectorAll(".item");
const barra = document.getElementById("barra");
const texto = document.getElementById("texto-progresso");

function atualizarProgresso() {
    let linhas = document.querySelectorAll(".item");
    let comprados = 0;
    for (let linha of linhas) {
        if (linha.classList.contains("comprado")) {
            comprados = comprados + 1;
        }
    }

    let total = linhas.length;

    if (total === 0) {
        barra.style.width = "0%";
        texto.textContent = "Nenhum item na lista";
        return;
    }

    let porcentagem = (comprados / total) * 100;
    barra.style.width = `${porcentagem}%`;

    if (comprados === total) {
        texto.textContent = "Tudo comprado!";
    } else {
        texto.textContent = `${comprados} de ${total} itens comprados`;
    }
}

atualizarProgresso();

for (let linha of linhas) {
    linha.addEventListener("click", function () {
        let form = linha.querySelector(".form-marcar")
        form.submit();
    });
}

const botaoMais = document.getElementById("botao-mais");
const painel = document.getElementById("painel");

botaoMais.addEventListener("click", function () {
    painel.classList.toggle("aberto");
});

const lista = window.location.pathname.split('/').pop();
const endereco = 'ws://' + window.location.host + '/ws/' + lista;
const ligacao = new WebSocket(endereco);

ligacao.onmessage = function (evento) {
    const aviso = JSON.parse(evento.data);
    const linhaDoProduto = document.querySelector('tr[data-id="' + aviso.produto_id + '"]');
    if (aviso.tipo === "marcado") {   
        if (aviso.comprado === true) {
            linhaDoProduto.classList.add("comprado");
            linhaDoProduto.querySelector(".etiqueta").textContent = "comprado";
        } else {
            linhaDoProduto.classList.remove("comprado");
            linhaDoProduto.querySelector(".etiqueta").textContent = "falta";
        }
    } else if (aviso.tipo === "excluido") {
        linhaDoProduto.remove()
    } else if (aviso.tipo === "editado") {
        linhaDoProduto.querySelector(".nome").textContent = aviso.nome;
        linhaDoProduto.querySelector(".quantidade").textContent = aviso.quantidade;
    } else if (aviso.tipo === "adicionado") {
        const tabela = document.querySelector("table");
        const nova = tabela.insertRow();
        nova.className = "item";
        nova.dataset.id = aviso.produto_id;
        nova.innerHTML = `
                            <td class="nome"></td>
                            <td class="quantidade"></td>
                            <td class="situacao"><span class="etiqueta">falta</span></td>
                            <td class="acoes">
                                <form class="form-marcar" action="/marcar/${aviso.produto_id}" method="post"></form>
                                <form action="/editar/${aviso.produto_id}" method="get"><button type="submit">editar</button></form><form action="/excluir/${aviso.produto_id}" method="post"><button type="submit" class="excluir">excluir</button></form>
                            </td>
                        `;
        nova.querySelector(".nome").textContent = aviso.nome;
        nova.querySelector(".quantidade").textContent = aviso.quantidade;
        nova.addEventListener("click", function () {
            let form = nova.querySelector(".form-marcar");
            form.submit();
        });
    } else if (aviso.tipo === "compartilhado") {
        const bolinha = document.createElement("span");
        bolinha.className = "bolinha";
        bolinha.title = aviso.usuario;
        bolinha.textContent = aviso.usuario[0].toUpperCase();
        botaoMais.before(bolinha);

        const linhaPessoa = document.createElement("form");
        linhaPessoa.className = "linha-pessoa";
        linhaPessoa.action = "/lista/" + lista + "/remover";
        linhaPessoa.method = "post";
        linhaPessoa.onsubmit = function () {
            return confirm("Remover " + aviso.usuario + " da lista?");
        };

        linhaPessoa.append(aviso.usuario + " ");
        const campo = document.createElement("input");
        campo.type = "hidden";
        campo.name = "usuario";
        campo.value = aviso.usuario;
        linhaPessoa.append(campo);

        if (document.body.dataset.usuario === document.body.dataset.dono) {
            const botao = document.createElement("button");
            botao.type = "submit";
            botao.className = "remover";
            botao.textContent = "Remover";
            linhaPessoa.append(botao);
        }
        document.querySelector(".lista-participantes").append(linhaPessoa);
    } else if (aviso.tipo === "removido") {
        if (aviso.usuario === document.body.dataset.usuario) {
            window.location.href = "/listas";
            return;
        }
        
        const bolinha = document.querySelector('.bolinha[title="' + aviso.usuario + '"]');
        bolinha.remove();

        const escondido = document.querySelector('.linha-pessoa input[value="' + aviso.usuario + '"]');
        escondido.closest(".linha-pessoa").remove();
    }
    atualizarProgresso();
};
