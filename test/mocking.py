from unittest import TestCase
from unittest.mock import Mock


class TestSubstraction(TestCase):
    def test_substraction(self):
        subtract = Mock(return_value=7)
        self.assertEqual(subtract(12, 5), 7)
        print(subtract.return_value)