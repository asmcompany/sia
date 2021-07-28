from django.test import TestCase
from .models import Product
# Create your tests here.

class TestProduct(TestCase):

    def setUp(self):
        self.title = 'گوشت گیاهی'
        self.price = '20000'
        self.caption = 'گوشت خیلی خوب'
        self.description = 'کامل کامل از همه چی بهتر'
        self.specifications = 'some = something'
        self.image = ''
        self.brand = ''
        self.tag = ''
        self.category = ''
        self.is_active = ''
        self.timestamp = ''
        self.views = ''
        self.inventory = '23'
        self.slug = ''

        self._dict = {
            "title" : self.title ,
            "price" : self.price ,
            "caption" : self.caption ,
            "description" : self.description ,
            "specifications" : self.specifications ,
            # "image" : self.image ,
            # "brand" : self.brand ,
            # "tag" : self.tag ,
            # "category" : self.category ,
            # "is_active" : self.is_active ,
            # "timestamp" : self.timestamp ,
            # "views" : self.views ,
            "inventory" : self.inventory ,
            # "slug" : self.slug ,
        }

    # def create_product(self):
    #     product = Product.objects.create(args=self._dict)
    #     product.save()
    #     return product
    
    # def test_create(self):
    #     product = self.create_product()

    #     self.assertTrue(product)