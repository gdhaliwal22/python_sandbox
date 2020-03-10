# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Create dictionary

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}


# Use contructor
person2 = dict(first_name='Sara', last_name='Williams')
print(person2, type(person2))


# Get value
print(person['first_name'])
print(person.get('last_name'))


# Add key/value
person['phone'] = '555-5555-5555'

print(person)
