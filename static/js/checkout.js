jQuery(document).ready(function () {
  const $ = jQuery
  console.log('checkout script loaded!')

  let cart = localStorage.getItem('leo-shop-cart')
  if (cart) {
    cart = JSON.parse(cart)
    setSavedCart(cart)
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
    $item.attr('leo-data-product-id', pro.id)
    $item.find('.leo-checkout-product-img').attr('src', pro.image)
    $item.find('.leo-checkout-product-name').text(pro.name)
    $item.find('.leo-checkout-qty').text(pro.quantity)
    $item.find('.leo-checkout-product-price').text(formatMoney(pro.price * pro.quantity))
    $item.on('click', e => handleProductClick(e, $))
    $item.css('display', 'block')

    $checkoutPanel.append($item)
    totalMoney += pro.price * pro.quantity
  })

  $cartTotal.find('.leo-checkout-total-money').text(formatMoney(totalMoney))
  $checkoutPanel.append($cartTotal)
}

const handleProductClick = (e, $) => {
  let cart = localStorage.getItem('leo-shop-cart')
  cart = JSON.parse(cart)

  let currQty

  const $pro = $(e.currentTarget)
  const productId = $pro.attr('leo-data-product-id')
  const $target = $(e.target)
  const clickData = $target.attr('data-leo-checkout-click')

  switch (clickData) {
    case 'remove':
      console.log('remove')
      cart = cart.filter(pro => pro.id !== productId)
      updateTotalMoney(cart)
      setSavedCart(cart)
      localStorage.setItem('leo-shop-cart', JSON.stringify(cart))
      $pro.remove()

      // update in header
      let cartNo = cart.length
      cartNo = cartNo > 9 ? cartNo : '0' + cartNo
      $('#leo-cart-header-no').text(cartNo)
      break
    case 'inc':
      currQty = parseInt($pro.find('.leo-checkout-qty').text())
      $pro.find('.leo-checkout-qty').text(currQty + 1)
      $pro.find('.leo-checkout-inc-qty').removeClass('pointer-event-none')
      if (currQty === 4) $target.addClass('pointer-event-none')

      cart = cart.map(pro => {
        if (pro.id === productId) pro.quantity = currQty + 1
        return pro
      })

      updateTotalMoney(cart)
      setSavedCart(cart)
      localStorage.setItem('leo-shop-cart', JSON.stringify(cart))

      break
    case 'dec':
      currQty = parseInt($pro.find('.leo-checkout-qty').text())
      $pro.find('.leo-checkout-qty').text(currQty - 1)
      $pro.find('.leo-checkout-dec-qty').removeClass('pointer-event-none')
      if (currQty === 2) $target.addClass('pointer-event-none')

      cart = cart.map(pro => {
        if (pro.id === productId) pro.quantity = currQty - 1
        return pro
      })

      updateTotalMoney(cart)
      setSavedCart(cart)
      localStorage.setItem('leo-shop-cart', JSON.stringify(cart))
      break
    default: console.log('Leo product clicked'); break;
  }

}

const setSavedCart = cart => {
  const savedCart = cart.map(pro => { return { id: pro.id, quantity: pro.quantity } })
  jQuery('input[name="leo_cart"]').attr('value', JSON.stringify(savedCart))
}

const updateTotalMoney = (cart, productId, currQty) => {
  let totalMoney = 0
  cart = cart.map(pro => {
    totalMoney += pro.price * pro.quantity
    return pro
  })
  console.log(cart)
  jQuery('#leo-checkout-total').find('.leo-checkout-total-money').text(formatMoney(totalMoney))
}