jQuery(document).ready(function() {
  const $ = jQuery
  console.log('checkout script loaded!')

  let cart = localStorage.getItem('leo-shop-cart')  
  if(cart) {
    cart = JSON.parse(cart)
    renderCheckoutCart($, cart)
  } else {
    // render null
  }
})

const renderCheckoutCart = ($, cart) => {
  let $itemForm = $('.product-checkout-form')
  const $cartTotal = $('#leo-checkout-total')
  let totalMoney = 0
  const $checkoutPanel = $('#leo-checkout-pannel')

  cart.map(pro => {
    let $item = $itemForm.clone(true) // true: deep clone
    $item.find('.leo-checkout-product-img').attr('src', pro.image)
    $item.find('.leo-checkout-product-name').text(pro.name)
    $item.find('.leo-checkout-qty').text(pro.quantity)
    $item.find('.leo-checkout-product-price').text(formatMoney(pro.price * pro.quantity))
    $item.css('display', 'block')
    
    $checkoutPanel.append($item)
    totalMoney += pro.price * pro.quantity
  })
  console.log(totalMoney)
  $cartTotal.find('.leo-checkout-total-money').text(formatMoney(totalMoney))
  $checkoutPanel.append($cartTotal)
}