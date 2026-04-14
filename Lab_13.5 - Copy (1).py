"""
Comprehensive Refactoring Solutions
Tasks 1-15: Code Refactoring Best Practices
"""

# ============================================================================
# TASK 1: Refactoring - Removing Code Duplication (Rectangle)
# ============================================================================

class Rectangle:
    """
    A class to represent a rectangle and calculate its area and perimeter.
    """
    
    def __init__(self, length, width):
        """
        Initialize rectangle with length and width.
        
        Args:
            length: Length of rectangle
            width: Width of rectangle
        """
        self.length = length
        self.width = width
    
    def area(self):
        """
        Calculate area of rectangle.
        
        Returns:
            Area as length * width
        """
        return self.length * self.width
    
    def perimeter(self):
        """
        Calculate perimeter of rectangle.
        
        Returns:
            Perimeter as 2 * (length + width)
        """
        return 2 * (self.length + self.width)
    
    def display(self):
        """Display area and perimeter of rectangle."""
        print(f"Area of Rectangle: {self.area()}")
        print(f"Perimeter of Rectangle: {self.perimeter()}")


# Task 1 Usage
rectangles = [(5, 10), (7, 12), (10, 15)]
for length, width in rectangles:
    rect = Rectangle(length, width)
    rect.display()


# ============================================================================
# TASK 2: Refactoring - Extracting Reusable Functions (Price Calculation)
# ============================================================================

def calculate_total(price, tax_rate=0.18):
    """
    Calculate total price including tax.
    
    Args:
        price: Original price before tax
        tax_rate: Tax rate as decimal (default 0.18 for 18%)
    
    Returns:
        Total price after tax
    """
    tax = price * tax_rate
    return price + tax


# Task 2 Usage
prices = [250, 500]
for price in prices:
    total = calculate_total(price)
    print(f"Total Price: {total}")


# ============================================================================
# TASK 3: Refactoring Using Classes (Grade Calculator)
# ============================================================================

class GradeCalculator:
    """
    A class to calculate student grades based on marks.
    """
    
    def calculate_grade(self, marks):
        """
        Calculate grade based on marks using predefined criteria.
        
        Args:
            marks: Student marks (0-100)
        
        Returns:
            Grade as string (Grade A, B, C, D, or Fail)
        """
        if marks >= 90:
            return "Grade A"
        elif marks >= 80:
            return "Grade B"
        elif marks >= 70:
            return "Grade C"
        elif marks >= 40:
            return "Grade D"
        else:
            return "Fail"


# Task 3 Usage
calc = GradeCalculator()
student_marks = [85, 72, 95, 35, 65]
for marks in student_marks:
    grade = calc.calculate_grade(marks)
    print(f"Marks: {marks} → {grade}")


# ============================================================================
# TASK 4: Refactoring - Procedural to Functions (Square Calculator)
# ============================================================================

def get_input():
    """
    Get user input for a number.
    
    Returns:
        Integer input from user
    """
    return int(input("Enter number: "))


def calculate_square(num):
    """
    Calculate square of a number.
    
    Args:
        num: Number to square
    
    Returns:
        Square of the number
    """
    return num * num


def display_result(result):
    """
    Display the result.
    
    Args:
        result: Result to display
    """
    print(f"Square: {result}")


# Task 4 Usage (uncomment to run)
# num = get_input()
# square = calculate_square(num)
# display_result(square)


# ============================================================================
# TASK 5: Refactoring - Procedural to OOP (Employee Salary)
# ============================================================================

class EmployeeSalaryCalculator:
    """
    A class to calculate employee salary after tax deduction.
    """
    
    def __init__(self, salary, tax_rate=0.2):
        """
        Initialize employee with salary and tax rate.
        
        Args:
            salary: Gross salary
            tax_rate: Tax rate as decimal (default 0.2 for 20%)
        """
        self.salary = salary
        self.tax_rate = tax_rate
    
    def calculate_tax(self):
        """
        Calculate tax amount.
        
        Returns:
            Tax amount
        """
        return self.salary * self.tax_rate
    
    def calculate_net_salary(self):
        """
        Calculate net salary after tax.
        
        Returns:
            Net salary
        """
        return self.salary - self.calculate_tax()
    
    def display(self):
        """Display salary details."""
        print(f"Gross Salary: {self.salary}")
        print(f"Tax: {self.calculate_tax()}")
        print(f"Net Salary: {self.calculate_net_salary()}")


