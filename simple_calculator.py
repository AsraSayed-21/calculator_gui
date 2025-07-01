#simple_calculator.py

#addition
def add(a,b):
    return a+b

#subtraction
def subtract(a,b):
    return a-b

#multiplication
def multiply(a,b):
    return a*b

#division
def divide(a,b):
    if b==0:
        return "Error: cannot divide by zero"
        return a/b
    
    
#menu for the user
print("Simple calculator")
print("Choose an operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
#taking users choice
choice=input("Enter your Choice (1/2/3/4): ")


#getting input from the useer and converting it to float
num1= float(input("Enter the first number: "))
num2= float(input("Enter the second number: "))


#writing if statements for functions to work accordingly when the user choses 1,2,3 or 4 function 
if choice == '1':
    result=add(num1,num2)
elif choice == '2':
    result=subtract(num1,num2)
elif choice == '3':
    result=multiply(num1,num2)
elif choice == '4':
    result=divide(num1,num2)
else:
    result="Invalid Choice"
    
    
#printing the result
print("Result : ",result)