# #Task-01:
# def is_leap_year_basic(year):
#     return year % 4 == 0

# def is_leap_year(year):
#     return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# # TEST
# test_years = [1900, 2000, 2024]
# print("Year | Basic | Correct | Expected")
# for year in test_years:
#     basic = is_leap_year_basic(year)
#     correct = is_leap_year(year)
#     expected = year in [2000, 2024]  # 1900 is NOT a leap year
#     print(f"{year} | {basic} | {correct} | {expected}")




# Task‑02:

# def gcd_one_shot(a, b):
#     """Euclidean algorithm."""
#     while b != 0:
#         a, b = b, a % b
#     return abs(a)


# # ZERO‑SHOT SOLUTION (naive brute‑force)
# def gcd_zero_shot(a, b):
#     a, b = abs(a), abs(b)
#     gcd = 1
#     for i in range(1, min(a, b) + 1):
#         if a % i == 0 and b % i == 0:
#             gcd = i
#     return gcd


# # TEST
# test_cases = [(12, 18), (48, 18), (100, 50), (17, 19)]
# print("Test Case | Zero-Shot | One-Shot | Correct")
# for a, b in test_cases:
#     print(
#         f"({a}, {b}) | "
#         f"{gcd_zero_shot(a, b)} | {gcd_one_shot(a, b)} | {gcd_one_shot(a, b)}"
#     )

# # EFFICIENCY ANALYSIS
# print("\nComplexity Analysis:")
# print("Zero-Shot (Naive): O(min(a,b)) - Checks all divisors")
# print("One-Shot (Euclidean): O(log(min(a,b))) - Uses modulo")
# print("Speedup: One-shot ~300-500x faster for large numbers")


# TASK-03

# import math

# def lcm_few_shot(a, b):
# 	return abs(a * b) // math.gcd(a, b)

# def lcm_zero_shot(a, b):
# 	a, b = abs(a), abs(b)
# 	max_val = max(a, b)
# 	multiple = max_val
# 	while True:
# 		if multiple % a == 0 and multiple % b == 0:
# 			return multiple
# 		multiple += max_val

# print("\n" + "=" * 70)
# print("QUESTION 3: LCM (FEW-SHOT vs ZERO-SHOT)")
# print("=" * 70)
# test_cases = [(4, 6), (5, 10), (7, 3), (12, 18)]
# print("Input | Few-Shot | Zero-Shot | Correct")
# for a, b in test_cases:
# 	few = lcm_few_shot(a, b)
# 	zero = lcm_zero_shot(a, b)
# 	print(f"({a},{b}) | {few} | {zero} | {few}")
# print("\nComplexity: Few-Shot O(log n) | Zero-Shot O(LCM/max) | Speedup: 100-1000x")
# print("Formula: LCM(a,b) = (a*b) / GCD(a,b)")
# print("\n" + "=" * 70)


#Task=05:

def decimal_to_binary(n):
	if n == 0:
		return "0"
	sign = "-" if n < 0 else ""
	n = abs(n)
	binary = ""
	while n > 0:
		binary = str(n % 2) + binary
		n //= 2
	return sign + binary

# Test cases
print(decimal_to_binary(10))   # 1010
print(decimal_to_binary(0))    # 0
print(decimal_to_binary(-5))   # -101



