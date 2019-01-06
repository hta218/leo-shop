from mongoengine import Document, StringField, ListField, IntField, BooleanField
# import mlab

# mlab.connect()

class Product(Document):
    category = StringField()
    name = StringField()
    images = ListField()
    price = StringField()
    colors = ListField()
    tags = ListField()
    brand = StringField()
    offer = IntField()
    new = BooleanField()
    intro = StringField()
    description = StringField()
    quantity = IntField()
    rate = IntField()
    deals = ListField()


    @classmethod
    def getProductByCategory(cls, category):
      products = Product.objects(category=category).limit(9).skip(0).fields(images=1, name=1, price=1, new=1, offer=1)
      return products

    @classmethod
    def getHomeProducts(cls):
      hotProducts = Product.objects(new=True).limit(8).fields(images=1, name=1, price=1, new=1, offer=1)
      return hotProducts

    # @classmethod
    # def getProductByField(cls, field):
    #   products = Product.objects([field]=field).limit(9).skip(0).fields(images=1, name=1, price=1, new=1, offer=1)
    #   return products

# for i in range(20):
#   pro = Product(
#     category="mobile",
#     name="Điện thoại iPhone Xs Max 512GB",
#     images=[
#         'https://cdn.tgdd.vn/Products/Images/42/191482/iphone-xs-max-512gb-gold-400x460.png',
#         'https://cdn.tgdd.vn/Products/Images/42/191482/iphone-xs-max-512gb-vang-1-1-org.jpg',
#         'https://cdn.tgdd.vn/Products/Images/42/191482/iphone-xs-max-512gb-vang-2-1-org.jpg',
#         'https://cdn.tgdd.vn/Products/Images/42/191482/iphone-xs-max-512gb-vang-4-org.jpg',
#         'https://cdn.tgdd.vn/Products/Images/42/191482/iphone-xs-max-512gb-vang-11-org.jpg'
#     ],
#     price='37.990.000đ',
#     colors=['gold', 'white', 'black'],
#     tags=['iphone', 'apple'],
#     brand='apple',
#     offer='10',
#     new=True,
#     intro='Sau 1 năm mong chờ, chiếc smartphone cao cấp nhất của Apple đã chính thức ra mắt mang tên iPhone Xs Max. Máy các trang bị các tính năng cao cấp nhất từ chip A12 Bionic, dàn loa đa chiều cho tới camera kép tích hợp trí tuệ nhân tạo.',
#     description="""
#       Hiệu năng đỉnh cao cùng chip Apple A12
#       iPhone Xs Max được Apple trang bị cho con chip mới toanh hàng đầu của hãng mang tên Apple A12.

#       Chip A12 Bionic được xây dựng trên tiến trình 7nm đầu tiên mà hãng sản xuất với 6 nhân đáp ứng vượt trội trong việc xử lý các tác vụ và khả năng tiết kiệm năng lượng tối ưu.

#       Trải nghiệm điện thoại iPhone Xs Max chính hãng

#       Hơn nữa, chiếc điện thoại iPhone còn có bộ xử lý đồ họa mạnh mẽ được Apple thiết kế riêng giúp hiệu năng được cải thiện rất lớn về mặt đồ họa của máy.

#       Chưa dừng lại ở đó, máy còn được tích hợp trí thông minh nhân tạo giúp phần cứng tối ưu hiệu suất, nhờ đó mà các thao tác của bạn được xử lý một cách nhanh chóng hơn.

#       Trải nghiệm điện thoại iPhone Xs Max chính hãng

#       Thiết kế viền thép không gỉ và mặt kính cường lực cao cấp, chắc chắn
#       Điện thoại iPhone Xs Max sở hữu lối thiết kế vô cùng đẹp mắt với những đường cong mềm mại được thừa hưởng từ chiếc iPhone đời trước đó.

#       Thiết kế điện thoại iPhone Xs Max chính hãng
#       Tuy nhiên, iPhone Xs Max lại có một thân hình to bản ngang bằng với kích thước dòng Plus nhưng chứa đựng một màn hình rộng lớn lên đến 6.5 inch.

