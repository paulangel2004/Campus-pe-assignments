import random

best_score = None

def play_game():
    global best_score
    number = random.randint(1, 100)
    attempts = 7
    used = 0

    while attempts > 0:
        guess = int(input("Enter your guess (1-100): "))
        used += 1
        attempts -= 1

        if guess == number:
            print("Correct! You guessed the number.")
            print("Attempts used:", used)

            if best_score is None or used < best_score:
                best_score = used
                print("New best score:", best_score)
            return

        elif guess < number:
            print("Too low.")
        else:
            print("Too high.")

        if abs(guess - number) <= 5:
            print("Hint: You are very close.")

        print("Attempts remaining:", attempts)

    print("You failed. The number was:", number)


while True:
    play_game()
    again = input("Do you want to play again? (yes/no): ").lower()
    if again != "yes":
        break