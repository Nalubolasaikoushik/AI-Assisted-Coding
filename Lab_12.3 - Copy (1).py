"""
Lab 12: Algorithms with AI Assistance

This file covers:
1. Sorting student records for placement drive
2. Bubble Sort with AI-style inline comments and complexity analysis
3. Quick Sort and Merge Sort recursive comparison
4. Inventory management search and sort recommendations
5. Real-time stock data sorting and searching

The program prints sample output and simple runtime measurements so it can be
used directly for the lab record.
"""

from __future__ import annotations

from dataclasses import dataclass
from heapq import heappop, heappush
from random import Random
from time import perf_counter
from typing import Callable, Iterable


random_generator = Random(42)


TASK_PROMPTS = {
    "Task_01": (
        "Generate Python code to store student records with name, roll number, "
        "and CGPA, then sort them in descending CGPA order using Quick Sort and "
        "Merge Sort."
    ),
    "Task_02": (
        "Write a Python Bubble Sort implementation and add inline comments "
        "explaining swaps, passes, and the early termination condition."
    ),
    "Task_03": (
        "Complete recursive Quick Sort and Merge Sort functions in Python, add "
        "docstrings, and compare their performance on random, sorted, and "
        "reverse-sorted lists."
    ),
    "Task_04": (
        "Recommend efficient search and sort algorithms for an inventory system "
        "with product ID, name, price, and stock quantity, then implement them "
        "in Python and justify the choices."
    ),
    "Task_05": (
        "Simulate stock price data, sort stocks by percentage gain or loss using "
        "Heap Sort, search stock symbols using a hash map, and compare "
        "performance with Python built-ins."
    ),
}


@dataclass
class StudentRecord:
    name: str
    roll_number: str
    cgpa: float


@dataclass
class Product:
    product_id: int
    name: str
    price: float
    stock_quantity: int


@dataclass
class StockRecord:
    symbol: str
    opening_price: float
    closing_price: float

    @property
    def percentage_change(self) -> float:
        return ((self.closing_price - self.opening_price) / self.opening_price) * 100


def print_heading(title: str) -> None:
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def print_prompt(task_key: str) -> None:
    print(f"Suggested AI Prompt: {TASK_PROMPTS[task_key]}")


# ============================================================
# Task_01: Sorting Student Records for Placement Drive
# Prompt:
# Generate Python code to store student records with name, roll number,
# and CGPA, then sort them in descending CGPA order using Quick Sort
# and Merge Sort.
# ============================================================


def quick_sort_students(records: list[StudentRecord]) -> list[StudentRecord]:
    """Return student records sorted by CGPA in descending order using Quick Sort."""
    if len(records) <= 1:
        return records[:]

    pivot = records[len(records) // 2].cgpa
    higher = [record for record in records if record.cgpa > pivot]
    equal = [record for record in records if record.cgpa == pivot]
    lower = [record for record in records if record.cgpa < pivot]
    return quick_sort_students(higher) + equal + quick_sort_students(lower)


def merge_sort_students(records: list[StudentRecord]) -> list[StudentRecord]:
    """Return student records sorted by CGPA in descending order using Merge Sort."""
    if len(records) <= 1:
        return records[:]

    mid = len(records) // 2
    left_half = merge_sort_students(records[:mid])
    right_half = merge_sort_students(records[mid:])
    return merge_students(left_half, right_half)


def merge_students(
    left_half: list[StudentRecord], right_half: list[StudentRecord]
) -> list[StudentRecord]:
    merged: list[StudentRecord] = []
    left_index = 0
    right_index = 0

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index].cgpa >= right_half[right_index].cgpa:
            merged.append(left_half[left_index])
            left_index += 1
        else:
            merged.append(right_half[right_index])
            right_index += 1

    merged.extend(left_half[left_index:])
    merged.extend(right_half[right_index:])
    return merged


def generate_student_records(count: int) -> list[StudentRecord]:
    records = []
    for index in range(1, count + 1):
        cgpa = round(random_generator.uniform(5.5, 10.0), 2)
        records.append(
            StudentRecord(
                name=f"Student_{index}",
                roll_number=f"SRU{1000 + index}",
                cgpa=cgpa,
            )
        )
    return records


def display_top_students(records: list[StudentRecord], limit: int = 10) -> None:
    print(f"Top {limit} Students by CGPA:")
    for rank, record in enumerate(records[:limit], start=1):
        print(
            f"{rank:>2}. {record.name:<12} "
            f"Roll No: {record.roll_number:<8} CGPA: {record.cgpa:.2f}"
        )


