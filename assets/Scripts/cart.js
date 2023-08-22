let cart_img = document.querySelector(".cart-img")
let cart_container = document.querySelector(".cart-container")
let cart_btn_close = document.querySelector(".cart-btn-close")

cart_img.onclick = () => {
  cart_container.classList.toggle("active")
}

cart_btn_close.onclick = () => {
  cart_container.classList.toggle("active")
}