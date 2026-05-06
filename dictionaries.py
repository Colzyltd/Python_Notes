# # A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.


# Create dict
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

# # Use constructor
person2 = dict(first_name='Sara', last_name='Williams')
person5 = dict(first_name='Samuel', last_name='Boris' )
# print(person5)

# # Get value
# print(person['first_name']) 
# print(person.get('last_name'))


# # Add key/value
person['phone'] = '555-555-5555'

# # Get dict keys
# print(person.keys())

# # Get dict items
# print(person.items())

# # Copy dict
# person2 = person.copy()
# person2['city'] = 'Boston'

# # Remove item
# del(person['age'])
# person.pop('phone')

# # Clear
# person.clear()

# # Get length
# print(len(person2))

# List of dict
import json 

# Lis of Dict 
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]
# print(people)
user = json.dumps(people)
# print(user)

peopleJSON = json.loads(user)
print(peopleJSON)
# print(people[1]['name'])