def benchmark_sort(
    sort_function: Callable[[list[StudentRecord]], list[StudentRecord]],
    records: list[StudentRecord],
    runs: int = 3,
) -> float:
    timings = []
    for _ in range(runs):
        copied_records = records[:]
        start_time = perf_counter()
        sort_function(copied_records)
        timings.append(perf_counter() - start_time)
    return sum(timings) / runs


def task_01_demo() -> None:
    print_heading("Task_01: Sorting Student Records for Placement Drive")
    print_prompt("Task_01")

    sample_records = [
        StudentRecord("Asha", "SRU101", 9.10),
        StudentRecord("Rohan", "SRU102", 8.75),
        StudentRecord("Diya", "SRU103", 9.62),
        StudentRecord("Kiran", "SRU104", 8.95),
        StudentRecord("Mehul", "SRU105", 9.45),
    ]

    quick_sorted = quick_sort_students(sample_records)
    merge_sorted = merge_sort_students(sample_records)

    print("Quick Sort Result:")
    for record in quick_sorted:
        print(f"{record.name:<10} {record.roll_number:<8} {record.cgpa:.2f}")

    print("\nMerge Sort Result:")
    for record in merge_sorted:
        print(f"{record.name:<10} {record.roll_number:<8} {record.cgpa:.2f}")

    large_dataset = generate_student_records(4000)
    quick_time = benchmark_sort(quick_sort_students, large_dataset)
    merge_time = benchmark_sort(merge_sort_students, large_dataset)

    print("\nAverage Runtime on 4000 Student Records:")
    print(f"Quick Sort: {quick_time:.6f} seconds")
    print(f"Merge Sort: {merge_time:.6f} seconds")

    best_students = merge_sort_students(large_dataset)
    print()
    display_top_students(best_students, 10)


# ============================================================
# Task_02: Bubble Sort with AI Comments
# Prompt:
# Write a Python Bubble Sort implementation and add inline comments
# explaining swaps, passes, and the early termination condition.
# ============================================================


def bubble_sort(numbers: list[int]) -> list[int]:
    """
    Sort a list in ascending order using Bubble Sort.

    Time Complexity:
    - Best Case: O(n) when the list is already sorted and no swaps happen.
    - Average Case: O(n^2)
    - Worst Case: O(n^2)

    Space Complexity:
    - O(1) because sorting is done in place except for the copied input list.
    """

    values = numbers[:]
    n = len(values)

    # Each outer pass moves the next largest element to the end.
    for pass_number in range(n):
        swapped = False

        # Compare adjacent elements and swap if they are in the wrong order.
        for index in range(0, n - pass_number - 1):
            if values[index] > values[index + 1]:
                values[index], values[index + 1] = values[index + 1], values[index]
                swapped = True

        # If no swaps happened in a full pass, the list is already sorted.
        if not swapped:
            break

    return values


def task_02_demo() -> None:
    print_heading("Task_02: Bubble Sort with AI Comments")
    print_prompt("Task_02")
    numbers = [45, 12, 78, 3, 19, 50]
    print("Original List:", numbers)
    print("Sorted List:  ", bubble_sort(numbers))
    print("\nComplexity Analysis:")
    print("Best Case: O(n)")
    print("Average Case: O(n^2)")
    print("Worst Case: O(n^2)")
    print("Space Complexity: O(1)")


# ============================================================
# Task_03: Quick Sort and Merge Sort Comparison
# Prompt:
# Complete recursive Quick Sort and Merge Sort functions in Python,
# add docstrings, and compare their performance on random, sorted,
# and reverse-sorted lists.
# ============================================================


