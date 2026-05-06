# # A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple/normal method 
fruits = ('Apples', 'Oranges', 'Grapes', 'Apples')
# print(fruits, type(fruits))

# # Using a constructor
fruits2 = tuple(('Berries', 'Mangos', 'Guava'))
# print(fruits2, type(fruits2))

# Single value needs trailing comma
fruits2 = ('Berries',)
# print(fruits2)

# # # Get value
fruits2 = tuple(('Berries', 'Mangos', 'Guava'))
# print(fruits2[1])

# # # Can't change value
# fruits2[0] = 'Pears'

# # # Delete tuple
# del fruits2

# # # Get length
# print(len(fruits))


# # # A Set is a collection which is unordered and unindexed. No duplicate members.

# # # Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}
# print(fruits_set)
# print(fruits_set, type(fruits_set))

# # # Check if in set
# print('Banana' in fruits_set)
# print(fruits_set)

# # # Add to set
fruits_set.add('Banana')
# print(fruits_set)

# # # Remove from set
fruits_set.remove('Apples')

# # Add duplicate
fruits_set.add('Banana')
# print(fruits_set)

# # # Clear set
fruits_set.clear()
# print(fruits_set)

# # # Delete
del fruits_set
print(fruits_set)

# # print(fruits_set)
