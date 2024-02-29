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


e1=[x for x in a if x not in b]
e2=list(set(c)-set(b))
print(e1)
print(e2)

a = [10,20,30,40,50]
b1 = a    ## b=a ### shallow copy
b2 = a[0:3] #deep copy

print(b1)
print(b2)

a = [10,20,30,40,50]
b=a[0:3]
a[0]=100  #deep copy
print(b)

a = [[1,2,3],[4,5,6]]
b=a[:]
a[0][0] =100  #shallow copy
print(b)

my_foods = ['pizza','falafel', 'carrot cake']
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# list는 mutable이다.
#sequares = []
#sequares.append('car')

# tuple은 immutable이다.
#tuple(10,20)

dimensions = (10,20,30,40,50)
#print(dimensions[0])
#print(dimensions[1])
print(dimensions)
for dimension in dimensions:
    print(dimension)
dimensions = (200,50)

dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

#dimesions[0]=250

my_t = (3,)

dimensions = (200,50)
for dimension in dimensions:
    print(dimension)

dimensions = (200,50)
print("Original diemsions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
