#coding=utf8
from mongoengine import Document, StringField, IntField
import mlab

mlab.connect()

class User(Document):
  display_name = StringField()
  user_name = StringField()
  password = StringField()
  email = StringField()
  role = StringField()
  gender = IntField()
  phone_number = StringField()
    
  @classmethod
  def findUser(cls, user_name, password):
    user = User.objects(user_name=user_name, password=password).first()
    return user

# new_user = User(
#   display_name = "Huỳnh Tuấn Anh",
#   user_name = 'admin',
#   password = '123456',
#   email="anhht@bravebits.vn",
#   role="admin",
#   gender=1,
#   phone_number="0387176583"
# )

# new_user.save()