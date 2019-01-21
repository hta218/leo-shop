$(document).ready(function() {
  console.log('Admin script loaded')
  $('#leo-des-add').on('click', function() {
    const $des = $('.leo-des-form').clone(true)
    $des.removeClass('d-none')
    $('#leo-des-form-panel').append($des)
  })

  $('.leo-remove-des').on('click', function() {
    const $des = $(this).closest('.leo-des-form')
    $des.remove()
  })
})