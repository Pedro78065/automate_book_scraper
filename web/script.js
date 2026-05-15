const resultado = document.getElementById("resultado");
const botao1 = document.getElementById("bt_enviar1");
const botao2 = document.getElementById("bt_enviar2");
const botao3 = document.getElementById("bt_enviar3");
const botao4 = document.getElementById("buscar");
const botao5 = document.getElementById("buscar_name");
const botao_deletar = document.getElementById("deletar");
let cacheLivros = [];

let lista_color = ["yellow", "brown", "pink", "purple", "orange"];

function trocarColor() {
    document.body.style.backgroundColor =
        lista_color[Math.floor(Math.random() * lista_color.length)];
}

setInterval(trocarColor, 2000);

// rota raiz
botao1.addEventListener("click", async () => {
    try {
        resultado.innerHTML = "carregando..."
        botao1.disabled = true
        const resposta = await fetch("http://127.0.0.1:8000");

        const dados = await resposta.json();

        resultado.innerHTML = JSON.stringify(dados)

        console.log(dados);

    } catch (erro) {
        console.log("Erro", erro);
        resultado.innerHTML = "Servidor não está no ar";
    }
    finally {
            botao1.disabled = false;
    }
});

// rota 2
botao2.addEventListener("click", async () => {
    try{
        resultado.innerHTML = "carregando..."
        botao2.disabled = true
        const resposta = await fetch("http://127.0.0.1:8000/livros/atualizar");
        let dados = await resposta.json();

        resultado.innerHTML = JSON.stringify(dados)
        console.log(dados)
        botao2.disabled = false

    } catch(erro) {
        console.log("Erro", erro);
        resultado.innerHTML = "Erro ao atualizar os dados";
    }
    finally {
        botao2.disabled = false
    }
});

// rota 3
botao3.addEventListener("click", async () => {
    try{
        resultado.innerHTML = "carregando..."
        botao3.disabled = true
        const resposta = await fetch("http://127.0.0.1:8000/livros")
        const dados = await resposta.json();

        resultado.innerHTML = "";
        cacheLivros = dados
        dados.forEach(livro => {
            const div = document.createElement("div");
            div.classList.add("livros");
            const titulo = document.createElement("h3");
            titulo.textContent = livro.Title;
            const preco = document.createElement("p");
            preco.textContent = "preço:" + " " + "€"+ livro.Price;

            div.appendChild(titulo);
            div.appendChild(preco);
            resultado.appendChild(div)
        });
        console.log(dados);

    } catch(erro) {
        console.log("Erro", erro);
        resultado.innerHTML = "Erro ao encontrar os dado(tente atualizar)";
    }
    finally {
            botao3.disabled = false

    };
});

botao4.addEventListener("click", async () => {
    try {
        resultado.innerHTML = "";

        const valor = Number(document.getElementById("filtro").value);

        const filtro = cacheLivros.filter(livros => {
            const preco = Number(livros.Price);
            return preco <= valor;
        });

        filtro.forEach(livros => {
            const div = document.createElement("div");
            div.classList.add("livros");
            
            const titulo = document.createElement("h3");
            titulo.textContent = livros.Title;

            const preco = document.createElement("p");
            preco.textContent = livros.Price;

            div.appendChild(titulo);
            div.appendChild(preco);
            resultado.appendChild(div);

        });
    } catch(e){
        console.log("Erros", e);
    };
});

botao5.addEventListener("click", async () => {
    resultado.innerHTML = "";
    const name_livro = String(document.getElementById("filtro_name").value.toLowerCase());
    const filtro = cacheLivros.filter(livros => {
        const name = String(livros.Title).toLowerCase();
        return name.includes(name_livro);
    });

    filtro.forEach(livros => {
        const div = document.createElement("div");
        div.classList.add("livros");
        const titulo = document.createElement("h3");
        titulo.textContent = livros.Title;

        const preco = document.createElement("p");
        preco.textContent = livros.Price;

        div.appendChild(titulo);
        div.appendChild(preco);
        resultado.appendChild(div);
    });
});

botao_deletar.addEventListener("click", async () => {
    try{
        const valor_delet = await fetch("http://127.0.0.1:8000/deletar");
        const dados_delet = await valor_delet.json();
        resultado.innerHTML = JSON.stringify(dados_delet);
    } catch(e){
        console.log("Erro",e);
        resultado.innerHTML = "algo deu errado!";
    };
});