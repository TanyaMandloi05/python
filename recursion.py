# prints n to 1 backwards
def printN(n):
    if(n==0):
        return
    print(n)
    printN(n-1)

printN(5)    

#factorial of a number n

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(5))  

# Write a recursive function to calculate the sum of first n natural numbers.
def sumOfAll(n):
    if(n==1):
        return 1
    else:
        return n+sumOfAll(n-1)
    
print(sumOfAll(5))    

# Write a recursive function to print all elements in a list.
def printList(list, idx):
    if(idx >= len(list)):
        return
    print(list[idx], end=' ')
    printList(list, idx = idx+1)

listItem = [1,2,3,4,5,6]
printList(listItem,0)    