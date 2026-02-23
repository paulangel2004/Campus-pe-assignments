Total_bill=float(input("Enter total bill: "))
no_of_ppl=int(input("Enter the number of people: "))
tax_per=float(input("Enter the tax percentage: "))
tip_per=float(input("Enter the tip percentage: "))

#Calculating tax 
tax_amt=(Total_bill)/(tax_per)

#calculating amt after adding tax amt
After_tax=Total_bill+tax_amt

#calculating tips
tip_amt=(After_tax*tip_per)/100

#calculating the total amt
total_amt=After_tax+tip_amt

#calcuting the amt per person
amt_per_pers=(total_amt)/no_of_ppl


print("===BILL BREAKDOWN===")
print(f"Subtotal: ${Total_bill:.2f}")
print(f"Tax(10%):{tax_amt} ")
print(f"After tax:  {After_tax}")
print(f"Tip(15%):{tip_amt}")
print(f"Total: {total_amt}")
print(f"Per Person: {amt_per_pers}")

