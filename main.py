import func
import logger as L

print("Calculator started.")
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide") 

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")
    opinion=False
    end=False
    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", func.add(num1, num2))
            a=str(num1)+"+"+str(num2)+"="+str(func.add(num1,num2))
            L.succeed(a)

        elif choice == '2':
            print(num1, "-", num2, "=", func.subtract(num1, num2))
            a=str(num1)+"-"+str(num2)+"="+str(func.subtract(num1,num2))
            L.succeed(a)

        elif choice == '3':
            print(num1, "*", num2, "=", func.multiply(num1, num2))
            a=str(num1)+"*"+str(num2)+"="+str(func.multiply(num1,num2))
            L.succeed(a)
            
        elif choice =='4':
            if num2 ==0:
                L.error("0으로 나눌 수 없습니다.")
            else:
                print(num1, "/", num2, "=", func.divide(num1,num2))
                a=str(num1)+"/"+str(num2)+"="+str(func.divide(num1,num2))
                L.succeed(a)
        
        while(1):
            next_calculation = input("Let's do next calculation? (yes/no): ")
            if next_calculation.lower() == "no":
                opnion=True
                sure=input("Are you sure? (yes/no): ")
                if sure.lower() == "yes":
                    end=True
                    break
                elif sure.lower() == "no":
                    opinion=False
                    break
                else:
                    print("Only (yes/no)")
                    continue
            elif next_calculation.lower() == "yes":
                break
            else:
                print("Only (yes/no)")
                continue
        if end == True:
            break
    else:
        L.error("1,2,3,4 이외의 입력은 들어올 수 없습니다.")
