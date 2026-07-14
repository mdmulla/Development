print("=" * 30)
print("\t CALCULATOR")
print("=" * 30)

num = []

choice = ""

while choice != "n":
    number = int(input("Enter a number: "))
    num.append(number)
    print(f"Entered Numbers: {num}")
    choice = input("Do you want to write another number?(Y/N): ").lower()
    if choice != "y":
        break
   
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n")
op = int(input("Choose the operation: "))

result = 0

if op == 1:
    for i in num:
        result += i
    print(f"Result: {result}")
elif op == 2:
    result = num[0]
    for i in num[1:]:
        result -= i
    print(f"Result: {result}")
elif op == 3:
    result = num[0]
    for i in num[1:]:
        result *= i
    print(f"Result: {result}")
elif op == 4:
    result = num[0]
    for i in num[1:]:
        result /= i
    print(f"Result : {result}")
else:
    print("Invalid Input. Try again..")




#OPTIMIZED VERSION

print("=" * 30)
print("\t CALCULATOR")
print("=" * 30)

numbers = []

while True:
    numbers.append(int(input("Enter a number: ")))

    choice = input("Add another number? (Y/N): ").lower()

    if choice == "n":
        break

print("""
1. Addition
2. Subtraction
3. Multiplication
4. Division
""")

operation = int(input("Choose an operation: "))

result = numbers[0]

if operation == 1:
    result = 0
    for number in numbers:
        result += number

elif operation == 2:
    for number in numbers[1:]:
        result -= number

elif operation == 3:
    for number in numbers[1:]:
        result *= number

elif operation == 4:
    for number in numbers[1:]:
        result /= number

print(f"Result: {result}")