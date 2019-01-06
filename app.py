from product import Product
from flask import Flask, render_template
import mlab

app = Flask(__name__)
mlab.connect()

@app.route('/')
def index():
    hotProducts = Product.getHomeProducts()
    hotProducts_1 = []
    hotProducts_2 = []

    for i in range(4):
        hotProducts_1.append(hotProducts[i])
        hotProducts_2.append(hotProducts[i + 4])

    featureProducts = Product.getHomeProducts()
    feaProducts_1 = []
    feaProducts_2 = []

    for i in range(4):
        feaProducts_1.append(featureProducts[i])
        feaProducts_2.append(featureProducts[i + 4])

    return render_template('index.html',
                            hotProducts_1=hotProducts_1, 
                            hotProducts_2=hotProducts_2, 
                            feaProducts_1=feaProducts_1,
                            feaProducts_2=feaProducts_2
                            )

@app.route('/product/<cat>')
def category(cat):
    products = Product.getProductByCategory(cat)
    print(products[0].to_mongo())
    return render_template('productgrid.html', products=products)

@app.route('/detail/<id>')
def detail(id):
    product = Product.objects().with_id(id)
    return render_template('product-detail.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)
