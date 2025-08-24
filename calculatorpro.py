# Input
num1 = float(input("First: "))
num2 = float(input("Second: "))

print("\nOp? ")
print("i.+  ii.-  iii.*  iv./")

choice = input("Pick: ")

# Calculation
if choice in ['i', '+']:
    print("Ans:", num1 + num2)

elif choice in ['ii', '-']:
    print("Ans:", num1 - num2)

elif choice in ['iii', '*']:
    print("Ans:", num1 * num2)

elif choice in ['iv', '/']:
    if num2 != 0:
        print("Ans:", num1 / num2)
    else:
        print("Err: /0")

else:
    print("Bad choice!")
