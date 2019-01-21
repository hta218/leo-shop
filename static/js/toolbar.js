jQuery(document).ready(function () {
  const $ = jQuery
  $('#leo-toolbar-order').on('change', function () {
    console.log('Leo toolbar change')
    const value = $(this).val()
    const { href } = window.location
    if (href.indexOf('order-by') > 0) {
      window.location = updateQueryStringParameter(href, 'order-by', value)
    } else if (href.indexOf('search') < 0) {
      window.location = `/product/search?order-by=${value}`
    } else {
      const temp = href.indexOf('?') > 0 ? '&' : '?'
      window.location = `${href}${temp}order-by=${value}`
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