# Age Calculator 

from datetime import date

birth_day = int(input("Enter your birth day: "))
birth_month = int(input("Enter your birth month: "))
birth_year = int(input("Enter your birth year: "))

# Today's date
today = date.today()

#initialzing DOB
dob = date(birth_year, birth_month, birth_day)

# Calculating age in years
age = today.year - birth_year

# If birthday has not come yet this year, reduce age by 1
if today.month < birth_month or (today.month == birth_month and today.day < birth_day):
    age = age - 1

# Calculating total days lived
days_lived = (today - dob).days

print("\n===== AGE DETAILS =====")
print("Current Age:", age, "years")
print("Age in Months:", age * 12)
print("Age in Days:", days_lived)
print("Age in Hours:", days_lived * 24)
print("Age in Minutes:", days_lived * 24 * 60)
print("Years until 100:", 100 - age)