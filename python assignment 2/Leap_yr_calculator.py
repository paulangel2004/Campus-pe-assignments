#LEAP YEAR RULE :A year is a leap year if divisible by 4 AND (NOT divisible by 100 OR divisible by 400).


Year=int(input("Enter the year:"))
if Year%4==0 and (Year%100!=0 or Year%400==0):
    print(f"{Year} is a leap year beacuse it satisfies the leap year rule ")
else:
    print(f"{Year} is not a leap year beacuse it does not satisfy the leap year rule  ")