# Task 5 Usage
emp = EmployeeSalaryCalculator(50000)
emp.display()


# ============================================================================
# TASK 6: Optimizing Search Logic (User Access)
# ============================================================================

def check_access_linear(users, username):
    """
    Check user access using linear search (O(n) complexity).
    
    Args:
        users: List of usernames
        username: Username to search
    
    Returns:
        "Access Granted" or "Access Denied"
    """
    for u in users:
        if u == username:
            return "Access Granted"
    return "Access Denied"


def check_access_set(users, username):
    """
    Check user access using set lookup (O(1) complexity).
    
    Args:
        users: List/set of usernames
        username: Username to search
    
    Returns:
        "Access Granted" or "Access Denied"
    """
    user_set = set(users)
    return "Access Granted" if username in user_set else "Access Denied"


# Task 6 Usage
users = ["admin", "guest", "editor", "viewer"]
# name = input("Enter username: ")
# result = check_access_set(users, name)
# print(result)


# ============================================================================
# TASK 7: Library Management System (Modular)
# ============================================================================

class LibraryManagement:
    """
    A class for managing library books.
    """
    
    def __init__(self):
        """Initialize empty library database."""
        self.library_db = {}
    
    def add_book(self, title, author, isbn):
        """
        Add a book to the library.
        
        Args:
            title: Book title
            author: Book author
            isbn: Book ISBN (unique identifier)
        
        Returns:
            Success message or book already exists message
        """
        if isbn not in self.library_db:
            self.library_db[isbn] = {"title": title, "author": author}
            return "Book added successfully."
        return "Book already exists."
    
    def search_book(self, isbn):
        """
        Search for a book by ISBN.
        
        Args:
            isbn: Book ISBN to search
        
        Returns:
            Book details or "Book not found"
        """
        if isbn in self.library_db:
            return self.library_db[isbn]
        return "Book not found."
    
    def remove_book(self, isbn):
        """
        Remove a book from the library.
        
        Args:
            isbn: Book ISBN to remove
        
        Returns:
            Success message or book not found message
        """
        if isbn in self.library_db:
            del self.library_db[isbn]
            return "Book removed successfully."
        return "Book not found."


# Task 7 Usage
lib = LibraryManagement()
print(lib.add_book("Python Basics", "John Doe", "101"))
print(lib.add_book("AI Fundamentals", "Jane Smith", "102"))
print(lib.search_book("101"))
print(lib.remove_book("101"))
print(lib.search_book("101"))


# ============================================================================
# TASK 8: Fibonacci Generator
# ============================================================================

def generate_fibonacci(n):
    """
    Generate Fibonacci series up to n terms.
    
    Args:
        n: Number of terms to generate
    
    Returns:
        List of Fibonacci numbers
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series


# Task 8 Usage
# n = int(input("Enter limit: "))
# fib = generate_fibonacci(n)
# print(fib)


# ============================================================================
# TASK 9: Twin Primes Checker
# ============================================================================

def is_prime(n):
    """
    Check if a number is prime.
    
    Args:
        n: Number to check
    
    Returns:
        True if prime, False otherwise
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def is_twin_prime(p1, p2):
    """
    Check if two numbers are twin primes.
    
    Args:
        p1: First number
        p2: Second number
    
    Returns:
        True if both are prime and differ by 2
    """
    return is_prime(p1) and is_prime(p2) and abs(p1 - p2) == 2