def quick_sort_recursive(values: list[int]) -> list[int]:
    """Sort integers in ascending order using recursive Quick Sort."""
    if len(values) <= 1:
        return values[:]

    pivot = values[len(values) // 2]
    left = [value for value in values if value < pivot]
    middle = [value for value in values if value == pivot]
    right = [value for value in values if value > pivot]
    return quick_sort_recursive(left) + middle + quick_sort_recursive(right)


def merge_sort_recursive(values: list[int]) -> list[int]:
    """Sort integers in ascending order using recursive Merge Sort."""
    if len(values) <= 1:
        return values[:]

    mid = len(values) // 2
    left = merge_sort_recursive(values[:mid])
    right = merge_sort_recursive(values[mid:])
    return merge_numbers(left, right)


def merge_numbers(left: list[int], right: list[int]) -> list[int]:
    merged: list[int] = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged


def benchmark_integer_sort(
    sort_function: Callable[[list[int]], list[int]],
    values: list[int],
    runs: int = 3,
) -> float:
    timings = []
    for _ in range(runs):
        start_time = perf_counter()
        sort_function(values[:])
        timings.append(perf_counter() - start_time)
    return sum(timings) / runs


def task_03_demo() -> None:
    print_heading("Task_03: Quick Sort and Merge Sort Comparison")
    print_prompt("Task_03")

    random_list = [random_generator.randint(1, 1000) for _ in range(2000)]
    sorted_list = list(range(1, 2001))
    reverse_sorted_list = list(range(2000, 0, -1))

    datasets = {
        "Random List": random_list,
        "Sorted List": sorted_list,
        "Reverse-Sorted List": reverse_sorted_list,
    }

    for label, dataset in datasets.items():
        quick_time = benchmark_integer_sort(quick_sort_recursive, dataset)
        merge_time = benchmark_integer_sort(merge_sort_recursive, dataset)
        print(f"{label}:")
        print(f"  Quick Sort Time: {quick_time:.6f} seconds")
        print(f"  Merge Sort Time: {merge_time:.6f} seconds")

    print("\nComplexity Summary:")
    print("Quick Sort -> Best: O(n log n), Average: O(n log n), Worst: O(n^2)")
    print("Merge Sort -> Best: O(n log n), Average: O(n log n), Worst: O(n log n)")


# ============================================================
# Task_04: Inventory Management System
# Prompt:
# Recommend efficient search and sort algorithms for an inventory system
# with product ID, name, price, and stock quantity, then implement them
# in Python and justify the choices.
# ============================================================


def build_inventory_indexes(products: Iterable[Product]) -> tuple[dict[int, Product], dict[str, Product]]:
    id_index = {}
    name_index = {}
    for product in products:
        id_index[product.product_id] = product
        name_index[product.name.lower()] = product
    return id_index, name_index


def search_product_by_id(product_index: dict[int, Product], product_id: int) -> Product | None:
    return product_index.get(product_id)


def search_product_by_name(name_index: dict[str, Product], name: str) -> Product | None:
    return name_index.get(name.lower())


def merge_sort_products_by_price(products: list[Product]) -> list[Product]:
    if len(products) <= 1:
        return products[:]

    mid = len(products) // 2
    left = merge_sort_products_by_price(products[:mid])
    right = merge_sort_products_by_price(products[mid:])
    merged: list[Product] = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index].price <= right[right_index].price:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged


def quick_sort_products_by_quantity(products: list[Product]) -> list[Product]:
    if len(products) <= 1:
        return products[:]

    pivot = products[len(products) // 2].stock_quantity
    lower = [product for product in products if product.stock_quantity < pivot]
    equal = [product for product in products if product.stock_quantity == pivot]
    higher = [product for product in products if product.stock_quantity > pivot]
    return quick_sort_products_by_quantity(lower) + equal + quick_sort_products_by_quantity(higher)


def task_04_demo() -> None:
    print_heading("Task_04: Real-Time Application - Inventory Management System")
    print_prompt("Task_04")

    inventory = [
        Product(101, "Keyboard", 899.0, 40),
        Product(102, "Mouse", 499.0, 75),
        Product(103, "Monitor", 12499.0, 12),
        Product(104, "USB Hub", 699.0, 55),
        Product(105, "Webcam", 2399.0, 18),
    ]

    print("Recommended Algorithms Table:")
    print("-" * 70)
    print(f"{'Operation':<20}{'Algorithm':<20}{'Justification'}")
    print("-" * 70)
    print(
        f"{'Search by ID':<20}{'Hash Map':<20}"
        "O(1) average lookup for large, frequently queried datasets"
    )
    print(
        f"{'Search by Name':<20}{'Hash Map':<20}"
        "Case-insensitive dictionary lookup is fast and practical"
    )
    print(
        f"{'Sort by Price':<20}{'Merge Sort':<20}"
        "Stable O(n log n) behavior for analytical reports"
    )
    print(
        f"{'Sort by Quantity':<20}{'Quick Sort':<20}"
        "Fast average performance for in-memory stock views"
    )

    id_index, name_index = build_inventory_indexes(inventory)
    print("\nSearch Results:")
    print("Product ID 103 ->", search_product_by_id(id_index, 103))
    print("Product Name 'mouse' ->", search_product_by_name(name_index, "mouse"))

    print("\nProducts Sorted by Price:")
    for product in merge_sort_products_by_price(inventory):
        print(product)

    print("\nProducts Sorted by Quantity:")
    for product in quick_sort_products_by_quantity(inventory):
        print(product)


# ============================================================
# Task_05: Real-Time Stock Data Sorting and Searching
# Prompt:
# Simulate stock price data, sort stocks by percentage gain or loss using
# Heap Sort, search stock symbols using a hash map, and compare
# performance with Python built-ins.
# ============================================================


def generate_stock_data(count: int) -> list[StockRecord]:
    records = []
    for index in range(count):
        symbol = f"STK{index + 1:03d}"
        opening_price = round(random_generator.uniform(80, 1500), 2)
        daily_move = random_generator.uniform(-0.15, 0.15)
        closing_price = round(opening_price * (1 + daily_move), 2)
        records.append(StockRecord(symbol, opening_price, closing_price))
    return records


def heap_sort_stocks_by_change(records: list[StockRecord]) -> list[StockRecord]:
    heap = []
    for record in records:
        heappush(heap, (-record.percentage_change, record.symbol, record))

    sorted_records = []
    while heap:
        _, _, record = heappop(heap)
        sorted_records.append(record)
    return sorted_records


def build_stock_index(records: Iterable[StockRecord]) -> dict[str, StockRecord]:
    return {record.symbol: record for record in records}


def search_stock(stock_index: dict[str, StockRecord], symbol: str) -> StockRecord | None:
    return stock_index.get(symbol.upper())


def benchmark_stock_sort(
    sort_function: Callable[[list[StockRecord]], list[StockRecord]],
    records: list[StockRecord],
    runs: int = 3,
) -> float:
    timings = []
    for _ in range(runs):
        start_time = perf_counter()
        sort_function(records[:])
        timings.append(perf_counter() - start_time)
    return sum(timings) / runs


def benchmark_stock_lookup(
    lookup_function: Callable[[str], StockRecord | None],
    symbols: list[str],
    runs: int = 1000,
) -> float:
    start_time = perf_counter()
    for index in range(runs):
        lookup_function(symbols[index % len(symbols)])
    return perf_counter() - start_time


def task_05_demo() -> None:
    print_heading("Task_05: Real-Time Stock Data Sorting and Searching")
    print_prompt("Task_05")

    stocks = generate_stock_data(3000)
    stock_index = build_stock_index(stocks)

    heap_time = benchmark_stock_sort(heap_sort_stocks_by_change, stocks)
    built_in_time = benchmark_stock_sort(
        lambda data: sorted(data, key=lambda record: record.percentage_change, reverse=True),
        stocks,
    )

    symbols_to_lookup = [stocks[0].symbol, stocks[1499].symbol, stocks[-1].symbol]
    dict_lookup_time = benchmark_stock_lookup(
        lambda symbol: search_stock(stock_index, symbol),
        symbols_to_lookup,
    )
    linear_lookup_time = benchmark_stock_lookup(
        lambda symbol: next((record for record in stocks if record.symbol == symbol), None),
        symbols_to_lookup,
    )

    ranked_stocks = heap_sort_stocks_by_change(stocks)
    print("Top 10 Stocks by Percentage Gain/Loss:")
    for rank, stock in enumerate(ranked_stocks[:10], start=1):
        print(
            f"{rank:>2}. {stock.symbol:<8} Open: {stock.opening_price:>8.2f} "
            f"Close: {stock.closing_price:>8.2f} Change: {stock.percentage_change:>7.2f}%"
        )

    print("\nSample Stock Search:")
    print(search_stock(stock_index, symbols_to_lookup[1]))

    print("\nPerformance Comparison:")
    print(f"Heap Sort Time:           {heap_time:.6f} seconds")
    print(f"Python sorted() Time:     {built_in_time:.6f} seconds")
    print(f"Hash Map Lookup Time:     {dict_lookup_time:.6f} seconds")
    print(f"Linear Search Lookup Time:{linear_lookup_time:.6f} seconds")

    print("\nTrade-Off Analysis:")
    print("Heap Sort is useful when repeated top-k extraction is required.")
    print("Python sorted() is usually simpler and highly optimized in practice.")
    print("Hash maps are the best choice for instant stock symbol lookup.")


def main() -> None:
    task_01_demo()
    task_02_demo()
    task_03_demo()
    task_04_demo()
    task_05_demo()


if __name__ == "__main__":
    main()
