jQuery(document).ready(function () {
  console.log('Custom JS loaded')
  const $ = jQuery

  initCart($)
  findCurrUser($)

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

  $('#leo-shop-cart').hover(function () {
    let cart = localStorage.getItem('leo-shop-cart')

    if (cart) {
      cart = JSON.parse(cart)
      renderHeaderCart($, cart)
    }
  })

  $('#leo-login-btn').on('click', e => {
    e.preventDefault()
    handleLogin($)
  })

  $('#leo-register-btn').on('click', e => {
    e.preventDefault()
    handleRegister($)
  })

  $('#leo-logout-user').on('click', e => {
    e.preventDefault()
    localStorage.removeItem('leo-curr-user')
    window.location = '/logout'
  })

  $('#leo-filter-btn').on('click', e => {
    e.preventDefault()
    const $form = $("#leo-filter-form")
    const floor = $form.find('input[name="floor"]').val()
    const ceil = $form.find('input[name="ceil"]').val()
    window.location = `/product/search?type=price&value=${floor}-${ceil}`
  })

  $('#leo-search-product-form').on('submit', e => {
    e.preventDefault()
    const $form = $('#leo-search-product-form')
    const term = $form.find('input[name="search"]').val()
    window.location = `/product/search?type=name&value=${term}`
  })
})

const findCurrUser = $ => {
  const user = localStorage.getItem('leo-curr-user')
  if (user) {
    $('#leo-user-menu').find('ul').addClass('d-none')
    $('#leo-user-name').text(user)
    $('#leo-user-menu').find('div').removeClass('d-none').addClass('d-block')
  }
}

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

const handleLogin = $ => {
  const $form = $("#leo-login-form")
  const user_name = $form.find('input[type="text"]').val()
  const password = $form.find('input[type="password"]').val()
  const remember = $form.find('input[type="checkbox"]').val()

  $.ajax({
    url: '/login',
    data: { user_name, password },
    type: 'GET',
    contentType: 'application/json;charset=UTF-8',
    success: function (user) {
      console.log(user)
      if (!user) $('.leo-form-warning').eq(0).css('display', 'block')
      else {
        if (user.role === 'admin') {
          window.location = '/admin'
          return
        }

        $('#login-modal').modal('hide')
        $('#leo-user-menu').find('ul').addClass('d-none')
        $('#leo-user-name').text(user.display_name)
        $('#leo-user-menu').find('div').addClass('d-block')

        if (remember) {
          localStorage.setItem('leo-curr-user', user.display_name)
        } else {
          localStorage.removeItem('leo-curr-user')
        }
      }
    },
    error: function (err) {
      console.log(err);
    }
  });
}

const handleRegister = $ => {
  const $form = $("#leo-register-form")
  const display_name = $form.find('input[name="name"]').val()
  const user_name = $form.find('input[name="user_name"]').val()
  const email = $form.find('input[name="email"]').val()
  const role = $form.find('input[name="role"]').val()
  const gender = $form.find('input[name="gender"]').val()
  const phone_number = $form.find('input[name="phone_number"]').val()

  $.ajax({
    url: '/register',
    data: { display_name, user_name, email, role, gender, phone_number },
    type: 'GET',
    contentType: 'application/json;charset=UTF-8',
    success: function (data) {
      console.log(data)
      if (!data.success) {
        $('.leo-form-warning').eq(1).find('i').text(`Tên đăng nhập "${user_name}" đã tồn tại !`)
        $('.leo-form-warning').eq(1).css('display', 'block')
      }
      else {
        $('#register-modal').modal('hide')
        $('#leo-user-menu').find('ul').addClass('d-none')
        $('#leo-user-name').text(display_name)
        $('#leo-user-menu').find('div').removeClass('d-none').addClass('d-block')
      }
    },
    error: function (err) {
      console.log(err);
    }
  });
}