def find_twin_primes_in_range(start, end):
    """
    Find all twin primes in a given range.
    
    Args:
        start: Start of range
        end: End of range
    
    Returns:
        List of twin prime pairs
    """
    twins = []
    for i in range(start, end - 1):
        if is_twin_prime(i, i + 2):
            twins.append((i, i + 2))
    return twins


# Task 9 Usage
print(is_twin_prime(11, 13))
print(find_twin_primes_in_range(1, 30))


# ============================================================================
# TASK 10: Chinese Zodiac Program
# ============================================================================

def get_zodiac(year):
    """
    Get Chinese Zodiac sign for a given year.
    
    Args:
        year: Year to calculate zodiac for
    
    Returns:
        Chinese Zodiac sign as string
    """
    zodiac_signs = [
        "Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox",
        "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat"
    ]
    return zodiac_signs[year % 12]


# Task 10 Usage
# year = int(input("Enter a year: "))
# print(f"Zodiac Sign: {get_zodiac(year)}")


# ============================================================================
# TASK 11: Harshad Number Checker
# ============================================================================

def is_harshad(number):
    """
    Check if a number is a Harshad (Niven) number.
    
    A Harshad number is divisible by the sum of its digits.
    
    Args:
        number: Number to check
    
    Returns:
        True if Harshad number, False otherwise
    """
    if number < 0:
        return False
    
    digit_sum = sum(int(digit) for digit in str(number))
    
    if digit_sum == 0:
        return False
    
    return number % digit_sum == 0


# Task 11 Usage
test_numbers = [18, 19, 21, 100, 102]
for num in test_numbers:
    print(f"{num} is Harshad: {is_harshad(num)}")


# ============================================================================
# TASK 12: Factorial Trailing Zeros
# ============================================================================

def count_trailing_zeros(n):
    """
    Count trailing zeros in factorial of n.
    
    Uses optimized approach: count multiples of 5 in n!
    
    Args:
        n: Non-negative integer
    
    Returns:
        Number of trailing zeros in n!
    """
    if n < 0:
        return 0
    
    count = 0
    power_of_5 = 5
    
    while power_of_5 <= n:
        count += n // power_of_5
        power_of_5 *= 5
    
    return count


# Task 12 Usage
# n = int(input("Enter a number: "))
# zeros = count_trailing_zeros(n)
# print(f"Trailing zeros: {zeros}")


# ============================================================================
# TASK 13: Collatz Sequence Generator
# ============================================================================

def generate_collatz_sequence(n):
    """
    Generate Collatz sequence (3n+1 problem) until reaching 1.
    
    Args:
        n: Starting number
    
    Returns:
        List representing Collatz sequence
    """
    if n <= 0:
        return []
    
    sequence = []
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    sequence.append(1)
    return sequence


# Task 13 Usage
print(generate_collatz_sequence(6))


# ============================================================================
# TASK 14: Lucas Number Sequence
# ============================================================================

def generate_lucas_sequence(n):
    """
    Generate Lucas sequence up to n terms.
    
    Lucas sequence: L(0)=2, L(1)=1, L(n)=L(n-1)+L(n-2)
    
    Args:
        n: Number of terms to generate
    
    Returns:
        List of Lucas numbers
    """
    if n <= 0:
        return []
    if n == 1:
        return [2]
    
    lucas = [2, 1]
    for i in range(2, n):
        lucas.append(lucas[-1] + lucas[-2])
    return lucas


# Task 14 Usage
print(generate_lucas_sequence(5))


# ============================================================================
# TASK 15: Vowel & Consonant Counter
# ============================================================================

def count_vowels_consonants(text):
    """
    Count vowels and consonants in a string.
    
    Args:
        text: Input string to analyze
    
    Returns:
        Tuple (vowel_count, consonant_count)
    """
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    
    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    return (vowel_count, consonant_count)


# Task 15 Usage
test_strings = ["hello", "", "aeiou", "Python Programming"]
for text in test_strings:
    vowels, consonants = count_vowels_consonants(text)
    print(f'"{text}" → Vowels: {vowels}, Consonants: {consonants}')