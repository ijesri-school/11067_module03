# Ibrahim Jesri | 02/12/2019 #
# Butler Community College | IN 252 | CRN 11067 | Module 03 #

print('#BEGIN STRINGS EXERCISE#')
my_string = 'Python is wonderful!'
print(my_string)
print(my_string[4])
print(len(my_string))
my_age = 18
print('My string is:', my_string, 'and my age is:', my_age)
print('#END STRINGS EXERCISE#\n')

print('#BEGIN LISTS EXERCISE#')
names = ['Michael', 'Cesar', 'Tyler', 'Brennen', 'Cam', 'Callum', 'Grizzly']
print(names)
names.append('Justin')
print(names)
names.remove('Cam')
print(names)
print('#END LISTS EXERCISE#\n')

print('#BEGIN DICTIONARY EXERCISE#')
my_dictionary = {'Michael': 18, 'Cesar': 18, 'Tyler': 18, 'Brennen': 18, 'Cam': 16, 'Callum': 16, 'Grizzly': 16, 'Justin': 21}
print(my_dictionary['Michael'])
print('#END DICTIONARY EXERCISE#\n')

print('#BEGIN BRANCHING EXERCISE#')
grade = 70 # CHANGE THIS VALUE #
if grade >= 70:
  print('You have passed!')
else:
  print('You have failed. Go back and study!')
points = 40 # CHANGE THIS VALUE #
if points == 20:
  print('Congratulations! You have won a Key Chain!')
elif points == 40:
  print('Congratulations! You have won a Bare!')
elif points == 60:
  print('Congratulations! You have won a $100!')
else:
  print('Opps! You didn\'t win any points. You can try again, Good Luck!')
print('#END BRANCHING EXERCISE#\n')

# Ibrahim Jesri | 02/12/2019 #
# Butler Community College | IN 252 | CRN 11067 | Module 03 #