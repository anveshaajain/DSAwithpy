students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

topper = max(students, key=students.get)

print("Topper is:", topper)
