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


  @classmethod
  def register(cls, request):
    display_name = request.args.get('display_name')
    user_name = request.args.get('user_name')
    email = request.args.get('email')
    role = request.args.get('role')
    gender = request.args.get('gender')
    phone_number = request.args.get('phone_number')

    user = User.objects(user_name=user_name).first()

    if user is None:
      new_user = User(
        display_name=display_name,
        user_name=user_name,
        password=user_name,
        email=email,
        role=role,
        gender=gender,
        phone_number=phone_number,
      )
      new_user.save()
      return { 'success': 1, 'display_name': display_name }
    
    return { 'success': 0 }