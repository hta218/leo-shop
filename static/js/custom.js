jQuery(document).ready(function () {
  console.log('Custom JS loaded')
  const $ = jQuery

  initCart($)
  
  // Set up event listener
  $('.add-to-cart-btn').on('click', function () {
    console.log('add to cart clicked')
    const quantity = parseInt($('#leo-product-quantity').val()) || 1
    let product = JSON.parse($(this).attr('data-product'))
    product.quantity = quantity

    let cart = localStorage.getItem('leo-shop-cart')
    let checkout = localStorage.getItem('leo-shop-checkout')

    if (!cart) cart = []
    else cart = JSON.parse(cart)

    let foundPro = false
    cart.map(pro => {
      if (pro.id === product.id) {
        pro.quantity += quantity
        foundPro = true
      }
    })

    if (!foundPro) cart.push(product)

    localStorage.setItem('leo-shop-cart', JSON.stringify(cart))
    updateUICart($, cart)
  })

  $('#leo-shop-cart').hover(function() {
    let cart = localStorage.getItem('leo-shop-cart')  

    if(cart) {
      cart = JSON.parse(cart)
      renderHeaderCart($, cart)
    }
  })
})

const initCart = $ => {
  let cart = localStorage.getItem('leo-shop-cart')

  console.log(6969, cart)

  if (cart) {
    cart = JSON.parse(cart)
    const $cart = $('#leo-shop-cart')
    const { length } = cart
    const cartNo = length > 9 ? length : '0' + length

    $cart.find('.cart_no').text(cartNo)

  }
}

const updateUICart = ($, cart) => {
  const { length } = cart
  const cartNo = length > 9 ? length : '0' + length
  const $cart = $('#leo-shop-cart')

  $cart.find('.cart_no').text(cartNo)
}

const renderHeaderCart = ($, cart) => {
  let $itemForm = $('#leo-cart-item-form')
  const $cartTotal = $('#leo-cart-total')
  let totalMoney = 0
  const $cartList = $('#leo-cart-list-header')

  $cartList.empty()

  cart.map(pro => {
    let $item = $itemForm.clone(true) // true: deep clone
    $item.find('.leo-pro-image').attr('src', pro.image)
    $item.find('.name').text(pro.name)
    $item.find('.leo-pro-quantity').text(pro.quantity)
    $item.find('.price').text(formatMoney(pro.price * pro.quantity))
    $item.css('display', 'block')
    
    $cartList.append($item)
    totalMoney += pro.price * pro.quantity
  })

  $cartTotal.find('strong').text(formatMoney(totalMoney))
  $cartTotal.css('display', 'block')
  $cartList.append($cartTotal)
}

const formatMoney = intMoney => parseInt(intMoney).toFixed(1).replace(/\d(?=(\d{3})+\.)/g, '$&,').replace('.0', 'đ')

