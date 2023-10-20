from django.test import SimpleTestCase
from home.models import Product


class TestModels(SimpleTestCase):

    def test_product(self):
        name = Product.objects.create(name='poco')
        self.assertEqual(str(name), 'poco')
        print("Isinstance:", isinstance(name, Product))
        self.assertTrue(isinstance(name, Product))
