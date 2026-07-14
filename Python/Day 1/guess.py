import random

print("=" * 30)
print("\tGUESS - NUMBER")
print("=" * 30)

ran_num = random.randint(1,100)
total_attempts = 15
guessed = []

print(f"-"*10,"Choose Level","-"*10)

print('''
1. Easy - 15 Attempts with Hints
2. Medium - 10 Attempts with Hints
3. Hard - 5 Attempts with no Hints   

''')
level = int(input("DIFFICULTY LEVEL: "))

def logic():
    for i in range(total_attempts):
        num = int(input("Guess a number: "))
        print(f"Your guessed number: {num}")
        guessed.append(num)

        print(f"Guessed Numbers: {guessed}")
        print(f"Remaining Attempts: {total_attempts - i - 1}")

        if num == ran_num:
            print(f"Congratulations! - The guess was right.\nThe number is {ran_num}")
            break
        elif num > ran_num:
            print("HINT: Try to guess a small number...")
        elif num < ran_num:
            print("HINT: Try to guess a greater number...")
        else:
            print("Invalid Input")

    print(f"The number was: {ran_num}")

if level == 1:
    logic()
elif level == 2:
    for i in range(total_attempts-5):
        num = int(input("Guess a number: "))
        print(f"Your guessed number: {num}")
        guessed.append(num)

        print(f"Guessed Numbers: {guessed}")
        print(f"Remaining Attempts: {total_attempts - i - 6}")

        if num == ran_num:
            print(f"Congratulations! - The guess was right.\nThe number is {ran_num}")
            break
        elif num > ran_num:
            print("HINT: Try to guess a small number...")
        elif num < ran_num:
            print("HINT: Try to guess a greater number...")
        else:
            print("Invalid Input")

    print(f"The number was: {ran_num}")
elif level == 3:
    for i in range(total_attempts-10):
        num = int(input("Guess a number: "))
        print(f"Your guessed number: {num}")
        guessed.append(num)

        print(f"Guessed Numbers: {guessed}")
        print(f"Remaining Attempts: {total_attempts - i - 11}")

        if num == ran_num:
            print(f"Congratulations! - The guess was right.\nThe number is {ran_num}")
            break

    print(f"The number was: {ran_num}")
else: 
    print("Invalid Input")