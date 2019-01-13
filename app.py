from product import Product
from flask import *
import mlab
import json
from order import Order

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

    cols=3
    return render_template('index.html',
                            hotProducts_1=hotProducts_1, 
                            hotProducts_2=hotProducts_2, 
                            feaProducts_1=feaProducts_1,
                            feaProducts_2=feaProducts_2,
                            cols=3
                            )

@app.route('/product/<cat>')
def category(cat):
    products = Product.getProductByCategory(cat)
    return render_template('productgrid.html', products=products)

@app.route('/detail/<id>')
def detail(id):
    product = Product.objects().with_id(id)
    hotProducts = Product.getHomeProducts()
    hotProducts_1 = []
    hotProducts_2 = []
    cols = 4

    for i in range(3):
        hotProducts_1.append(hotProducts[i])
        hotProducts_2.append(hotProducts[i + 3])

    return render_template('product-detail.html', 
                            product=product, 
                            hotProducts_1=hotProducts_1, 
                            hotProducts_2=hotProducts_2,
                            cols=cols)

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'GET':
        return render_template('checkout.html')
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        phone_number = form['phone_number']
        email = form['email']
        requirement = form['requirement']
        address = form['address']
        district = form['district']
        province = form['province']
        payment = form['payment']
        cart = json.loads(form['leo_cart'])

        print('=====================>', name)

        Order.createOrder({
            'customer_name': name,
            'phone_number': phone_number,
            'email': email,
            'requirement': requirement,
            'address': address,
            'district': district,
            'province': province,
            'payment': payment,
            'cart': cart,
        })

        return 'done'

if __name__ == '__main__':
    app.run(debug=True)
