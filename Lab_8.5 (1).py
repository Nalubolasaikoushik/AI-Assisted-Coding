# # # #TASK-01:

# # # '''
# # # give the python code to develop 
# # # a user registration system that requires a email input validation with
# # # Must contain @ and . characters
# # #  Must not start or end with special characters
# # #  Should not allow multiple @ symbols
# # #  AI should generate test cases covering valid and invalid email formats
# # # Implement is_valid_email(email) to pass all AI-generated test cases'''
# # # import re
# # # def is_valid_email(email):
# # #     # Check if email contains exactly one @ symbol
# # #     if email.count('@') != 1:
# # #         return False
    
# # #     # Check if email contains at least one . character
# # #     if '.' not in email:
# # #         return False
    
# # #     # Check if email starts or ends with special characters
# # #     if email[0] in ['@', '.'] or email[-1] in ['@', '.']:
# # #         return False
    
# # #     # Check for valid characters in the email
# # #     if not re.match(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$', email):
# # #         return False
    
# # #     return True 
# # # # Test cases
# # # test_cases = {
# # #     "valid": [
# # #         "user@example.com",
# # #         "test.email@domain.co.uk",
# # #         "user123@test-domain.org"
# # #     ],
# # #     "invalid": [
# # #         "@example.com",
# # #         "user@",
# # #         "user..name@example.com",
# # #         "user@domain.",
# # #         "user@@domain.com",
# # #         ".user@example.com",
# # #         "user@example.",
# # #         "invalid.email"
# # #     ]
# # # }
# # # # Run test cases
# # # for email in test_cases["valid"]:
# # #     assert is_valid_email(email) == True, f"Expected {email} to be valid"   
# # # for email in test_cases["invalid"]:
# # #     assert is_valid_email(email) == False, f"Expected {email} to be invalid"


# # #TASK-02:
# # import unittest
# # from grading import assign_grade


# # class TestAssignGrade(unittest.TestCase):

# #     # ----- Valid Grade Tests -----

# #     def test_grade_A(self):
# #         self.assertEqual(assign_grade(95), "A")
# #         self.assertEqual(assign_grade(90), "A")   # boundary

# #     def test_grade_B(self):
# #         self.assertEqual(assign_grade(85), "B")
# #         self.assertEqual(assign_grade(80), "B")   # boundary

# #     def test_grade_C(self):
# #         self.assertEqual(assign_grade(75), "C")
# #         self.assertEqual(assign_grade(70), "C")   # boundary

# #     def test_grade_D(self):
# #         self.assertEqual(assign_grade(65), "D")
# #         self.assertEqual(assign_grade(60), "D")   # boundary

# #     def test_grade_F(self):
# #         self.assertEqual(assign_grade(50), "F")
# #         self.assertEqual(assign_grade(0), "F")

# #     # ----- Invalid Input Tests -----

# #     def test_negative_score(self):
# #         with self.assertRaises(ValueError):
# #             assign_grade(-5)

# #     def test_score_above_100(self):
# #         with self.assertRaises(ValueError):
# #             assign_grade(105)

# #     def test_non_numeric_input(self):
# #         with self.assertRaises(TypeError):
# #             assign_grade("eighty")


# # if __name__ == "__main__":
# #     unittest.main()

# #TASK-03:
# import unittest
# from palindrome import is_sentence_palindrome


# class TestSentencePalindrome(unittest.TestCase):

#     # ----- Valid Palindromes -----

#     def test_simple_palindrome(self):
#         self.assertTrue(is_sentence_palindrome("madam"))

#     def test_sentence_palindrome(self):
#         self.assertTrue(is_sentence_palindrome("A man a plan a canal Panama"))

#     def test_with_punctuation(self):
#         self.assertTrue(is_sentence_palindrome("Madam, I'm Adam"))

#     def test_mixed_case(self):
#         self.assertTrue(is_sentence_palindrome("RaceCar"))

#     def test_numeric_palindrome(self):
#         self.assertTrue(is_sentence_palindrome("12321"))

#     # ----- Non-Palindromes -----

#     def test_simple_non_palindrome(self):
#         self.assertFalse(is_sentence_palindrome("hello"))

