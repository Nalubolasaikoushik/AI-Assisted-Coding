"""
Lab 11: Data Structures with AI

This file contains complete Python implementations for:
Task 1: Smart Contact Manager
Task 2: Library Book Search System
Task 3: Emergency Help Desk
Task 4: Hash Table
Task 5: Real-Time Application Challenge

The code is organized with clear task headings and includes demonstration
output so it can be 
used directly in the lab record.
"""


# ============================================================
# Task 1: Smart Contact Manager (Arrays & Linked Lists)
# ============================================================

print("=" * 60)
print("Task 1: Smart Contact Manager (Arrays & Linked Lists)")
print("=" * 60)


class ArrayContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        self.contacts.append({"name": name, "phone": phone})
        print(f"Contact added: {name} - {phone}")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact["name"].lower() == name.lower():
                return contact
        return None

    def delete_contact(self, name):
        for index, contact in enumerate(self.contacts):
            if contact["name"].lower() == name.lower():
                removed_contact = self.contacts.pop(index)
                print(f"Deleted contact: {removed_contact['name']}")
                return True
        print("Contact not found.")
        return False

    def display_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return

        print("Contact List:")
        for contact in self.contacts:
            print(f"{contact['name']} - {contact['phone']}")


class ContactNode:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.next = None


class LinkedListContactManager:
    def __init__(self):
        self.head = None

    def add_contact(self, name, phone):
        new_node = ContactNode(name, phone)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        print(f"Contact added: {name} - {phone}")

    def search_contact(self, name):
        current = self.head
        while current is not None:
            if current.name.lower() == name.lower():
                return {"name": current.name, "phone": current.phone}
            current = current.next
        return None

    def delete_contact(self, name):
        current = self.head
        previous = None

        while current is not None:
            if current.name.lower() == name.lower():
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                print(f"Deleted contact: {current.name}")
                return True
            previous = current
            current = current.next

        print("Contact not found.")
        return False

    def display_contacts(self):
        if self.head is None:
            print("No contacts available.")
            return

        print("Contact List:")
        current = self.head
        while current is not None:
            print(f"{current.name} - {current.phone}")
            current = current.next


print("\nArray-Based Contact Manager Demo")
array_manager = ArrayContactManager()
array_manager.add_contact("Aisha", "9876543210")
array_manager.add_contact("Rahul", "9123456780")
array_manager.add_contact("Meena", "9988776655")
array_manager.display_contacts()
print("Search Result:", array_manager.search_contact("Rahul"))
array_manager.delete_contact("Aisha")
array_manager.display_contacts()

print("\nLinked List Contact Manager Demo")
linked_manager = LinkedListContactManager()
linked_manager.add_contact("Aisha", "9876543210")
linked_manager.add_contact("Rahul", "9123456780")
linked_manager.add_contact("Meena", "9988776655")
linked_manager.display_contacts()
print("Search Result:", linked_manager.search_contact("Meena"))
linked_manager.delete_contact("Rahul")
linked_manager.display_contacts()

print("\nComparison of Array vs Linked List")
print("1. Insertion Efficiency:")
print("   Array insertion at the end is usually fast, but internal resizing may occur.")
print("   Linked list insertion is dynamic and does not require resizing.")
print("2. Deletion Efficiency:")
print("   Array deletion may require shifting elements.")
print("   Linked list deletion updates pointers after locating the node.")
print("3. Search Efficiency:")
print("   Both approaches require linear search in this implementation.")

print("\nSuggested AI Prompt:")
print(
    "Generate Python methods for searching and deleting contacts in both "
    "an array-based and linked-list-based contact manager."
)


# ============================================================
# Task 2: Library Book Search System (Queues & Priority Queues)
# ============================================================

print("\n" + "=" * 60)
print("Task 2: Library Book Search System (Queues & Priority Queues)")
print("=" * 60)


class BookRequestQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, request):
        self.queue.append(request)
        print(f"Request added: {request}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        request = self.queue.pop(0)
        print(f"Processed request: {request}")
        return request

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Current Queue:")
            for request in self.queue:
                print(request)


class PriorityBookRequestQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, user_type, request):
        priority = 1 if user_type.lower() == "faculty" else 2
        self.queue.append((priority, user_type.title(), request))
        self.queue.sort(key=lambda item: item[0])
        print(f"Request added: {user_type.title()} - {request}")

    def dequeue(self):
        if self.is_empty():
            print("Priority queue is empty.")
            return None
        priority, user_type, request = self.queue.pop(0)
        print(f"Processed request: {user_type} - {request}")
        return priority, user_type, request

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        if self.is_empty():
            print("Priority queue is empty.")
        else:
            print("Current Priority Queue:")
            for _, user_type, request in self.queue:
                print(f"{user_type} - {request}")


print("\nQueue Demo")
book_queue = BookRequestQueue()
book_queue.enqueue("Student - Data Science Book")
book_queue.enqueue("Student - Python Programming")
book_queue.enqueue("Faculty - AI Research Book")
book_queue.display()
book_queue.dequeue()
book_queue.display()

print("\nPriority Queue Demo")
priority_queue = PriorityBookRequestQueue()
priority_queue.enqueue("student", "Database Systems")
priority_queue.enqueue("faculty", "Machine Learning")
priority_queue.enqueue("student", "Operating Systems")
priority_queue.enqueue("faculty", "Cloud Computing")
priority_queue.display()
print("\nServing Requests:")
priority_queue.dequeue()
priority_queue.dequeue()
priority_queue.dequeue()
priority_queue.dequeue()

print("\nSuggested AI Prompt:")
print(
    "Generate Python enqueue() and dequeue() methods for a normal queue "
    "and a priority queue where faculty requests have higher priority."
)


# ============================================================
# Task 3: Emergency Help Desk (Stack Implementation)
# ============================================================

print("\n" + "=" * 60)
print("Task 3: Emergency Help Desk (Stack Implementation)")
print("=" * 60)


class HelpDeskStack:
    def __init__(self, capacity=None):
        self.stack = []
        self.capacity = capacity

    def push(self, ticket):
        if self.is_full():
            print("Stack is full. Cannot add more tickets.")
            return
        self.stack.append(ticket)
        print(f"Ticket raised: {ticket}")

    def pop(self):
        if self.is_empty():
            print("No tickets to resolve.")
            return None
        ticket = self.stack.pop()
        print(f"Ticket resolved: {ticket}")
        return ticket

    def peek(self):
        if self.is_empty():
            print("No tickets available.")
            return None
        print(f"Top ticket: {self.stack[-1]}")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        if self.capacity is None:
            return False
        return len(self.stack) >= self.capacity

    def display(self):
        print("Current Tickets:", self.stack)


print("\nStack Demo")
helpdesk = HelpDeskStack(capacity=10)
helpdesk.push("Ticket 1: Wi-Fi issue")
helpdesk.push("Ticket 2: Login problem")
helpdesk.push("Ticket 3: Printer not working")
helpdesk.push("Ticket 4: System crash")
helpdesk.push("Ticket 5: Email not syncing")
helpdesk.display()
helpdesk.peek()
print("\nResolving Tickets:")
helpdesk.pop()
helpdesk.pop()
helpdesk.pop()
helpdesk.display()

print("\nLIFO Behavior:")
print("The last ticket raised is the first ticket resolved.")

print("\nSuggested AI Prompt:")
print(
    "Suggest additional stack operations in Python such as checking whether "
    "the stack is empty and whether it is full."
)


# ============================================================
# Task 4: Hash Table
# ============================================================

print("\n" + "=" * 60)
print("Task 4: Hash Table")
print("=" * 60)


