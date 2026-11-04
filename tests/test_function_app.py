import unittest
from function_app import analyze_number


class TestAnalyzeNumber(unittest.TestCase):

    def test_perfect_number_28(self):
        self.assertEqual(
            analyze_number(28),
            {
                "sum_of_digits": 10,
                "is_prime": False,
                "is_odd": False,
                "is_perfect": True
            }
        )

    def test_prime_number_7(self):
        self.assertEqual(
            analyze_number(7),
            {
                "sum_of_digits": 7,
                "is_prime": True,
                "is_odd": True,
                "is_perfect": False
            }
        )

    def test_perfect_number_6(self):
        self.assertTrue(analyze_number(6)["is_perfect"])

    def test_number_10(self):
        self.assertEqual(
            analyze_number(10),
            {
                "sum_of_digits": 1,
                "is_prime": False,
                "is_odd": False,
                "is_perfect": False
            }
        )

    def test_zero(self):
        self.assertEqual(
            analyze_number(0),
            {"error": "please enter a number greater than 0"}
        )

    def test_invalid_data_type(self):
        self.assertEqual(
            analyze_number("hello"),
            {"error": "please enter a valid number"}
        )


if __name__ == "__main__":
    unittest.main()