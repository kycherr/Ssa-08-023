import unittest
from product import ProductModel

class TestProductModel(unittest.TestCase):
    def test_create_product(self):
        product = ProductModel('Product 1', 10.0)
        self.assertEqual(product.name, 'Product 1')
        self.assertEqual(product.price, 10.0)

if __name__ == '__main__':
    unittest.main()