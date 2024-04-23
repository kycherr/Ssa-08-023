import unittest
from db import (
    create_product,
    get_product_by_id,
    update_product,
    delete_product,
    ProductModel
)

class TestProductDatabase(unittest.TestCase):

    def setUp(self):
        # Set up any initial state needed for the tests
        pass

    def tearDown(self):
        # Clean up any resources used by the tests
        pass

    def test_create_product(self):
        # Test creating a product
        product = create_product("Test Product", 50)
        self.assertIsInstance(product, ProductModel)
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.price, 50)

    def test_get_product_by_id(self):
        # Test retrieving a product by ID
        product = create_product("Test Product", 50)
        retrieved_product = get_product_by_id(product.id)
        self.assertIsInstance(retrieved_product, ProductModel)
        self.assertEqual(retrieved_product.name, "Test Product")
        self.assertEqual(retrieved_product.price, 50)

    def test_update_product(self):
        # Test updating a product
        product = create_product("Test Product", 50)
        updated_product = update_product(product.id, name="Updated Product", price=100)
        self.assertEqual(updated_product.id, product.id)
        self.assertEqual(updated_product.name, "Updated Product")
        self.assertEqual(updated_product.price, 100)

    def test_delete_product(self):
        # Test deleting a product
        product = create_product("Test Product", 50)
        self.assertTrue(delete_product(product.id))
        self.assertIsNone(get_product_by_id(product.id))

if __name__ == '__main__':
    unittest.main()
