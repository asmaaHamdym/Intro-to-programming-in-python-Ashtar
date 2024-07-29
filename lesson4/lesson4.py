# There are four mistakes in this program. What are the mistakes and how would you x them?
# carrots = input('How many carrots do you have? ')
# rabbits = 6

# if rabbits < carrots:
#     print('There are not enough carrots')
# if rabbits > carrots:
#     print('There are too many carrots')
# else:
#     print('You have the right number of carrots')


# city = 'Cairo'
# city2 = 'London'
# city3 = 'Paris'
# city4 = 'Tokyo'
# city5 = 'New York'


# List of strings
cities = ['Cairo','London','Paris','Tokyo','New York']
# list of integers
numbers = [12,21,33,14,52]
# list of more than one data type
mixed_list = ['apple', 2, 3.5, True]

# List values can be accessed using their index in square brackets
print(cities[0])  # Output: Cairo
print(numbers[1])  # Output: 2
print(mixed_list[2])  # Output: 3.5

# List indexes start counting from 0
student_names = [
    'Ahmed', # index 0
    'Ali',   # index 1
    'Osama', # index 2
    'Mohamed'# index 3
    ]
print(cities[-1])  # Output: New York
print(numbers[-2])  # Output: 4
    

# setting list values using index
print(student_names[0])  # Output: Ahmed
student_names[0] = 'Hassan'
print(student_names[0])  # Output: Hassan

#  random choice method
import random
print(random.choice(student_names))  

# List Methods
# len() - returns the number of items in the list
print(len(cities))  # Output: 5
print(len(numbers))  # Output: 5
# min() - returns the smallest value in the list
print(min(numbers))  # Output: 1
# max() - returns the biggest value in the list
print(max(numbers))  # Output: 5
# sum() - returns the sum of all values in the list
print(sum(numbers))  # Output: 15



# append() - adds a new element to the end of the list
cities.append('Barcelona')
print(cities)  # Output: ['Cairo', 'London', 'Paris', 'Tokyo', 'New York' , 'Barcelona']

# pop() - removes and returns the last element from a list
cities.pop()
print(cities)  # Output: ['Cairo', 'London', 'Paris', 'Tokyo', 'New York']

# remove() - removes the first occurrence of a value
cities.remove('Paris')
print(cities)  # Output: ['Cairo', 'London', 'Tokyo', 'New York']
# sorted() - returns a new sorted list from the elements of any sequence
print(sorted(numbers))
print(sorted(cities))

# reverse() - reverses the list
cities.reverse()
print(cities)  

# In operator in Lists
# The in operator is used to check if a value is present in a list or not
print('Paris' in cities)
print('Paris' not in cities)


# Shopping Example
# Create a list of items
items = ['apple', 'milk', 'eggs', 'meat', 'coffee']
if 'rice' in items:
    print('We got the Rice')
else:
    print('We forgot!')


# Looping over a list:
# for loop
for item in items:
    print(f'We have {item}')


# Dictionary
# A dictionary is a collection of key-value pairs
person = {
    'name': 'Asmaa',
    'age': 25,
    'city': 'Cairo'
    }

# Values in a dictionary are accessed using their keys
print(person['name'])
print(person['age'])
print(person['city'])

# dicts inside other dicts
person2 = {
    'name': 'Ali',
    'age': 25,
    'city': 'Cairo',
    'address': {
        'street': 'street1',
        'building': '15',
        'floor': '6'
        }

}
print(person2['address']['street'])


# Dicts in lists
people = [
    {'name': 'Asmaa', 'age': 25},
    {'name': 'Ali', 'age': 36},
    {'name': 'Ahmed', 'age': 15}
    ]

#  for loops with Dicts
for person in people:   
    print(f'{person["name"]} is {person["age"]} years old')


