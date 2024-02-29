
cars=['audi','bmw','subaru','toyota']

for car in cars:
    if car == 'bmw' :
        print(car.upper())
    else : 
        print(car.title())\

age = 12 
if age >= 18 :
    print('You are old enough to vote!')
else : 
    print('too young')

age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

age=12
if age < 4:
    print('입장료 $0')
elif age< 18:
    print('입장료 $25')
else :
    print('입장료 $40')

requsted_toppings = ['mushroom','green peppers','extra cheese']

for requested_topping in requsted_toppings:
    if requested_topping  == 'green peppers' :
        print("Sorry, we are out of green peppers right now.")
    else :
        print(f"Adding {requested_topping}.")

print("\nFinisehd making your pizza!")

availabe_toppings = ['mushrooms', 'olives','green peppers', 'pepperoni','pineapple','extra cheese']

requested_toppings = ['mushrooms','french fries','extra cheese']

for requested_tooping in requested_topping :
    if requested_topping in availabe_toppings :
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFineshed making your pizza")