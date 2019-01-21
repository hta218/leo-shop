#coding=utf8
from mongoengine import Document, StringField, ListField, IntField, BooleanField
import mlab
from helper import formatMoney
mlab.connect()

class Product(Document):
    category = StringField()
    name = StringField()
    images = ListField()
    price = IntField()
    display_price = StringField()
    colors = ListField()
    tags = ListField()
    brand = StringField()
    offer = IntField()
    new = BooleanField()
    intro = StringField()
    description = ListField()
    quantity = IntField()
    rate = IntField()
    deals = ListField()


    @classmethod
    def getProductByCategory(cls, category):
      products = Product.objects(category=category).limit(9).skip(0).fields(images=1, 
                                                                            name=1, 
                                                                            price=1, 
                                                                            display_price=1,
                                                                            new=1, 
                                                                            offer=1)
      return products

    @classmethod
    def getHomeProducts(cls):
      hotProducts = Product.objects(new=True).limit(8).fields(images=1, name=1, price=1, display_price=1, new=1, offer=1)
      return hotProducts

    @classmethod
    def createProduct(cls, form):
      category = form['category']
      name = form['name']
      brand = form['brand']
      price = form['price']
      quantity = form['quantity']

      offer = form['offer']
      colors = form.getlist('colors')
      tags = form.getlist('tags')

      deals = [form['deals1'], form['deals2'], form['deals3']]
      intro = form['intro']
      images = [form['image1'], form['image2'], form['image3'], form['image4'], form['image5']]

      description = [
        {
          'title': form['des_title1'],
          'content': form['des_content1'],
          'image': form['des_img1'],
        },
        {
          'title': form['des_title2'],
          'content': form['des_content2'],
          'image': form['des_img2'],
        },
        {
          'title': form['des_title3'],
          'content': form['des_content3'],
          'image': form['des_img3'],
        },
      ]

      new_pro = Product(
        category=category,
        name=name,
        brand=brand,
        price=price,
        display_price=formatMoney(int(price)),
        quantity=quantity,
        offer=offer,
        colors=colors,
        tags=tags,
        deals=deals,
        intro=intro,
        images=images,
        description=description,
        rate=5,
        new=True
      )

      new_pro.save()