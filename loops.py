"""# Print numbers from 1 to 100.
n = 1
while n <= 100:
    print(n)
    n += 1"""

"""#Print numbers from 100 to 1
n = 100
while n>=1:
    print(n)
    n -= 1 """

"""# multiplication table of number n
n = 1
while n<=10:
    print(2 * n)
    n += 1 """

"""# Print the elements of the following list using a loop:
list = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
i = 0
while i<len(list):
    print(list[i])
    i += 1
"""

"""numbers = [1,2,3,4,5,6,7]
x = int(input(("enter the number to search")))
i = 0
found = False
while i<len(numbers):
    if numbers[i] == x:
        print(f"{x} found at index{i}")
        found = True
        break
    i += 1

if not found:
    print(f"{x} is not found")    
"""

"""num = [1,2,3,4]  
for el in num:
    print(el)
else:
    print("end")  """  

"""for el in range(5):
    print(el); """ 


"""for el in range(1,8):
    print(el)"""

"""for el in range(1,5,2):
    print(el)"""

"""for el in range(10, 0, -1):
    print(el)"""

n = 2
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")


# WAP to find the sum of first n numbers. (using while)
sum=0
n=int(input("enter a number n"))
i=0
while i<=n:
    sum+=i
    i = i+1

print(sum)    

# WAP to find the factorial of first n numbers. (using for)
fact = 1
n = int(input("enter a number "))
for i in range(n, 0, -1):
    fact = fact * i


print(f"factorial of {n} is {fact}")