class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        # Convert the key into an index.
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        bucket = self.table[index]

        for i, (stored_key, stored_value) in enumerate(bucket):
            if stored_key == key:
                bucket[i] = (key, value)
                print(f"Updated: {key} -> {value}")
                return

        bucket.append((key, value))
        print(f"Inserted: {key} -> {value}")

    def search(self, key):
        index = self.hash_function(key)
        bucket = self.table[index]

        for stored_key, stored_value in bucket:
            if stored_key == key:
                return stored_value
        return None

    def delete(self, key):
        index = self.hash_function(key)
        bucket = self.table[index]

        for i, (stored_key, stored_value) in enumerate(bucket):
            if stored_key == key:
                del bucket[i]
                print(f"Deleted key: {key}")
                return True

        print("Key not found.")
        return False

    def display(self):
        print("Hash Table Contents:")
        for index, bucket in enumerate(self.table):
            print(f"Index {index}: {bucket}")


print("\nHash Table Demo")
hash_table = HashTable()
hash_table.insert("101", "Aisha")
hash_table.insert("102", "Rahul")
hash_table.insert("112", "Meena")
hash_table.insert("122", "Kiran")
hash_table.display()
print("Search key 102:", hash_table.search("102"))
hash_table.delete("112")
hash_table.display()

print("\nCollision Handling:")
print("This implementation uses chaining, where each index stores a list of key-value pairs.")

print("\nSuggested AI Prompt:")
print(
    "Generate a Python hash table implementation with insert, search, and "
    "delete methods using chaining for collision handling."
)


# ============================================================
# Task 5: Real-Time Application Challenge
# ============================================================

print("\n" + "=" * 60)
print("Task 5: Real-Time Application Challenge")
print("=" * 60)

print("\nFeature to Data Structure Mapping")
print("- Student Attendance Tracking -> Hash Table / Dictionary")
print(
    "  Justification: A hash table allows quick access using student ID "
    "and supports fast update, insertion, and lookup."
)
print("- Event Registration System -> Dynamic List / Linked List")
print(
    "  Justification: Registrations can be added or removed dynamically, "
    "making flexible storage useful."
)
print("- Library Book Borrowing -> Queue")
print(
    "  Justification: Requests are usually handled in the order they are "
    "received, which matches FIFO behavior."
)
print("- Bus Scheduling System -> Graph")
print(
    "  Justification: A graph models stops as nodes and routes as edges, "
    "which is useful for route planning."
)
print("- Cafeteria Order Queue -> Queue")
print(
    "  Justification: Orders are processed in the order customers place "
    "them, so FIFO is appropriate."
)


class AttendanceSystem:
    def __init__(self):
        self.attendance = {}

    def mark_attendance(self, student_id, name, status):
        self.attendance[student_id] = {"name": name, "status": status}
        print(f"Attendance marked: {student_id} - {name} - {status}")

    def search_attendance(self, student_id):
        return self.attendance.get(student_id, "Record not found.")

    def delete_record(self, student_id):
        if student_id in self.attendance:
            del self.attendance[student_id]
            print(f"Deleted attendance record for student ID: {student_id}")
        else:
            print("Record not found.")

    def display_all(self):
        if not self.attendance:
            print("No attendance records available.")
            return

        print("Attendance Records:")
        for student_id, details in self.attendance.items():
            print(f"{student_id}: {details['name']} - {details['status']}")


print("\nSelected Feature Implementation: Student Attendance Tracking")
attendance_system = AttendanceSystem()
attendance_system.mark_attendance("S101", "Aisha", "Present")
attendance_system.mark_attendance("S102", "Rahul", "Absent")
attendance_system.mark_attendance("S103", "Meena", "Present")
attendance_system.display_all()
print("Search:", attendance_system.search_attendance("S102"))
attendance_system.delete_record("S102")
attendance_system.display_all()

print("\nSelected Feature Justification:")
print("A hash table is suitable because student IDs can be used as keys.")
print("This enables fast insertion, update, deletion, and search operations.")


# ============================================================
# End of Lab
# ============================================================

print("\n" + "=" * 60)
print("Lab 11 completed successfully.")
print("=" * 60)
