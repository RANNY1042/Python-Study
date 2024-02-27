for value in range(1,6):
    print(value)

numbers = set(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

sequares = []
for value in range(1,11):
    sequares.append(value**2)

print(sequares)
print(value)

sequares =[value**2 for value in range(1,11)]  #list comprehension
print(sequares)

number = [number for number in range(1,21)]
print(number)

players =['charles','martina','michael','florence','eli']
print(players[0:3])

print(players[1:4])

print(players[-3:])

players =['charles','martina','michael','florence','eli']
print("Here are the first players on my team:")
for player in players[:3]:
    print(player.title())


my_list = [1,2,3,4,5,6,7,8]

print(my_list[::-1])
print(my_list[::-2])
print(my_list[::-3])

a = [1,2]
b = [3,4]
c = a+b
print(c)

e=c-b
print(e)