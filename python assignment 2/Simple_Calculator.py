num1=int(input("Enter first number: "))
num2=int(input("Enter the Second number: "))

addition=num1+num2
subtraction=num1-num2
multiplication=num1*num2
division=num1/num2
modulus=num1%num2
exponent=num1**num2
print("Results\n")

print(f"{num1} + {num2} ={addition}")
print(f"{num1} - {num2} ={subtraction}")
print(f"{num1} * {num2} ={multiplication}")
print(f"{num1} / {num2} ={division:.2f}")
print(f"{num1} % {num2} ={modulus}")
print(f"{num1} ^ {num2} ={exponent}")
