courses = ["MIT", "Cybersecurity", "Data Science"]
print(courses)

# Accesing an element in an array

print(courses[1])

# Looping through an array

for course in courses:
    print(course)

# Adding an element

courses.append("Android Programming")
print(courses)

# Deleting an element from an array

courses.remove("Data Science")
print(courses)
print(type("courses"))
