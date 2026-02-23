count = int(input("How many numbers? "))

total = 0
max = None
min = None

for i in range(1, count + 1):
    num = int(input(f"Enter number {i}: "))
    
    total += num

    if max is None or num > max:
        max = num

    if min is None or num < min:
        min = num

average = total / count

print("Sum:", total)
print("Average:", average)
print("maximum:", max)
print("minimum:", min)