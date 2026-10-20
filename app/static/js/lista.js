const linhas = document.querySelectorAll(".item");
const barra = document.getElementById("barra");
const texto = document.getElementById("texto-progresso");

function atualizarProgresso() {
    let comprados = 0;
    for (let linha of linhas) {
        if (linha.classList.contains("comprado")) {
            comprados = comprados + 1;
        }
    }

    let total = linhas.length;
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
        linha.classList.toggle("comprado");

        let situacao = linha.children[2];
        if (linha.classList.contains("comprado")) {
            situacao.textContent = "Comprado";
        } else {
            situacao.textContent = "Falta comprar";
        }

        atualizarProgresso();
    });
}
