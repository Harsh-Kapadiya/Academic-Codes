print("Select Option\n 1. Add\n 2. subtract\n 3. Multiply\n 4. Divide\nEnter your choise(1/2/3/4): ")

choice = input()

x = float(input("Enter first Number: "))

y = float(input("Enter second Numebr: "))

if choice == '1':
    result = float(x) + float(y)
    print("Result: ", result)

if choice == '2':
    result = float(x) - float(y)
    print("Result: ", result)

if choice == '3':
    result = float(x) * float(y)
    print("Result: ", result)

if choice == '4':
    if y == 0 :
        print("Error: Division by zero is not allowed.")
    else:
        result = float(x)/float(y)
        print("Result: ", result)