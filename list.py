"""marks=[90, 80, 70, 80, 90]
print(marks[0])
marks[0] = 100
print(marks[0])

student = ["tanya", 20, "delhi"]
print(student)
print(len(student))

print(marks[1:4])"""

#append, sort, reverseSort, insert element at idx

fruits=["kiwi", "banana"]
number=[100,90,80,12,56]
number.sort()
print(number)

number.sort(reverse=True)
print(number)
fruits.insert(5, "apple")
print(fruits)

number.append(1000)
print(number)

print(fruits.index("apple"))

number.remove(90)
print(number)

number.pop(4)
print(number)