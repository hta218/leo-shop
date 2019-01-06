from product import Product
from flask import Flask, render_template
import mlab

app = Flask(__name__)
mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

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
