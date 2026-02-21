def add(x, y):
    z=x+y
    return z

def subtract(x, y):
    z=x-y
    return z

def multiply(x, y):
    z=x*y
    return z

def divide(x, y):
    if y ==0:
        return "Error! Division by zero."
    elif x<y:
        return "Error! Division not possible when first number is smaller than second number."
    z=x/y
    return z
def modulus(x,y):
    if y ==0:
        return "Error! Division by zero."
    elif x<y:
        return "Error! Modulus not possible when first number is smaller than second number."
    z=x%y
    return z

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")

while True:
    select = input("Enter inputs(1/2/3/4/5): ")

    if select in ('1','2','3','4','5'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        if select == '1':
            print(num1,"+",num2,"=",add(num1,num2))
        elif select == '2':
            print(num1,"-",num2,"=",subtract(num1,num2))
        elif select == '3':
            print(num1,"*",num2,"=",multiply(num1,num2))
        elif select == '4':
            print(num1,"/",num2,"=",divide(num1,num2))
        elif select == '5':
            print(num1,'%',num2,'=',modulus(num1,num2))
        
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation.lower() == "no":
            break
    else:
        print("Invalid Input")

