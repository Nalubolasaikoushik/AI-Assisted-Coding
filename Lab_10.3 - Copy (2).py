# #Problem-1:
# """
# Calculate the factorial of a non-negative integer.
# Args:
#     n (int): A non-negative integer for which to calculate the factorial.
# Returns:
#     int: The factorial of n (n!), which is the product of all positive 
#          integers less than or equal to n.
# Example:
#     >>> factorial(5)
#     120
#     >>> factorial(0)
#     1
# Note:
#     This function uses iterative multiplication to compute the factorial.
#     For n=0, it returns 1 by definition.
# """
# def factorial(n):
#     result = 1
#     for i in range(1, n):
#         result = result * i
#     return result
# print(factorial(5))
# #corrected code:
# #Review and improve code quality using AI tools.
# #Identify syntax, logic, and performance issues in code.
# #Refactor code to improve readability and maintainability.
# #Compare AI outputs generated using different prompting techniques.

# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result = result * i
#     return result
# print(factorial(5))

#Question2:
def calc(a, b, c):
    if c == "add":
        return a + b
    elif c == "sub":
        return a - b
    elif c == "mul":
        return a * b
    elif c == "div":
        return a / b
print(calc(10, 5, "add"))
print(calc(10, 5, "sub"))

#AI improved code:
def perform_calculation(number1, number2, operation):
    """
    Perform a basic arithmetic operation on two numbers.

    Parameters:
    number1 (int or float): The first numeric operand.
    number2 (int or float): The second numeric operand.
    operation (str): The arithmetic operation to perform.
                     Supported values:
                     - "add" : Addition
                     - "sub" : Subtraction
                     - "mul" : Multiplication
                     - "div" : Division

    Returns:
    float or int: Result of the arithmetic operation.

    Raises:
    TypeError: If inputs are not valid types.
    ValueError: If operation is unsupported.
    ZeroDivisionError: If division by zero is attempted.

    Examples:
    >>> perform_calculation(10, 5, "add")
    15
    >>> perform_calculation(10, 5, "div")
    2.0
    """

    # Input validation for numbers
    if not isinstance(number1, (int, float)) or not isinstance(number2, (int, float)):
        raise TypeError("Both number1 and number2 must be int or float.")

    # Input validation for operation
    if not isinstance(operation, str):
        raise TypeError("Operation must be a string.")

    operation = operation.lower()

    if operation == "add":
        return number1 + number2
    elif operation == "sub":
        return number1 - number2
    elif operation == "mul":
        return number1 * number2
    elif operation == "div":
        if number2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return number1 / number2
    else:
        raise ValueError(f"Unsupported operation: {operation}")
print(perform_calculation(10, 5, "add"))
print(perform_calculation(10, 5, "sub"))

#Question -3:
def Checkprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

#PEP8 compliant version
#List all PEP8 violations. Refactor the code (function name, spacing, indentation, naming) to be PEP8 compliant.

def check_prime(n):
    """
    Check if a number is prime.

    Parameters:
        n (int): The number to check.
    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


#task 4 (AI as a Code Reviewer in Real Projects)
#scenrio : In a GitHub project, a teammate submits:

def processData(d):
    return [x * 2 for x in d if x % 2 == 0]

#Make sure to follow the abelow instructions and suggest the code changes:

'''
#instrucations for code review:
Manually review the function for:
o Readability and naming.
o Reusability and modularity.
o Edge cases (non-list input, empty list, non-integer
elements).
2. Use AI to generate a code review covering:
a. Better naming and function purpose clarity.
b. Input validation and type hints.
c. Suggestions for generalization (e.g., configurable
multiplier).
3. Refactor the function based on AI feedback.
4. Write a short reflection on whether AI should be a
standalone reviewer or an assistant.
'''

def process_data(data: list[int]) -> list[int]:
    """
    Process a list of integers by doubling the even numbers.

    Parameters:
        data (list[int]): A list of integers to process.

    Returns:
        list[int]: A new list containing the doubled values of the even numbers from the input list.

    Raises:
        ValueError: If the input is not a list or contains non-integer elements.
    """
    if not isinstance(data, list):
        raise ValueError("Input must be a list.")
    if any(not isinstance(x, int) for x in data):
        raise ValueError("All elements in the input list must be integers.")
    
    return [x * 2 for x in data if x % 2 == 0]

