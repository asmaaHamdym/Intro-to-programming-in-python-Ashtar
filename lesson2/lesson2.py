#float data type
#float data type is used to store decimal numbers
rate = 48.29
usd = 50
egp = usd * rate
print(egp)
# type function
print(type(usd))
print(type(egp))
print(int(egp))
# #  type conversion
# #int to float             
usd = float(usd)
print(usd)
print(type(usd))



# # taking input from the user

age = input("What is your age? ")

print(f'you are {age} years old')
print(type(age))

# # Budget planner
salary = int(input("What is your salary? "))
food = int(input("How much do you spend on food? "))
rent = int(input("How much do you spend on rent? "))
phone = int(input("How much do you spend on phone? "))
transportation = int(input("How much do you spend on transportation? "))
savings =  salary - ( food + rent + phone + transportation)
print(f'You have {savings} left to save')
# what happens if we typed a string?

# importing modules
# modules are code written bt someone else
import datetime

time = datetime.datetime.today()
print(time)

# random module
import random 

random_number = random.random() * 10
random_from_range = random.randint( 1,40)
print(random_from_range)



# flow control with loops
# for loop

# print hello 5 times
for number in range(5):
    print('hello')

for character in 'Banana':
    print(character)        

# Counter game
for number in range(1, 30, 3):
  print(number)


# while loop:

# print hello 5 times
number = 5
while number > 0:
    print('hello')  
    number = number - 1


# Elevator example
elevator_capacity = 5
while elevator_capacity > 0 :
    print('Please come in')
    elevator_capacity = elevator_capacity - 1

print('Elevator is full')
    
# functions
#hello name function

def say_Hello(name):
    print(f"Hello, {name}")


say_Hello("Asmaa")
say_Hello("ALi")
say_Hello("Laila")
say_Hello("Sara")

#sum function

def sum_two_numbers( num1, num2):
    result = num1 + num2
    return result



print(sum_two_numbers( 3, 9))
print(sum_two_numbers( 3, 9566))
print(sum_two_numbers( 99, 100))

# days in hours function
def calculate_days_in_hours(days):
    return days * 24

print(calculate_days_in_hours(20))
print(calculate_days_in_hours(100))
print(calculate_days_in_hours(80))
print(calculate_days_in_hours(70))