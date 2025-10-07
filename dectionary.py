"""dict = {
    "name":"tanya",
     "marks": 98,
     "cgpa":[8, 9, 10],
     "marks":64
}

print(dict["marks"])"""

Student = {
    "name":"tanya",
    "score": {
        "math": 98,
        "chem":76,
        "physics":54
    }
}

newData = {
    "class": 5,
}

# print(Student)
# print(Student.keys())
# print(Student.values())
# print(Student.items())
print(Student.get("score").get("math"))
Student.update(newData)
print(Student)
