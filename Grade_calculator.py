total=0
passed= True

for i in range(1,6):
    marks=int(input(f"Enter the marks of the subjects {i}:"))
    total+=marks

    if marks< 40:
        passed = False

percentage=(total/500)*100

#calculating the grade

if percentage >=90:
    grade="A+ (outstading)"
elif percentage >=80:
    grade="A (outstading)"
elif percentage >=70:
    grade="B (outstading)"
elif percentage >=60:
    grade="C (outstading)"
elif percentage >=50:
    grade="D (outstading)"

else :
    grade="F (Fail)"

#result
if passed:
    result="pass"
else:
    result="fail"

print("\n==RESULT===")
print("Total Marks:",total,"/500")
print(f"Percentage:{percentage:.2f}%")
print("Grade :",grade)
print("Result:" , result)





