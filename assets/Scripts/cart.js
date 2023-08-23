let cart_img = document.querySelector(".cart-img");
let cart_container = document.querySelector(".cart-container");
let cart_btn_close = document.querySelector(".cart-btn-close");

cart_img.onclick = () => {
  cart_container.classList.toggle("active");
}

cart_btn_close.onclick = () => {
  cart_container.classList.toggle("active");
}

function ready() {
  const addToCartButtons = document.getElementsByClassName('p-buy-btn');
  for (var i = 0; i < addToCartButtons.length; i++) {
    addToCartButtons[i].addEventListener("click", addProductToCart);
  }
}

function addProductToCart(event) {
  const button = event.target;
  const productInfos = button.parentElement.parentElement.parentElement;
  const productImage = productInfos.querySelector('.p-img-front').src;
  const productTitle = productInfos.querySelector('.product-title').innerText;
  const productPrice = productInfos.querySelector('.p-price').innerText;

  let newCartProduct = document.createElement('div');
  newCartProduct.classList.add('cart-product');

  // Cria opções de tamanho
  let sizeOptions = '';
  for (let i = 34; i <= 45; i++) {
    sizeOptions += `<option value="${i}">${i}</option>`;
  }

  // Cria opções de quantidade
  let quantOptions = '';
  for (let i = 1; i <= 10; i++) {
    quantOptions += `<option value="${i}">${i}</option>`;
  }

  newCartProduct.innerHTML =
    `
    <div class="cart-item-container">
      <div class="cart-item-img">
          <img src="${productImage}" alt="${productTitle}">
      </div>
      <div class="cart-item-text">
          <span class="product-title">${productTitle}</span>
          <span class="p-price">${productPrice}</span>
          <div class="size-selector">
            <label>Tamanho:   </label>
            <select class="product-size">
              ${sizeOptions}
            </select> <!-- Fecho do select de tamanho adicionado aqui -->
            <label>Quantidade:</label>
            <select class="product-quant">
              ${quantOptions}
            </select>
          </div>
      </div>
      <button class="remove-item">Remove</button>
    </div>`;

  const cartProductsContainer = document.querySelector('.cart-products');
  cartProductsContainer.appendChild(newCartProduct);

  // Adicionar botão de remover
  let removeButton = newCartProduct.querySelector('.remove-item');
  removeButton.addEventListener("click", removeProductFromCart);
}

function removeProductFromCart(event) {
  let buttonClicked = event.target;
  buttonClicked.closest('.cart-product').remove();
}

// Call the ready function when the document is fully loaded
document.addEventListener("DOMContentLoaded", ready);


// Manipulação de comentários
document.getElementById("submitComment").addEventListener("click", function() {
  const userComment = document.getElementById("userComment").value;

  // Aqui, você pode adicionar o comentário à lista de comentários, enviá-lo ao servidor, etc.
  // Por exemplo, adicionar o comentário a um dos elementos "card-content":
  const cardContent = document.querySelector(".card-content .textfont");
  cardContent.textContent = userComment;

  // Limpar o campo de comentário após o envio
  document.getElementById("userComment").value = '';
});

// Quando o documento estiver pronto
document.addEventListener("DOMContentLoaded", () => {
  const nameInput = document.getElementById('nameInput'); // Campo de nome
  const commentInput = document.getElementById('commentInput');
  const submitCommentBtn = document.getElementById('submitComment');
  const commentList = document.querySelector('.comment-list');

  // Função para adicionar comentário
  function addComment() {
      const name = nameInput.value.trim();
      const commentText = commentInput.value.trim();

      if (name && commentText) {
          const commentDiv = document.createElement('div');
          commentDiv.classList.add('comment');
          commentDiv.innerHTML = `<strong>${name}:</strong> ${commentText}`; // Nome e comentário
          commentList.appendChild(commentDiv);
          nameInput.value = ''; // Limpar o campo de nome
          commentInput.value = ''; // Limpar o campo de entrada
      } else {
          alert("Por favor, insira seu nome e comentário."); // Mensagem de erro se os campos estiverem vazios
      }
  }

  // Adicionar evento de clique ao botão de envio
  submitCommentBtn.addEventListener("click", addComment);
});
