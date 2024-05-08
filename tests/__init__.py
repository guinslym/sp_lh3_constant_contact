import unittest
from sp_lh3_constant_contact import check_operator_response
from pprint import pprint as tprint

class TestOperatorResponse(unittest.TestCase):
    def test_response_time(self):
        # Test cases with known discrepancies
        discrepancies = check_operator_response(3423927, constant_contact=5)
        self.assertEqual(len(discrepancies), 1)  # Check if there is one discrepancy

        # Add more test cases for different chat IDs if needed
        # discrepancies = check_operator_response(another_chat_id, constant_contact=5)
        # self.assertEqual(len(discrepancies), expected_number_of_discrepancies)

    def test_no_discrepancy(self):
        # Test cases with no discrepancies
        discrepancies = check_operator_response(3423928, constant_contact=5)
        self.assertEqual(len(discrepancies), 0)  # Check if there are no discrepancies

        # Add more test cases for different chat IDs if needed
        # discrepancies = check_operator_response(another_chat_id, constant_contact=5)
        # self.assertEqual(len(discrepancies), 0)

if __name__ == "__main__":
    unittest.main()
