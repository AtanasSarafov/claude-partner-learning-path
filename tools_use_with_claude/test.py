import unittest
from main import calculate_pi


class TestCalculatePi(unittest.TestCase):
    """Test cases for the calculate_pi function."""
    
    def test_pi_accuracy(self):
        """Test that pi is calculated to 10 decimal places accurately."""
        result = calculate_pi()
        expected_pi = 3.1415926536  # Pi to 10 decimal places
        
        # Check if result matches expected value
        self.assertEqual(result, expected_pi, 
                        f"Expected {expected_pi}, but got {result}")
    
    def test_pi_return_type(self):
        """Test that the function returns a float."""
        result = calculate_pi()
        self.assertIsInstance(result, float, 
                            "calculate_pi should return a float")
    
    def test_pi_range(self):
        """Test that pi is within a reasonable range."""
        result = calculate_pi()
        self.assertGreater(result, 3.14, 
                          "Pi should be greater than 3.14")
        self.assertLess(result, 3.15, 
                       "Pi should be less than 3.15")
    
    def test_pi_decimal_places(self):
        """Test that the result has at most 10 decimal places."""
        result = calculate_pi()
        # Convert to string and count decimal places
        result_str = str(result)
        if '.' in result_str:
            decimal_places = len(result_str.split('.')[1])
            self.assertLessEqual(decimal_places, 10, 
                                f"Result should have at most 10 decimal places, got {decimal_places}")


if __name__ == '__main__':
    unittest.main()
