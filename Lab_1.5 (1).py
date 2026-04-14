# TASK_1

# # String Reversal Without Functions
# user_input = input("Enter a string to reverse: ")

# # Reverse the string using slicing
# reversed_string = user_input[::-1]

# # Display the result
# print(f"Original string: {user_input}")
# print(f"Reversed string: {reversed_string}")


# #TASK-2:
# # String Reversal - Optimized
# user_input = input("Enter a string to reverse: ")
# print(f"Original string: {user_input}")
# print(f"Reversed string: {user_input[::-1]}")



# #Task-3:
# def reverse_string(s):
# 	"""
# 	Reverse a string using slicing.
# 	Args:
# 		s (str): The string to reverse
# 	Returns:
# 		str: The reversed string
# 	"""
# 	return s[::-1]
# # Test cases
# print("\n--- Function Test Cases ---")
# test_cases = ["hello", "python", "a", "", "12345"]
# for test in test_cases:
# 	result = reverse_string(test)
# 	print(f"Input: '{test}' -> Output: '{result}'")
	
# #Task-4:
# # Comparison: Procedural vs Function-based String Reversal
# print("\n--- COMPARISON ANALYSIS ---\n")
# # PROCEDURAL APPROACH
# print("1. PROCEDURAL APPROACH:")
# print(" Clarity: Code is straightforward but scattered")
# print(" Reusability: Must rewrite logic each time")
# print(" Debugging: Harder to isolate and fix issues")
# print(" Scalability: Difficult to extend with new features")
# string = input("Enter a string: ")
# reversed_string = ""
# for i in range(len(string) - 1, -1, -1):
# 	reversed_string += string[i]
# print(f"Reversed: {reversed_string}\n")
# # FUNCTION-BASED APPROACH
# def reverse_string(s):
# 	"""Reverse a string using slicing."""
# 	return s[::-1]

# print("2. FUNCTION-BASED APPROACH:")
# print(" Clarity: Logic encapsulated, self-documenting")
# print(" Reusability: Call function anywhere, anytime")
# print(" Debugging: Test and fix in one location")
# print(" Scalability: Easy to add validation, logging, etc.\n")
# string = input("Enter a string: ")
# print(f"Reversed: {reverse_string(string)}\n")
# # VERDICT
# print("RECOMMENDATION: Use function-based approach for production code")
# print("- Better code organization")
# print("- Easier unit testing")
# print("- Improved maintainability")



#Task -5:
# BONUS: Side-by-side comparison of both methods
print("\n--- METHOD COMPARISON ---\n")
test_string = input("Enter a string for method comparison: ")
# Loop-based approach
reversed_loop = ""
for i in range(len(test_string) - 1, -1, -1):
	reversed_loop += test_string[i]
# Slicing-based approach
reversed_slice = test_string[::-1]
print(f"Original string: '{test_string}'")
print(f"Loop-based result: '{reversed_loop}'")
print(f"Slicing-based result: '{reversed_slice}'")
print(f"Both methods match: {reversed_loop == reversed_slice}")




