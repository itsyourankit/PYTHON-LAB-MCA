# -------------------------------------------
# 🧠 Dictionary Operations in Python
# -------------------------------------------

# 1️⃣ Creating a dictionary
print("=== 1. Creating a Dictionary ===")
courses = {
    "Python": 120,
    "Java": 95,
    "C++": 80,
    "Data Science": 150,
    "Machine Learning": 130
}
print("Original Dictionary:")
print(courses)

# 2️⃣ Accessing value using get()
print("\n=== 2. Accessing value using get() ===")
print("Students in Java:", courses.get("Java"))

# 3️⃣ Adding a new course
print("\n=== 3. Adding a new course ===")
courses["Cyber Security"] = 90
print("After adding Cyber Security:")
print(courses)

# 4️⃣ Updating existing course
print("\n=== 4. Updating existing course ===")
courses.update({"Python": 125})
print("After updating Python students:")
print(courses)

# 5️⃣ Removing a course using pop()
print("\n=== 5. Removing a course using pop() ===")
removed = courses.pop("C++")
print(f"Removed C++ with {removed} students")
print(courses)

# 6️⃣ Removing last inserted item using popitem()
print("\n=== 6. Removing last inserted item using popitem() ===")
last_item = courses.popitem()
print(f"Removed last inserted item: {last_item}")
print(courses)

# 7️⃣ Displaying all keys, values, and items
print("\n=== 7. Displaying all keys, values, and items ===")
print("Courses (keys):", courses.keys())
print("Courses and Students (items):", courses.items())

# 8️⃣ Checking if a course exists
print("\n=== 8. Checking if a course exists ===")
if "Java" in courses:
    print("Java course is available.")
else:
    print("Java course is not available.")

# 9️⃣ Copying dictionary
print("\n=== 9. Copying dictionary ===")
copy_dict = courses.copy()
print("Copied Dictionary:", copy_dict)

# 🔟 Clearing dictionary
print("\n=== 10. Clearing dictionary ===")
courses.clear()
print("Dictionary after clearing:", courses)

# -------------------------------------------
# 🌟 Using Box from python-box library
# -------------------------------------------
print("\n=== 11. Using Box (Object-like Dictionary) ===")

from box import Box

# Creating Box object
box_courses = Box({
    'math': 'Algebra',
    'science': 'Physics',
    'history': 'World History'
})

# Accessing values using dot notation
print("Math course:", box_courses.math)
print("Science course:", box_courses.science)
print("History course:", box_courses.history)

# Checking if key exists
if "Java" in box_courses:
    print("Java course is available.")
else:
    print("Java course is not available.")

# Copying Box
copy_box = box_courses.copy()
print("\nCopied Box Dictionary:", copy_box)

# Clearing Box
box_courses.clear()
print("Box Dictionary after clearing:", box_courses)
