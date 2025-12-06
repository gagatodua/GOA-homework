#1)

def greeting():
    print('hello')
greeting()

#2)

def add(a, b):
    print(a + b)
add(2, 5)   

def subtract(a, b):
    print(a - b)
subtract(5, 2)   


def multiply(a, b):
    print(a * b)
multiply(5, 2)   


def divide(a, b):
    print(a / b)
divide(5, 2)   


#3)

def ask_age():
    age=int(input("enter your age"))
    if age >=18:
        print("you are an adult")
    else:
        print("you are kid")

#4)

```def calculator(a,b):
    operator = input('enter operator (+, -, *, /): ')
    if operator == '+':
        add(a, b)
    elif operator == '-':
        subtract(a, b)
    elif operator == '*':
        multiply(a, b)
    elif operator == '/':
        divide(a,b)
    else:
        print("enter valid answer")
        calculator(a, b)
    
calculator(10, 15)```
    
