#Drawing a shape
print('  /-----')
print(' / |')
print('/__|')

#Data Types and Variables
character_name = 'Kimora Lee'
character_age ='35'
print('There was a lady named ' + character_name + ',')
print('She was ' + character_age  + ' years old')

character_name = 'Beyonce'
print('She liked the name ' + character_name + '')
print('She didnt like being ' + character_age +'')

#Strings and Variables
print('Giraffe\nAcademy')
phrase = 'Igbinedion University'
print(phrase + ' is cool')

#Strings, Variables and Fuctions
print(phrase.lower())
print(phrase.upper())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0])
print(phrase.index('I'))

print(phrase.replace('Igbinedion', 'Babcock'))

#Working with numbers
print(3*5+(4+4))
print(10%3)

my_num = 100
print(my_num)

print(str(my_num) + ' my favorite number')

from math import *
print(sqrt (50))
print(pow(3, 5))

my_num = -5
print(abs(my_num))
print(ceil(3.7))
print(round(5.6))

#Lists
friends = ['Kimora', 'Kim' , 'Pamela']
friends[1] = 'Beyonce'
print(friends[1])

#Functions with Lists
lucky_numbers = [4, 5, 6, 7, 8, 9]
friends = ['Kimora', 'Kim', 'Pamela', 'Angela']
friends.extend(lucky_numbers)
print(friends)

#Tuples
coordinates = (4, 5)
print(coordinates[0])

#Tules and Lists
coordinates = [(4, 5), (6, 7), (80, 34)]
print(coordinates)

#Fuction
def sayhi():
    print('Hello World')

sayhi()

def say_hi(name):
    print('Hello ' +  name)

say_hi('Kimora')
say_hi('LaLa') 

# Return Statement
def cube(num):
    return num*num*num

print(cube(4))

# If Statement
is_male = True
if is_male:
    print('You are a male')
else:
    print('You are not a male')

is_male = True
is_tall = True

if is_male or is_tall:
    print('You are male or tall or both')
else:
    print('You are neither male, nor tall')

is_male = False
is_tall = False

if is_male and is_tall:
    print('You are male or tall or both')

elif is_male and not(is_tall):
    print('You are short')

elif not(is_male) and is_tall:
    print('You are tall')

else:
    print('You are not male, nor tall')

# If Statement and Comparisons
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(300, 40, 5))

#Dictionaries
monthConvertions = {
    'Jan': 'January',
    'Feb': 'February',
    'Mar': 'March',

}

print(monthConvertions['Jan'])

#Loop
i = 1
while i <= 10:
    print(i)
    i += 1

print('Done with loop')

#For Loop
for letter in "Starlite Aviation":
    print(letter)

#For Loop
friends = ['Kimora, Adele, Subomi']
for friend in friends:
    print (friend)

#Exponent function
print(2**3)

#Function in Exponent function and for loop
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result =result * base_num
    return result

print(raise_to_power(2, 3))

#2DLists and nested for loop
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0],

]

print(number_grid[0][0])

#Translation
def translate(phrase):
    translation = ''
    for letter in phrase:
        if letter in 'AEIOUaeiou':
            translation = translation + 'g'
        else:
            translation = translation + letter
    return translation

print(translate(input('Enter a phrase'))) 

# The # sign means comment. used as prefix to make comments in code
#python aint finna run it. """""" also can be used.

#Try and except
try:
    number = int(input('Enter a number:'))
    print(number)
except:
    print('Invalid Input')

#Reading File.
employee_file = open('employees.txt', 'r')
print(employee_file.read())

employee_file.close()

