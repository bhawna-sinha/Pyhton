print('Hello World')

name = input('What is your name? ')
print('Hello' + name)

#working with strings

first_name = 'Jamila'
surname = 'smith'


full_name = first_name +' ' + surname

print(full_name)
print(len(first_name))
print(len(surname))
print(full_name.endswith('Smith'))

#working with numbers

addition = 10 + 5
subtraction = 10 - 5
division = 10 / 5
multiplication = 10 * 5
modulus = 10 % 4

print(addition)
print(subtraction)
print(multiplication)
print(division)
print(modulus)

#working with bolleans

print(10<=10)
print(10>8)
print(0==0)
print(1>2)

#if statement

is_adult = False
age = 18

if is_adult:
    print("is adult")

if age >= 18:
    print('adult')  
else:
    print('not an adult') 



is_adult = False
age = 17

if is_adult:
    print("is adult")

if age >= 18:
    print('adult') 
else: 
    print('not an adult') 


#working with list

cars= ['BMW', 'toyota', 'mercedes']
print(len(cars))
print(cars)
print(cars[0])
print(cars[1])
print(cars[2])


#working with loops


cars = ['bmw', 'toyota', 'mercedes']

for car in cars:
    print(car)

for car in cars:
    if car == 'bmw':
        print(car.upper())
else:
    print(car.capitalize())   

#working with while loop

umber = 0

while number <= 10:
    print(number)


number = 0

while number <= 10:
    print(number)
    number = number + 1

number = 0

while number <= 10:
    print(number)
    number = number + 1
else:
    print('while loop ended and value of number is' + str(number))