import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("=== Password Generator ===")
    while True:
        try:
            length = int(input("Enter password length: "))
            if length <= 0:
                print("Length must be greater than 0.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        password = generate_password(length)
        print("\nGenerated Password:")
        print(password)

        again = input("\nGenerate another? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
