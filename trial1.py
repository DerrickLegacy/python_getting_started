import math
name = input("Whats your name? ")
colour = input("Colour? ")
print(name + " likes " + colour)

sentence = "Hello Marry!"
copy_sentence = sentence[:]
print(copy_sentence)

# formatted string
first = 'John'
last = 'Jameson'

message = first + ' has ' + last + ' as his last name'
msg = f'{first}  has [{last}]  as his last name'

print(message)
print(msg)

# string methods
course = 'python for beginners'
print(len(course))
print(course.upper())
print(course.lower())
print(course.find('begginers'))  # returns the index of a character
print(course.replace('for', 'Advanced'))
print(course.title())
print('for' in course)

# arithmetic operators
print(10*3)
print(10**3)  # exponential
print(10/3)
print(10 % 3)

# math function
x = 2.9
print(abs(2.9))
print(math.ceil(x))
print(math.floor(x))

# if statement
is_hot = True
is_cold = True
if is_hot:
    print('It is hot day')
elif is_cold:
    print('Its a cold day')
else:
    print('It is cold day')
print('Enjoy your cold day')

price = 10000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1*price
else:
    down_payment = 0.2*price
print(f"Down payment: {down_payment}" )

# Logical operators- use and or operators
has_high_income = True
has_good_credit = True
has_no_permit = False
if has_high_income and has_good_credit:
    print('eligible')
    
if has_no_permit and not has_good_credit:
    print('eligible')
 
# comparison operators
# >, <, >=, <=