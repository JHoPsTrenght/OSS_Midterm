# Program make a simple calculator
import logger as L


# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y

#Need to define divide function.
def divide (x,y):
    if y==0:
        print("0으로 나눌 수 없습니다.")
        L.error("0으로 나눌 수 없습니다.")
    else:
        return x/y

