import random
import string

def generate_password(length, complexity):
    # these are Character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # this is our Complexity levels
    if complexity == 1:
        characters = lowercase
    elif complexity == 2:
        characters = lowercase + uppercase
    elif complexity == 3:
        characters = lowercase + uppercase + digits
    elif complexity == 4:
        characters = lowercase + uppercase + digits + symbols
    else:
        print("Invalid choice! Defaulting to full complexity.")
        characters = lowercase + uppercase + digits + symbols

    # this is used to Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# this is our main program
if __name__ == "__main__":
    try:
        length = int(input("Enter desired password length: "))
        print("\nChoose complexity level:")
        print("1 - Only lowercase")
        print("2 - Lowercase + Uppercase")
        print("3 - Letters + Digits")
        print("4 - Letters + Digits + Symbols")

        complexity = int(input("Enter choice (1-4): "))
        password = generate_password(length, complexity)
        print("\nGenerated Password:", password)

    except ValueError:
        print("Please enter valid inputs.")
