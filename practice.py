# with open("practice.txt","w") as f:
#     f.write("Hi Everyone")
#     f.write("\n we are learning File I/O")
#     f.write("\n using java")
#     f.write("\n i like programming in java")

# with open("practice.txt","r") as f:
#     data = f.read()
# newdata = data.replace("java", "python")
# print(newdata)

# with open("practice.txt", "w") as f:
#     f.write(newdata)

word = "learning"
with open("practice.txt", "r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("found")
    else:
        print("not found")


word = "like"
def find_line_of_word():
    with open("practice.txt", "r") as f:
        data = True
        line = 1
        while data:
            data = f.readline()
            if(word in data):
                print(line)
            line += 1
        return -1        
        
find_line_of_word()

def countEven():
    with open("number.txt","r") as f:
        data = f.read()
        num = ""
        count = 0
        for i in range(len(data)):
            if(data[i] == ','):
                val = int(num)
                num = ""
                if(val % 2 == 0):
                    count += 1
            else:
                num += data[i] 
        if num:
            val = int(num)
            if val % 2 == 0:
                count += 1

        return count                      
    
print(countEven())    

# better approch using split
def countAllEven():
    with open("number.txt", "r") as f:
        count = 0
        data = f.read()
        num = data.split(",")
        for val in num:
            if(int(val) % 2 == 0):
                count += 1
        return count     
       
print(countAllEven())
