def sum(a,b):
    s = a+b
    return s

print(sum(23,50))

# WAF to print the length of a list. ( list is the parameter)
def printLen(list):
    print(len(list))

sample = [1,2,3]
printLen(sample)    


# WAF to print the elements of a list in a single line. ( list is the parameter)
def printList(list):
    for item in list:
        print(item, end=' ')
    print()    

listData = [1,2,3,4,5]
printList(listData)


# WAF to find the factorial of n. (n is the parameter)
def factorial(n):
    fact = 1
    for i in range(n, 0, -1):
        fact = fact * i
        return fact    

print(factorial(5))

# WAF to convert USD to INR.
def usdToInr(usd):
    conversionRate = 88.76
    INR = usd * conversionRate
    print(INR)

usdToInr(5)