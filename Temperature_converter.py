#Temperture converter
print("1. Celsius to Fahrenheit: ")
print("2. Fahrenheit to Celsius: ")
print("3. Celsius to Kelvin: ")
print("4. Kelvin to Celsius: ")
print("5. Fahrenheit to Kelvin: ")
print("6. Kelvin to Fahrenheit: ")
print("7. Exit")

choice = int(input("Enter your choice: "))

if choice == 7:
    print("Exited")

else:
 celsius=float(input("Enter the temperture ein celsius"))
 
 c_to_f=(celsius*(9)/(5)+32)
 fahrenheit=c_to_f

 #fahrenheit to celsius
 f_to_c=(fahrenheit-32)*(5)/(9)

 #celsius to kelvin
 c_to_k=(celsius+273.15)

 kelvin =c_to_k

#kelvin to celsius
 k_to_c=kelvin -273.15
 
 #fahrenhiet to kelvin
 f_to_k=(fahrenheit-32)*(5)/(9)+273.15

 #kelvin to fahrenhiet 
 k_to_f=(kelvin -273.15)*(9)/(5)+32

 if choice == 1:
        print(f"Celsius to Fahrenheit: {c_to_f}")
 elif choice == 2:
        print(f"Fahrenheit to Celsius: {f_to_c}")
 elif choice == 3:
        print(f"Celsius to Kelvin: {c_to_k}")
 elif choice == 4:
        print(f"Kelvin to Celsius: {k_to_c}")
 elif choice == 5:
        print(f"Fahrenheit to Kelvin: {f_to_k}")
 elif choice == 6:
        print(f"Kelvin to Fahrenheit: {k_to_f}")




