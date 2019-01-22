jQuery(document).ready(function () {
  const $ = jQuery

  initPagination($)

  $('#leo-toolbar-order').on('change', function () {
    console.log('Leo toolbar change')
    const value = $(this).val()
    const { href } = window.location

    if (href.indexOf('search') < 0) {
      window.location = `/product/search?order-by=${value}`
    } else {
      window.location = updateQueryStringParameter(href, 'order-by', value)
    }
  })

  $('#leo-toolbar-pagination').on('click', e => {
    e.preventDefault()
    const $target = $(e.target)
    const value = $target.attr('data-leo-page-click')
    const { href } = window.location
    let currPage = parseInt(localStorage.getItem('leo-curr-page'))
    if (!currPage) currPage = 1

    switch (value) {
      case 'next':
        currPage += 1
        console.log('next')
        localStorage.setItem('leo-curr-page', currPage)
        window.location = updateQueryStringParameter(href, 'page', currPage)
        break
      case 'prev':
        currPage -= 1
        console.log('prev')
        localStorage.setItem('leo-curr-page', currPage)
        window.location = updateQueryStringParameter(href, 'page', currPage)
        break
      default:
        const page = parseInt(value)
        if (!page) break

        localStorage.setItem('leo-curr-page', page)
        window.location = updateQueryStringParameter(href, 'page', page)
        break
    }
  })
})

const initPagination = $ => {
  let currPage = parseInt(localStorage.getItem('leo-curr-page'))
  if (!currPage) currPage = 1

  $('.leo-page').removeClass('active')
  $(`.leo-page[data-leo-page-click="${currPage}"]`).addClass('active')

  if (currPage === 3) {
    $('.leo-page-navigation.next-page').addClass('pointer-event-none')
  } else if (currPage === 1) {
    $('.leo-page-navigation.prev-page').addClass('pointer-event-none')
  }
}

// Something from SO! Ref: https://stackoverflow.com/questions/5999118/how-can-i-add-or-update-a-query-string-parameter
function updateQueryStringParameter(uri, key, value) {
  var re = new RegExp("([?&])" + key + "=.*?(&|$)", "i");
  var separator = uri.indexOf('?') !== -1 ? "&" : "?";
  if (uri.match(re)) {
    return uri.replace(re, '$1' + key + "=" + value + '$2');
  }
  else {
    return uri + separator + key + "=" + value;
  }
}