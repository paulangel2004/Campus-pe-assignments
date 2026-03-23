num = int(input("Enter the number: "))
end = int(input("Enter the range (end): "))

print("Multiplication Table (1 to 10)\n")

for i in range(1, 11):        #for rows
    for j in range(1, 11):    #for columns
        print(i * j, end="\t")  
    print()  