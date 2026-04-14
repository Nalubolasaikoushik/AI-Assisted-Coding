# #TASK-01:
# class Student:
    
#     def __init__(self, name, roll_number, branch):
#         self.name = name
#         self.roll_number = roll_number
#         self.branch = branch
    
#     def display_details(self):
#         print("Student Details:")
#         print("Name:", self.name)
#         print("Roll Number:", self.roll_number)
#         print("Branch:", self.branch)


# # Example usage
# student1 = Student("Syed Althaf", "CSE2023A01", "CSE-AIML")
# student1.display_details()

#TASK-02:
# def print_multiples(number):
#     for i in range(1, 11):
#         print(f"{number} x {i} = {number * i}")


# # Example usage
# print_multiples(5)

# def print_multiples(number):
#     i = 1
#     while i <= 10:
#         print(f"{number} x {i} = {number * i}")
#         i += 1


# # Example usage
# print_multiples(7)

#TASK-03:
# def classify_age(age):
#     if age < 0:
#         return "Invalid age"
#     elif age <= 12:
#         return "Child"
#     elif age <= 19:
#         return "Teenager"
#     elif age <= 59:
#         return "Adult"
#     else:
#         return "Senior"


# # Example usage
# print(classify_age(10))
# print(classify_age(16))
# print(classify_age(30))
# print(classify_age(65))

# def classify_age(age):
#     age_groups = {
#         "Child": range(0, 13),
#         "Teen": range(13, 20),
#         "Adult": range(20, 60),
#         "Senior": range(60, 150)
#     }
    
#     for category, age_range in age_groups.items():
#         if age in age_range:
#             return category

# # Example
# print(classify_age(25))   # Adult
# print(classify_age(10))   # Child


#TASK-04:
# def sum_to_n(n):
#     total = 0
#     for i in range(1, n + 1):
#         total += i
#     return total
# print(sum_to_n(5))   # Output: 15

# def sum_to_n(n):
#     total = 0
#     i = 1
    
#     while i <= n:
#         total += i
#         i += 1
        
#     return total
# print(sum_to_n(5))   # Output: 15

#TASK-05:
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ₹{amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrawn: ₹{amount}")

    def display_balance(self):
        print(f"Current Balance: ₹{self.balance}")


account = BankAccount("Syed Althaf", 1000)
account.display_balance()
account.deposit(500)
account.withdraw(300)
account.display_balance()
