# Starter: How do I output the species values for each of the dictionaries?
[
{'species': 'zebra', 'name': 'Penelope'},
{'species': 'penguin', 'name': 'Jenn'},
{'species': 'elephant', 'name': 'Harris'},
{'species': 'flamingo', 'name': 'Florence'},
]

# solution
for item in animals:
    print(item['species'])



# File handling in Python
# How do I write to a text file and print its contents?
with open('file.txt', 'w+') as file:
    people = 'Ahmed \nLaila \n'
    file.write(people)


# How to add data to a file without over-writting existing data (append)
with open("file.txt", 'a') as file:
    file.write("\nHamza")


# How do I read a text file and print its contents?
with open('file.txt', 'r') as new_file:
    print(new_file.read())
    

# Save shopping list taken from the user to a file

item = input("what do you want to buy? ")
with open('list.txt', 'a') as file:
    file.write(item + '\n')  
    

shopping_list =input("please Enter shopping List separated by a space:  ").split()

for item in shopping_list:
    with open('shopping_list.txt', 'a') as file:
        file.write(item + '\n')


with open('shopping_list.txt', 'r') as file:
    print(file.read())

# Dealing with CSV files:
# writting to a CSV file
import csv

filed_names = ['name', 'age']
data = [
    {'name': 'ahmed','age': 25},
    {'name': 'laila','age': 30},
    {'name': 'mona','age': 33}
       
]

with open('people.csv', 'w+') as file:
    writer = csv.DictWriter(file, fieldnames=filed_names)
    writer.writeheader()
    writer.writerows(data)

# Reading a CSV file and print its contents?
with open('people.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['name'])
        print(row['age'])


# Command to install requests liberary using terminal:
# pip install requests



import requests
from pprint import pprint

pokemon_no = input("What is the pokemon ID? ")
url =f'https://pokeapi.co/api/v2/pokemon/{pokemon_no}/'

response = requests.get(url)
# pprint(response.json())
# check response status
if response.status_code == 200:
    data = response.json()
    print(data['name'])
    print(data['weight'])
    print(data['species'])
else:
    print("Bad request")

