from product import Product
from flask import *
import mlab
import json
from order import Order
from user import User

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

@app.route('/product/search')
def search():
    search_type = request.args.get('type')
    value = request.args.get('value')
    
    products = Product.search(search_type, value)
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
        customer_name = form['name']
        phone_number = form['phone_number']
        email = form['email']
        requirement = form['requirement']
        address = form['address']
        district = form['district']
        province = form['province']
        payment = form['payment']
        cart = json.loads(form['leo_cart'])

        Order.createOrder(
            customer_name, phone_number, email,
            requirement, address, district, province,
            payment, cart
        )

        return redirect('/checkout-success')

@app.route('/checkout-success')
def checkout_success():
    hotProducts = Product.getHomeProducts()
    hotProducts_1 = []
    hotProducts_2 = []
    cols = 4

    for i in range(3):
        hotProducts_1.append(hotProducts[i])
        hotProducts_2.append(hotProducts[i + 3])

    return render_template('checkout-success.html', 
                            hotProducts_1=hotProducts_1, 
                            hotProducts_2=hotProducts_2,
                            cols=cols)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login')
def login():
    user_name = request.args.get('user_name')
    password = request.args.get('password')
    user = User.findUser(user_name, password)

    if user is None: 
        return jsonify(user)

    display_name = user.display_name
    role = user.role

    return jsonify({ 'display_name': display_name, 'role': role })

@app.route('/register')
def register():
    data = User.register(request)
    return jsonify(data)

@app.route('/logout')
def logout():
    return redirect('/')

@app.route('/admin')
def admin():
    model = request.args.get('model')
    category = request.args.get('category')
    if category is None:
        category = 'mobile'

    if model == 'product':
        products = Product.objects(category=category)
        return render_template('admin/index.html', products=products)
    elif model == 'user':
        users = User.objects()
        return render_template('admin/admin-user.html', users=users)
    elif model == 'order':
        orders = Order.objects()
        return render_template('admin/admin-order.html', orders=orders)
    else:
        products = Product.objects(category='mobile')
        return render_template('admin/index.html', products=products)
        
@app.route('/admin/add-product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'GET': 
        return render_template('admin/new-product-form.html')
    else: 
        form = request.form
        Product.createProduct(form)
        return render_template('admin/new-product-form.html')

@app.route('/delete-product/<pro_id>')
def delete_product(pro_id):
    pro = Product.objects.with_id(pro_id)
    if pro is not None:
        pro.delete()

    return redirect('/admin')

if __name__ == '__main__':
    app.run(debug=True)
