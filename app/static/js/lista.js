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
