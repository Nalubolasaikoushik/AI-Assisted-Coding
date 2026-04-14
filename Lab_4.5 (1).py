# #TASK-01:

# def is_leap_year(year):
#     """
#     Returns True if the given year is a leap year,
#     otherwise returns False.
#     """
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     else:
#         return False


# # Sample Testing
# year = int(input("Enter a year: "))
# if is_leap_year(year):
#     print("Leap Year")
# else:
#     print("Not a Leap Year")



#TASK-02:
# def cm_to_inches(cm):
#     """
#     Converts centimeters to inches.
#     1 inch = 2.54 centimeters
#     """
#     return cm / 2.54


# # Sample Test Cases
# print("10 cm =", round(cm_to_inches(10), 2), "inches")
# print("25.4 cm =", round(cm_to_inches(25.4), 2), "inches")
# print("50 cm =", round(cm_to_inches(50), 2), "inches")


#TASK-03:
# def format_name(full_name):
#     """
#     Accepts a full name and formats it as 'Last, First'.
    
#     Args:
#         full_name (str): The complete name of a person
        
#     Returns:
#         str: Name formatted as 'Last, First'
#     """
    
#     # Remove leading/trailing spaces and split the name
#     words = full_name.strip().split()
    
#     # Ensure at least two words are present
#     if len(words) < 2:
#         return "Invalid name format"
    
#     # Extract last name
#     last_name = words[-1]
    
#     # Extract first name(s)
#     first_names = " ".join(words[:-1])
    
#     # Return formatted result
#     return f"{last_name}, {first_names}"

#TASK-04:
# def count_vowels(text):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in text:
#         if char in vowels:
#             count += 1
#     return count


#TASK=05:
def count_lines(filename):
    """
    Reads a .txt file and returns the number of lines.
    
    Args:
        filename (str): Path to the text file
        
    Returns:
        int: Total number of lines in the file
    """
    try:
        with open(filename, 'r') as file:
            return sum(1 for _ in file)
    except FileNotFoundError:
        return "File not found"
# Sample Testing
filename = input("Enter the filename (with .txt extension): ")


