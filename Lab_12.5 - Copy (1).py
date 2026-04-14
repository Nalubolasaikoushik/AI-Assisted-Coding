"""
Lab 12.5: Algorithms with AI Assistance - Sorting, Searching, and
Optimizing Algorithms

This file contains structured solutions for:
Task_01: Merge Sort implementation
Task_02: Binary Search with AI optimization
Task_03: Smart Healthcare Appointment Scheduling System
Task_04: Railway Ticket Reservation System
Task_05: Smart Hostel Room Allocation System
Task_06: Online Movie Streaming Platform
Task_07: Smart Agriculture Crop Monitoring System
Task_08: Airport Flight Management System
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Callable, Iterable


TASK_PROMPTS = {
    "Task_01": (
        "Generate a Python function merge_sort(arr) that sorts a list in "
        "ascending order and include time and space complexity in the docstring."
    ),
    "Task_02": (
        "Create a Python function binary_search(arr, target) that returns the "
        "index of the target in a sorted list or -1 if not found, with "
        "complexity details in the docstring."
    ),
    "Task_03": (
        "Recommend efficient search and sort algorithms for healthcare "
        "appointments and implement search by appointment ID plus sorting by "
        "time and consultation fee."
    ),
    "Task_04": (
        "Recommend efficient search and sort algorithms for railway tickets and "
        "implement search by ticket ID plus sorting by travel date and seat number."
    ),
    "Task_05": (
        "Recommend efficient search and sort algorithms for hostel room "
        "allocation and implement search by student ID plus sorting by room "
        "number and allocation date."
    ),
    "Task_06": (
        "Recommend efficient search and sort algorithms for movie records and "
        "implement search by movie ID plus sorting by rating and release year."
    ),
    "Task_07": (
        "Recommend efficient search and sort algorithms for crop monitoring data "
        "and implement search by crop ID plus sorting by moisture level and "
        "yield estimate."
    ),
    "Task_08": (
        "Recommend efficient search and sort algorithms for flight information "
        "and implement search by flight ID plus sorting by departure time and "
        "arrival time."
    ),
}


def print_heading(title: str) -> None:
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)


def print_prompt(task_key: str) -> None:
    print(f"Suggested AI Prompt: {TASK_PROMPTS[task_key]}")


def parse_date(value: str) -> datetime:
    return datetime.strptime(value, "%Y-%m-%d")


def parse_datetime(value: str) -> datetime:
    return datetime.strptime(value, "%Y-%m-%d %H:%M")


def merge_sort_generic(items: list[Any], key: Callable[[Any], Any]) -> list[Any]:
    if len(items) <= 1:
        return items[:]

    mid = len(items) // 2
    left = merge_sort_generic(items[:mid], key)
    right = merge_sort_generic(items[mid:], key)
    merged: list[Any] = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if key(left[left_index]) <= key(right[right_index]):
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged


def build_index(records: Iterable[Any], key_name: str) -> dict[Any, Any]:
    return {getattr(record, key_name): record for record in records}


# ============================================================
# Task_01: Merge Sort Implementation
# Prompt:
# Generate a Python function merge_sort(arr) that sorts a list in
# ascending order and include time and space complexity in the docstring.
# ============================================================


def merge_sort(arr: list[int]) -> list[int]:
    """
    Sort a list of integers in ascending order using Merge Sort.

    Time Complexity:
    - Best Case: O(n log n)
    - Average Case: O(n log n)
    - Worst Case: O(n log n)

    Space Complexity:
    - O(n) due to auxiliary arrays created during merging.
    """
    return merge_sort_generic(arr, key=lambda value: value)


def task_01_demo() -> None:
    print_heading("Task_01: Merge Sort Implementation")
    print_prompt("Task_01")
    test_cases = [
        [38, 27, 43, 3, 9, 82, 10],
        [5, 1, 4, 2, 8],
        [1],
        [],
    ]
    for case in test_cases:
        print(f"Input: {case} -> Sorted: {merge_sort(case)}")


# ============================================================
# Task_02: Binary Search with AI Optimization
# Prompt:
# Create a Python function binary_search(arr, target) that returns the
# index of the target in a sorted list or -1 if not found, with
# complexity details in the docstring.
# ============================================================


def binary_search(arr: list[int], target: int) -> int:
    """
    Search for a target value in a sorted list using Binary Search.

    Time Complexity:
    - Best Case: O(1) when the middle element is the target
    - Average Case: O(log n)
    - Worst Case: O(log n)

    Space Complexity:
    - O(1) for the iterative implementation.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2

        # Compare the middle element first to reduce the search interval by half.
        if arr[middle] == target:
            return middle
        if arr[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


def task_02_demo() -> None:
    print_heading("Task_02: Binary Search with AI Optimization")
    print_prompt("Task_02")
    values = [2, 5, 8, 12, 16, 23, 38, 56, 72]
    targets = [23, 2, 72, 9]
    print("Sorted List:", values)
    for target in targets:
        print(f"Target {target} -> Index {binary_search(values, target)}")


# ============================================================
# Task_03: Smart Healthcare Appointment Scheduling System
# Prompt:
# Recommend efficient search and sort algorithms for healthcare
# appointments and implement search by appointment ID plus sorting by
# time and consultation fee.
# ============================================================


@dataclass
class Appointment:
    appointment_id: int
    patient_name: str
    doctor_name: str
    appointment_time: str
    consultation_fee: float


def sort_appointments_by_time(records: list[Appointment]) -> list[Appointment]:
    return merge_sort_generic(records, key=lambda record: parse_datetime(record.appointment_time))


def sort_appointments_by_fee(records: list[Appointment]) -> list[Appointment]:
    return merge_sort_generic(records, key=lambda record: record.consultation_fee)


def task_03_demo() -> None:
    print_heading("Task_03: Smart Healthcare Appointment Scheduling System")
    print_prompt("Task_03")
    print("Recommended search: Hash Map for O(1) average appointment ID lookup")
    print("Recommended sort: Merge Sort for stable O(n log n) ordering")

    appointments = [
        Appointment(201, "Asha", "Dr. Rao", "2026-03-20 10:30", 600.0),
        Appointment(202, "Rohan", "Dr. Mehta", "2026-03-20 09:15", 850.0),
        Appointment(203, "Diya", "Dr. Rao", "2026-03-20 11:00", 500.0),
    ]
    appointment_index = build_index(appointments, "appointment_id")

    print("\nSearch Result for Appointment ID 202:")
    print(appointment_index.get(202))

    print("\nSorted by Appointment Time:")
    for record in sort_appointments_by_time(appointments):
        print(record)

    print("\nSorted by Consultation Fee:")
    for record in sort_appointments_by_fee(appointments):
        print(record)


# ============================================================
# Task_04: Railway Ticket Reservation System
# Prompt:
# Recommend efficient search and sort algorithms for railway tickets and
# implement search by ticket ID plus sorting by travel date and seat number.
# ============================================================


@dataclass
class RailwayTicket:
    ticket_id: int
    passenger_name: str
    train_number: str
    seat_number: int
    travel_date: str


def sort_tickets_by_travel_date(records: list[RailwayTicket]) -> list[RailwayTicket]:
    return merge_sort_generic(records, key=lambda record: parse_date(record.travel_date))


def sort_tickets_by_seat_number(records: list[RailwayTicket]) -> list[RailwayTicket]:
    return merge_sort_generic(records, key=lambda record: record.seat_number)


def task_04_demo() -> None:
    print_heading("Task_04: Railway Ticket Reservation System")
    print_prompt("Task_04")
    print("Recommended search: Hash Map because ticket ID queries are direct")
    print("Recommended sort: Merge Sort for predictable O(n log n) performance")

    tickets = [
        RailwayTicket(301, "Isha", "12701", 42, "2026-04-10"),
        RailwayTicket(302, "Karthik", "12618", 15, "2026-03-28"),
        RailwayTicket(303, "Meena", "12861", 27, "2026-04-02"),
    ]
    ticket_index = build_index(tickets, "ticket_id")

    print("\nSearch Result for Ticket ID 303:")
    print(ticket_index.get(303))

    print("\nSorted by Travel Date:")
    for record in sort_tickets_by_travel_date(tickets):
        print(record)

    print("\nSorted by Seat Number:")
    for record in sort_tickets_by_seat_number(tickets):
        print(record)


# ============================================================
# Task_05: Smart Hostel Room Allocation System
# Prompt:
# Recommend efficient search and sort algorithms for hostel room
# allocation and implement search by student ID plus sorting by room
# number and allocation date.
# ============================================================


@dataclass
class HostelAllocation:
    student_id: str
    room_number: int
    floor: int
    allocation_date: str


def sort_allocations_by_room(records: list[HostelAllocation]) -> list[HostelAllocation]:
    return merge_sort_generic(records, key=lambda record: record.room_number)


def sort_allocations_by_date(records: list[HostelAllocation]) -> list[HostelAllocation]:
    return merge_sort_generic(records, key=lambda record: parse_date(record.allocation_date))


def task_05_demo() -> None:
    print_heading("Task_05: Smart Hostel Room Allocation System")
    print_prompt("Task_05")
    print("Recommended search: Hash Map for constant average-time student ID lookup")
    print("Recommended sort: Merge Sort for clean multi-record reporting")

    allocations = [
        HostelAllocation("STU501", 212, 2, "2026-06-12"),
        HostelAllocation("STU502", 108, 1, "2026-06-05"),
        HostelAllocation("STU503", 315, 3, "2026-06-09"),
    ]
    allocation_index = build_index(allocations, "student_id")

    print("\nSearch Result for Student ID STU502:")
    print(allocation_index.get("STU502"))

    print("\nSorted by Room Number:")
    for record in sort_allocations_by_room(allocations):
        print(record)

    print("\nSorted by Allocation Date:")
    for record in sort_allocations_by_date(allocations):
        print(record)


# ============================================================
# Task_06: Online Movie Streaming Platform
# Prompt:
# Recommend efficient search and sort algorithms for movie records and
# implement search by movie ID plus sorting by rating and release year.
# ============================================================


@dataclass
class Movie:
    movie_id: int
    title: str
    genre: str
    rating: float
    release_year: int


def sort_movies_by_rating(records: list[Movie]) -> list[Movie]:
    return merge_sort_generic(records, key=lambda record: record.rating)


def sort_movies_by_release_year(records: list[Movie]) -> list[Movie]:
    return merge_sort_generic(records, key=lambda record: record.release_year)


def task_06_demo() -> None:
    print_heading("Task_06: Online Movie Streaming Platform")
    print_prompt("Task_06")
    print("Recommended search: Hash Map for quick movie ID access")
    print("Recommended sort: Merge Sort for stable O(n log n) catalog ordering")

    movies = [
        Movie(401, "The Orbit", "Sci-Fi", 8.6, 2023),
        Movie(402, "Silent River", "Drama", 7.9, 2021),
        Movie(403, "Sky Hunters", "Action", 8.2, 2024),
    ]
    movie_index = build_index(movies, "movie_id")

    print("\nSearch Result for Movie ID 401:")
    print(movie_index.get(401))

    print("\nSorted by Rating:")
    for record in sort_movies_by_rating(movies):
        print(record)

    print("\nSorted by Release Year:")
    for record in sort_movies_by_release_year(movies):
        print(record)


# ============================================================
# Task_07: Smart Agriculture Crop Monitoring System
# Prompt:
# Recommend efficient search and sort algorithms for crop monitoring data
# and implement search by crop ID plus sorting by moisture level and
# yield estimate.
# ============================================================


@dataclass
class CropRecord:
    crop_id: int
    crop_name: str
    soil_moisture_level: float
    temperature: float
    yield_estimate: float


def sort_crops_by_moisture(records: list[CropRecord]) -> list[CropRecord]:
    return merge_sort_generic(records, key=lambda record: record.soil_moisture_level)


def sort_crops_by_yield(records: list[CropRecord]) -> list[CropRecord]:
    return merge_sort_generic(records, key=lambda record: record.yield_estimate)


def task_07_demo() -> None:
    print_heading("Task_07: Smart Agriculture Crop Monitoring System")
    print_prompt("Task_07")
    print("Recommended search: Hash Map for direct crop ID lookup")
    print("Recommended sort: Merge Sort for reliable analytics-oriented sorting")

    crops = [
        CropRecord(501, "Rice", 68.5, 30.2, 4.8),
        CropRecord(502, "Wheat", 52.1, 27.4, 3.9),
        CropRecord(503, "Maize", 61.0, 29.1, 4.2),
    ]
    crop_index = build_index(crops, "crop_id")

    print("\nSearch Result for Crop ID 503:")
    print(crop_index.get(503))

    print("\nSorted by Soil Moisture Level:")
    for record in sort_crops_by_moisture(crops):
        print(record)

    print("\nSorted by Yield Estimate:")
    for record in sort_crops_by_yield(crops):
        print(record)


# ============================================================
# Task_08: Airport Flight Management System
# Prompt:
# Recommend efficient search and sort algorithms for flight information
# and implement search by flight ID plus sorting by departure time and
# arrival time.
# ============================================================


@dataclass
class Flight:
    flight_id: str
    airline_name: str
    departure_time: str
    arrival_time: str
    status: str


def sort_flights_by_departure(records: list[Flight]) -> list[Flight]:
    return merge_sort_generic(records, key=lambda record: parse_datetime(record.departure_time))


def sort_flights_by_arrival(records: list[Flight]) -> list[Flight]:
    return merge_sort_generic(records, key=lambda record: parse_datetime(record.arrival_time))


def task_08_demo() -> None:
    print_heading("Task_08: Airport Flight Management System")
    print_prompt("Task_08")
    print("Recommended search: Hash Map for instant flight ID lookup")
    print("Recommended sort: Merge Sort for stable schedule ordering")

    flights = [
        Flight("AI201", "Air India", "2026-05-10 08:30", "2026-05-10 10:45", "On Time"),
        Flight("6E402", "IndiGo", "2026-05-10 06:50", "2026-05-10 09:00", "Boarding"),
        Flight("UK811", "Vistara", "2026-05-10 09:40", "2026-05-10 12:10", "Delayed"),
    ]
    flight_index = build_index(flights, "flight_id")

    print("\nSearch Result for Flight ID 6E402:")
    print(flight_index.get("6E402"))

    print("\nSorted by Departure Time:")
    for record in sort_flights_by_departure(flights):
        print(record)

    print("\nSorted by Arrival Time:")
    for record in sort_flights_by_arrival(flights):
        print(record)


def main() -> None:
    task_01_demo()
    task_02_demo()
    task_03_demo()
    task_04_demo()
    task_05_demo()
    task_06_demo()
    task_07_demo()
    task_08_demo()


if __name__ == "__main__":
    main()
