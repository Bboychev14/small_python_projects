from unittest import TestCase, main

from shopping_cart_logic import ShoppingCart


class ShoppingCartTests(TestCase):

    def test_constructor_with_correct_data(self):
        test_cart = ShoppingCart("Test", 100)
        self.assertEqual("Test", test_cart.shop_name)
        self.assertEqual(100, test_cart.budget)

    def test_name_with_wrong_data(self):
        test_cart = ShoppingCart("Test", 100)
        with self.assertRaises(ValueError) as ex:
            test_cart.shop_name = 'test'
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ex.exception))
        self.assertEqual("Test", test_cart.shop_name)

        with self.assertRaises(ValueError) as ex:
            test_cart.shop_name = "Test1"
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ex.exception))


if __name__ == '__main__':
    main()