#ATM Simualator

balance= 10000
while True:
    print("\n ATM Simulator")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice=int(input("enter choice: "))
    if choice ==1:
        print("Current Balance: ₹", balance)
    elif choice == 2:
        amount=float(input("Enter amount to deposit:"))
        balance += amount
        print("Deposit succesfull")
        print("Updated Balance : ₹", balance)
    elif choice==3:
        amount=float(input("Enter amount to withdraw: "))
       
        if amount>balance:
           print("insufficient Balance")
       
        elif balance - amount < 500:
            print("Minimum balance of ₹500 must remain!")

        else:
            balance -= amount
            print("Withdrawal successful!")
            print("New balance: ₹", balance)

    elif choice == 4:
             print("Thank you for using ATM.")
             break
 
    else:
        print("Invalid choice!")
