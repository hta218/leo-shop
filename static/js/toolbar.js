jQuery(document).ready(function () {
  const $ = jQuery
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

    switch (value) {
      case 'next':
        console.log('next')
        break
      case 'prev':
        console.log('prev')
        break
      default:
        const page = parseInt(value)
        if (!page) break

        const { href } = window.location
        window.location = updateQueryStringParameter(href, 'page', page)
        break
    }
  })
})

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