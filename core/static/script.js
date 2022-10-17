// Portifólio
const seta_anterior = document.querySelector(".anterior");
const seta_proximo = document.querySelector(".proximo");
const depoimentos = document.querySelectorAll(".carrossel div.item");

let contador_item = 0;

function item_proximo () {
    contador_item++;
    
    let qnt_items = (depoimentos.length) - 1;
    if (contador_item > qnt_items) {
        contador_item = 0;
    }

    depoimentos.forEach((depoimento) => {
        depoimento.classList.replace("mostrar", "esconder")
    });
    depoimentos[contador_item].classList.replace("esconder", "mostrar");
}

function item_anterior () {
    contador_item--;

    if (contador_item < 0) {
        let qnt_items = (depoimentos.length) - 1;
        contador_item = qnt_items;
    }

    depoimentos.forEach((depoimento) => {
        depoimento.classList.replace("mostrar", "esconder")
    });
    depoimentos[contador_item].classList.replace("esconder", "mostrar");
}

seta_anterior.addEventListener('click', item_anterior);
seta_proximo.addEventListener('click', item_proximo);


// click no botão mobile
const botaoNav = document.querySelector("#botao-menu");

function mostrarMenu () {
    const menu = document.querySelector(".menu-direita");

    menu.classList.toggle("mostrar");
}

botaoNav.addEventListener('click', mostrarMenu);

document.querySelector(".navlinks").addEventListener("click", (event) => {
    if (event.target.classList.contains("navlink")) {
      document.querySelectorAll(".navlink").forEach((navlink) => {
        navlink.classList.remove("ativado");
      });
  
      event.target.classList.add("ativado");
    }
  });