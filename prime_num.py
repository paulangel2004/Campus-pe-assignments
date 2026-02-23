# Part 1: Check if a number is prime

num = int(input("Enter a number: "))

if num < 2:
    print(f"{num} is NOT a prime number")

elif num == 2:
    print("2 is a PRIME number")

else:
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{num} is a PRIME number")
    else:
        print(f"{num} is NOT a prime number")

#Prime numbers in a range

start = int(input("Enter start range: "))
end = int(input("Enter end range: "))

print("Prime numbers:", end=" ")

for num in range(start, end + 1):
    if num >= 2:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=", ")