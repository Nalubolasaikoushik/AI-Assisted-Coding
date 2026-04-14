# #TASK-01:
# # Basic prime-checking method
# def is_prime_basic(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
# # Optimized prime-checking method
# def is_prime_optimized(n):
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True
# # Example usage
# number = 29
# print(f"Basic method: Is {number} prime? {is_prime_basic(number)}")
# print(f"Optimized method: Is {number} prime? {is_prime_optimized(number)}")
# # Explanation of performance improvement
# # The optimized version improves performance by reducing the number of checks needed to

# # It eliminates even numbers and multiples of 3 right away, and only checks for factors up
# # to the square root of n, which significantly decreases the number of iterations for larger


# #TASK-02:
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)


# num = 6
# print(f"Fibonacci number at position {num} is:", fibonacci(num))

#TASK-03:
# def process_file(filename):
#     try:
#         with open(filename, 'r') as file:
#             numbers = []

#             for line in file:
#                 line = line.strip()

#                 if line == "":
#                     continue

#                 number = float(line)
#                 numbers.append(number)

#         if len(numbers) == 0:
#             print("The file contains no valid numeric data.")
#             return

#         average = sum(numbers) / len(numbers)
#         print("Numbers read from file:", numbers)
#         print("Average:", average)

#     except FileNotFoundError:
#         print("Error: The file was not found. Please check the filename.")

#     except ValueError:
#         print("Error: The file contains invalid (non-numeric) data.")

#     except Exception as e:
#         print("Unexpected error occurred:", e)


# process_file("data.txt")

#TASK-04:
# Insecure login system (for demonstration)

# stored_username = "admin"
# stored_password = "admin123"   # Plain-text password (NOT secure)

# username = input("Enter username: ")
# password = input("Enter password: ")

# if username == stored_username and password == stored_password:
#     print("Login successful!")
# else:
#     print("Invalid credentials.")


#TASK-05:
import datetime

def log_user_activity(username, email, action):
    with open("activity.log", "a") as log_file:
        timestamp = datetime.datetime.now()
        log_file.write(f"{timestamp} | USER: {username} | EMAIL: {email} | ACTION: {action}\n")

# Example usage
log_user_activity("john_doe", "john@example.com", "Logged in")
