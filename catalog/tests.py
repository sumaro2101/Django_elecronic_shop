from django.test import TestCase
from django.utils import timezone
# Create your tests here.
from .models import Product, Companies, Category
from .templatetags.tags_filter import discount, filter_query


class ProductModelTests(TestCase):
    
    def test_is_new(self):
        product = Product(name='some', company_id='ROG', category_id='Телефоны', price=323132, discount=0, quantity=1, release=timezone.now())
        self.assertTrue(product.is_new())
        
    def test_is_sale(self):
        product = Product(name='some', company_id='ROG', category_id='Телефоны', price=323132, discount=17.0, quantity=1)
        self.assertTrue(product.is_sale())
   
        
class TagDiscountTests(TestCase):
    
    def test_one_hundred_procent(self):
        result = discount(30000, 100.0)
        self.assertEqual(result, 0)
        
    def test_fifty_procent(self):
        result = discount(30000, 50.0)
        self.assertEqual(result, 15000)
        
    def test_zero_procent(self):
        result = discount(30000, 0.0)
        self.assertEqual(result, 30000)
        
class TagFilterQueryTests(TestCase):
    
    pass
