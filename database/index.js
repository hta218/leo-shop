const puppeteer = require('puppeteer');

  (async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto('https://www.thegioididong.com/dtdd');
    await page.addScriptTag({ path: require.resolve('jquery') })

    const products = await page.evaluate(async () => {
      const $ = window.$
      let products = []
      const lis = await document.querySelector('ul.homeproduct').querySelectorAll('li')

      lis.forEach(li => {
        const imgLink = $(li).find('img').attr('src')
        products.push(imgLink)
      })


      return products
    })

    console.log(products)

    await browser.close();
  })();