#       Thiết kế điện thoại iPhone Xs Max chính hãng
#       Nhờ thế mà bạn sẽ có một không gian trải nghiệm vô cùng rộng rãi để thưởng thức những bộ phim chất lượng cao được trở nên trọn vẹn.

#       Màn hình OLED chất lượng cao rộng 6.5 inch đầu tiên của Apple
#       Với công nghệ Super Retina kết hợp tấm nền OLED trên iPhone Xs Max đem lại dải màu sắc cực kì sống động và sắc nét đến từng chi tiết.

#       Màn hình điện thoại iPhone Xs Max chính hãng

#       Bên cạnh đó, Apple còn tích hợp thêm công nghệ HDR10 cùng tần số cảm ứng 120 Hz giúp chất lượng hình ảnh được nâng cao và mượt mà hơn đáng kể.

#       Màn hình điện thoại iPhone Xs Max chính hãng

#       Việc sở hữu màn hình lớn đem đến cho bạn khá nhiều tiện ích như dễ dàng chỉnh sửa ảnh, xem phim, lướt web nhưng sẽ khó khăn hơn trong việc di chuyển.

#       Camera kép tích hợp trí tuệ nhân tạo
#       Dù không sở hữu thông số camera khủng nhưng iPhone Xs Max luôn cho thấy sự đẳng cấp của mình về khả năng nhiếp ảnh với cụm camera kép độ phân giải 12MP.

#       Máy được trang bị hệ thống xử lý hình ảnh chất lượng cân bằng sáng, giảm nhiễu, tăng cường độ phơi sáng, màu da sao cho phù hợp và tự nhiên nhất.

#       Camera sau điện thoại iPhone Xs Max chính hãng

#       Cùng với đó là khả năng điều chỉnh khẩu độ ấn tượng từ f/1.4 đến f/16 ngay trên bức ảnh sau khi chụp ảnh với chế độ chân dung.

#       Chưa dừng lại ở đó, máy còn được tích hợp thêm công nghệ Smart HDR giúp tái tạo hình ảnh và cho ra một bức hình với độ sáng tốt nhất.

#       Camera sau điện thoại iPhone Xs Max chính hãng

#       Ngoài ra, iPhone Xs Max còn được hỗ trợ bởi trí thông minh nhân tạo đem đến khả năng tự động điều chỉnh màu sắc, độ sáng và độ tương phản sao cho phù hợp với từng vật thể khác nhau.

#       Một số tính năng cao cấp được cập nhật và bổ sung
#       Face ID đã được Apple cải tiến về khả năng bảo mật cũng như cho tốc độ mở khóa được nhanh hơn nhờ các thuật toán mới.

#       Mở khoá điện thoại iPhone Xs Max chính hãng

#       Bên cạnh đó, tính năng Animoji cũng được cập nhật thêm một số biểu tượng mới trông khá ngộ nghĩnh và đáng yêu.

#       Animoji trên điện thoại iPhone Xs Max chính hãng

#       Với hệ thống camera TrueDepth nay bạn có thể tự tạo cho bản thân những bức ảnh ấn tượng với công nghệ thực tế ảo tăng cường AR.

#       Ngoài ra, hệ thống âm thanh 2 chiều trên siêu phẩm mới được Apple tinh chỉnh lại cho dải âm rộng, âm thanh sống động hơn hay khả năng kháng nước và bụi cũng được nâng cấp lên thành IP 68 đảm bảo an toàn hơn cho máy.
#       """,
#     quantity = 20,
#     rate = 5,
#     deals=[
#       'Giảm ngay 1 triệu *',
#       'Mua kèm Tai nghe Bluetooth AirPods Apple với giá ưu đãi giảm 1 triệu (không áp dụng đồng thời khuyến mãi khác)',
#       'Cơ hội trúng 61 xe Wave Alpha khi trả góp Home Credit'
#     ]
#   )
#   pro.save()
