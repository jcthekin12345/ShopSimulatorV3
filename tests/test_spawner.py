# tests/test_spawner.py
import unittest
from src.spawner import spawn_customer
from unittest.mock import patch


class TestSpawnCustomer(unittest.TestCase):

    def test_spawn_customer_returns_integer(self):
        result = spawn_customer()
        self.assertIsInstance(result, int, "The budget should be an integer.")

    def test_spawn_customer_within_bounds(self):
        for _ in range(100):  # Test multiple times for randomness
            result = spawn_customer()
            self.assertGreaterEqual(result, 1, "The budget should not be less than 1.")
            self.assertLess(result, 100, "The budget should be less than 100.")

    @patch('spawner.random.randrange')
    def test_spawn_customer_mocked(self, mock_randrange):
        mock_randrange.return_value = 42
        result = spawn_customer()
        self.assertEqual(result, 42, "The mocked value should be returned.")


if __name__ == '__main__':
    unittest.main()
