import random

all_letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

all_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
all_symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator")
letters_count = int(
    input("How many letters would you like in your password? "))
symbols_count = int(input("How many symbols would you like? "))
numbers_count = int(input("How many numbers would you like? "))

password = ""

for _ in range(0, letters_count):
  password += random.choice(all_letters)

for _ in range(0, symbols_count):
  password += random.choice(all_symbols)

for _ in range(0, numbers_count):
  password += random.choice(all_numbers)

password_as_list = list(password)
random.shuffle(password_as_list)
shuffled_password = ''.join(password_as_list)

print(f"Here is your password: {shuffled_password}")
print(
    "Thank you for using the Password Generator! Stay safe out there!\U0001f600"
)