#     def test_sentence_non_palindrome(self):
#         self.assertFalse(is_sentence_palindrome("This is not a palindrome"))

#     # ----- Edge Cases -----

#     def test_empty_string(self):
#         self.assertTrue(is_sentence_palindrome(""))

#     def test_only_punctuation(self):
#         self.assertTrue(is_sentence_palindrome("!!!"))

#     def test_non_string_input(self):
#         with self.assertRaises(TypeError):
#             is_sentence_palindrome(12321)


# if __name__ == "__main__":
#     unittest.main()

# import string


# def is_sentence_palindrome(sentence):
#     if not isinstance(sentence, str):
#         raise TypeError("Input must be a string")

#     # Normalize: remove non-alphanumeric characters and convert to lowercase
#     cleaned = ''.join(
#         char.lower() for char in sentence if char.isalnum()
#     )

#     return cleaned == cleaned[::-1]

#TASK-04:
# import unittest
# from shopping_cart import ShoppingCart


# class TestShoppingCart(unittest.TestCase):

#     def setUp(self):
#         self.cart = ShoppingCart()

#     # ----- Add Item Tests -----

#     def test_add_single_item(self):
#         self.cart.add_item("Laptop", 50000)
#         self.assertEqual(self.cart.total_cost(), 50000)

#     def test_add_multiple_items(self):
#         self.cart.add_item("Phone", 20000)
#         self.cart.add_item("Headphones", 2000)
#         self.assertEqual(self.cart.total_cost(), 22000)

#     # ----- Remove Item Tests -----

#     def test_remove_item(self):
#         self.cart.add_item("Tablet", 15000)
#         self.cart.remove_item("Tablet")
#         self.assertEqual(self.cart.total_cost(), 0)

#     def test_remove_one_of_multiple_items(self):
#         self.cart.add_item("Mouse", 1000)
#         self.cart.add_item("Keyboard", 3000)
#         self.cart.remove_item("Mouse")
#         self.assertEqual(self.cart.total_cost(), 3000)

#     def test_remove_non_existing_item(self):
#         with self.assertRaises(ValueError):
#             self.cart.remove_item("NonExisting")

#     # ----- Empty Cart Behavior -----

#     def test_empty_cart_total(self):
#         self.assertEqual(self.cart.total_cost(), 0)

#     # ----- Invalid Input Tests -----

#     def test_add_item_invalid_price(self):
#         with self.assertRaises(ValueError):
#             self.cart.add_item("Invalid", -100)

#     def test_add_item_non_numeric_price(self):
#         with self.assertRaises(TypeError):
#             self.cart.add_item("Invalid", "1000")


# if __name__ == "__main__":
#     unittest.main()

#TASK-05:
import unittest
from date_converter import convert_date_format


class TestConvertDateFormat(unittest.TestCase):

    # ----- Valid Dates -----

    def test_valid_date(self):
        self.assertEqual(convert_date_format("2023-10-15"), "15-10-2023")

    def test_valid_single_digit_month_day(self):
        self.assertEqual(convert_date_format("2023-01-05"), "05-01-2023")

    def test_leap_year_date(self):
        self.assertEqual(convert_date_format("2024-02-29"), "29-02-2024")

    # ----- Invalid Format -----

    def test_wrong_separator(self):
        with self.assertRaises(ValueError):
            convert_date_format("2023/10/15")

    def test_incomplete_date(self):
        with self.assertRaises(ValueError):
            convert_date_format("2023-10")

    def test_invalid_string(self):
        with self.assertRaises(ValueError):
            convert_date_format("invalid-date")

    # ----- Invalid Dates -----

    def test_invalid_month(self):
        with self.assertRaises(ValueError):
            convert_date_format("2023-13-10")

    def test_invalid_day(self):
        with self.assertRaises(ValueError):
            convert_date_format("2023-02-30")

    # ----- Invalid Type -----

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            convert_date_format(20231015)


if __name__ == "__main__":
    unittest.main()
from datetime import datetime


def convert_date_format(date_str):
    if not isinstance(date_str, str):
        raise TypeError("Date must be a string")

    try:
        # Validate and parse the date
        parsed_date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format or invalid date")

    # Convert to required format
    return parsed_date.strftime("%d-%m-%Y")
