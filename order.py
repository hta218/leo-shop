from mongoengine import Document, StringField, ListField, IntField, BooleanField, DictField
import mlab
from product import Product

mlab.connect()

class Order(Document):
  customer_name = StringField()
  phone_number = StringField()
  email = StringField()
  requirement = StringField()
  address = StringField()
  district = StringField()
  province = StringField()
  payment = StringField()
  cart = ListField()



  @classmethod
  def createOrder(cls, order):
    new_order = Order(
      customer_name = order['customer_name'],
      phone_number = order['phone_number'],
      email = order['email'],
      requirement = order['requirement'],
      address = order['address'],
      district = order['district'],
      province = order['province'],
      payment = order['payment'],
      cart = order['cart']
    )

    for pro in order['cart']:
      curr_pro = Product.objects.with_id(pro['id'])
      if curr_pro is not None:
        curr_pro.update(
          set__quantity=(curr_pro['quantity'] - pro['quantity'])
        )
    
    new_order.save()

    return 'ok'