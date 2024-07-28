# Starter: Rewrite this code to use a for loop and the range() function:
print('~' * 0)
print('~' * 1)
print('~' * 2)
print('~' * 3)
print('~' * 4)
print('~' * 5)
print('~' * 6)
print('~' * 7)
print('~' * 8)

for num  in range(9):
    print('~' * num)

# Boolean data type

is_weather_hot = True
print(type(is_weather_hot))

# Comparison operators
# ==, !=, >, <, >=, <=
print( 10 == (2+5))
print(5 != 5)
print( 10 > 6)
print( 3 < 2)
print( 3 >= 3)
print( 5 <= 5)


today = input("What day is it? ")
is_Sunday = (today == 'Sunday')
print(is_Sunday)

# How much is the sandwitch?
price = float(input(" How much is the sandwitch? "))
budget = float(input("How much money do you have? "))

is_within_budget = budget >= price

print(f"Sandwitch is within Budget: {is_within_budget}")

# Logical operators
# and, or, not

is_sunny = True
is_too_hot = True

# and - not 
is_good_weather = is_sunny and not is_too_hot
print(f"Is good weather: {is_good_weather}")
# or - not
is_good_weather = is_sunny or not is_too_hot
print(f"Is good weather: {is_good_weather}")

# not 
is_good_weather = not is_sunny and not is_too_hot
print(f"Is good weather: {is_good_weather}")


# If statement

name = input("What is your name? ")
is_admin = name == "admin"
password = input("What is your password? ")
is_valid_password = password == "abcdefg"

if is_admin and is_valid_password:
    print("Welcome admin")
if not is_admin or not is_valid_password:
    print("Access denied")


# Rewite it using else
# name = input("What is your name? ")


is_admin = name =='admin'

if is_admin :
    password = input("What is your password? ")
    is_valid_password = password = '1234'
    if is_valid_password:
        print("Welcome admin")
    else:
        print("Wrong password")

else: 
    print("wrong username")

# Password Checker

password = input("Enter Password: ")
confirm_password = input("Enter Password again: ")

if len(password) >= 8 and password.isalnum():
    print("Password is valid")

if len(confirm_password) >= 8 and confirm_password.isalnum():
    print("Password is valid")

if password == confirm_password:
    print("Passwords match")
else: 
    print("Passwords don't match!")




# rewrite the sandwitch example using if statments

price = float(input(" How much is the sandwitch? "))
budget = float(input("How much money do you have? "))


if budget > price:
    print('I can afford to buy it.😀 ')
elif budget < price:
    print("I can't afford it 😟")

else:
    print("I have exactly enough! 😉")

# Books or Movies example
choice = input("Books or movies: ").lower().strip()
if choice == 'books':
    print("📔")

elif choice == 'movies':
    print("🍿")

elif choice == 'Sleep':
    print("🛌")

else:
    print('🌹')



# Random number game

import random

secret_num = random.randint(1,10)


tries = 3

while tries > 0:
    try:
        guess = int(input("Guess a random number between 1 and 10: "))
        if guess == secret_num:
            print("You won 🎉")
            break
        
        tries -= 1
        if tries > 0:
            print("Try again")
    
    except:
        print("Invalid input")

    

if tries == 0 :
    print("Game Over 😟")