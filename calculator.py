num1 = 53
#input("Enter First Number")
num2 = 7
#input("Enter Second Number")

    #total = num1 + 1
def add(num1, num2):
    result = num1
    for i in range(num2):
        result = result + 1
    print(result) 

#Subtraction
def sub(num1, num2):
    result = num1
    for i in range(num2):
        result = result - 1
    print(result)


#Multiplication
def mult(num1, num2):
    result = 0
    for i in range(num2):
        for i in range(num2):
            result = result + 1
    print(result)

add(num1,num2)
sub(num1,num2)
mult(num1,num2)
