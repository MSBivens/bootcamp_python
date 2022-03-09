# Variable Declaration 
num1 = 42
num2 = 2.3

# Data Type > Primitive > Boolean 
boolean = True

# Data Type > Primitive > String
string = 'Hello World'

# Data Type > Composite > List
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']

# Data Type > Composite > Dictionary
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

# Data Type > Composite > Tuple
fruit = ('blueberry', 'strawberry', 'banana')

# Type Check
print(type(fruit))

# Data Type > Composite > Dictionary > access value
print(pizza_toppings[1])

# Data Type > Composite > list > add value
pizza_toppings.append('Mushrooms')

# Data Type > Composite > Dictionary > access value
print(person['name'])

# Data Type > Composite > Dictionary > change value
person['name'] = 'George'
person['eye_color'] = 'blue'

# Data Type > Composite > Tuple > access value
print(fruit[2])

# Conditional > if, else
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

# Conditional > if, elif, else
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

# for loop
for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)

# Variable declaration, while loop
x = 0
while(x < 5):
    print(x)
    x += 1

# Data Type > Composite > list > delete value
pizza_toppings.pop()
pizza_toppings.pop(1)

# Data Type > Composite > Dictionary > delete value
print(person)
person.pop('eye_color')

# log statement
print(person)

# for loop, conditionals, continue
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

# Function > declaration
def print_hello_ten_times():
    for num in range(10):
        print('Hello')

# function > return
print_hello_ten_times()

# function > argument
def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

# function > return
print_hello_x_times(4)

# function > parameter
def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

# function > return
print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""
num3 = 72
print(num3)


fruit[0] = 'cranberry'
fruit.append('raspberry')
fruit.pop(1)

person.append("'favorite_team': Toronto Maple Leafs")
print(person['favorite_team'])

print(pizza_toppings[7])
    print(boolean)