#coding=utf8
from mongoengine import Document, StringField, ListField, IntField, BooleanField, DictField, DateTimeField
import mlab
from product import Product
from gmail import GMail, Message
from datetime import datetime
import locale
locale.setlocale( locale.LC_ALL, '' )

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
  total = IntField()
  display_total = StringField()
  time = DateTimeField()
  display_time = StringField()


  @classmethod
  def createOrder(cls, customer_name, phone_number, email, requirement, address, district, province, payment, cart):
    time = datetime.now()
    total = 0
    payment_in_mail = 'Chuyển khoản ngân hàng qua tài khoản 41210000669434 (Ngân Hàng BIDV)' if payment == 'online' else 'Gửi tiền khi nhận hàng'
    cart_html = ''
    pro_html_form = '''
      <tr>
        <td>
          <p>
            <img src="{{pro_image}}" width="100px">
          </p>
        </td>
        <td>
          <p>{{pro_name}}</p>
        </td>
        <td align="center">{{pro_quantity}}</td>
        <td>{{pro_price}}</td>
      </tr>
    '''

    for pro in cart:
      curr_pro = Product.objects.with_id(pro['id'])
      if curr_pro is not None:
        curr_pro.update(set__quantity=(curr_pro['quantity'] - pro['quantity']))
        total += pro['quantity'] * curr_pro.price
        pro_html = pro_html_form \
                      .replace('{{pro_image}}', curr_pro.images[0]) \
                      .replace('{{pro_name}}', curr_pro.name) \
                      .replace('{{pro_quantity}}', str(pro['quantity'])) \
                      .replace('{{pro_price}}', str(curr_pro.display_price)) \

        cart_html += pro_html

    display_total = formatMoney(total)
    display_time = str(time.strftime("%H:%M %p - %d/%m/%Y"))

    #### MUST BE IN ORDER - FUCK Python
    new_order = Order(
      customer_name, phone_number, email,
      requirement, address, district,
      province, payment, cart, total, display_total, time,
      display_time
    )

    new_order.save()

    order_mail = open('assets/order-mail.html', encoding="utf8") \
                  .read() \
                  .replace('{{customer_name}}', customer_name) \
                  .replace('{{order_id}}', str(new_order.id)) \
                  .replace('{{order_cart}}', cart_html) \
                  .replace('{{order_total}}', display_total) \
                  .replace('{{order_time}}', display_time) \
                  .replace('{{order_payment_method}}', payment_in_mail) \
                  .replace('{{order_address}}', "{0}, {1}, {2}".format(address, district, province))

    gmail = GMail('20130075@student.hust.edu.vn','tuananh1k95')
    msg = Message('Thông báo xác nhận đơn hàng', to=email, html=order_mail)
    gmail.send(msg)


def formatMoney(money):
  return locale \
          .currency(money, grouping=True) \
          .replace('$', '') \
          .replace('.00', 'đ') \
          .replace(',', '.') \