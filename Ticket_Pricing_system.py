Age=int(input("Enter the Age: "))

#D_OF_W=Day of week
D_OF_W=str(input("Enter the day of the week: "))
no_tickets=int(input("Enter the number of tickets: "))
Base_price_child=150
Base_price_adult=300
Base_price_senior=200

if Age<3:
    ticket_price=0
elif Age >=3 and  Age <= 12 :
    ticket_price=Base_price_child
elif Age >=13 and  Age <= 59 :
     ticket_price=Base_price_adult
else:
    ticket_price=Base_price_senior

if D_OF_W in ["Friday", "Saturday", "Sunday"]:
    discount = 0.20
else:
    discount = 0

base_total=ticket_price*no_tickets
discount_amount=base_total*discount
final_total=base_total-discount_amount

print("\n==TICKET BILL===")
print("Base price per ticket:",ticket_price)
print("Total before discount :", base_total)
print("Discount amount:", discount_amount)
print("Final amouunt :", final_total)