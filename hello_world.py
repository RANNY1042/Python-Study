print("Hello Python world!")
name = 'ada lovelace'
print(name)
name

print(name.title())
print(name.upper())

first_name='ada'
last_name=' lovelace '
full_name=f"{first_name}\n\t{last_name.title()}!"
print(full_name)
print('language: \nptyhon\tjava')
print('python')

last_name.strip()

person='hyeran'
message='안녕하세요. 에릭, 오늘 파이썬 배워 보는 게 어떨까요?'
personmessage = f"{person}\t{message}"
print(personmessage)
personmessage

print(person.upper())
print(person)
print(person.title())


print("알베르트 아인슈타인,\"한 번도 실수한 적이 없는 사람은 한 번도 새로운 것에 도전해 본 적이 없는 사람이다.")

famous_person='\t알베르트 \n아인슈타인'
message='"한 번도 실수한 적이 없는 사람은 한 번도 새로운 것에 도전해 본 적이 없는 사람이다.'
famous_person_message=f"{famous_person},{message}"
print(famous_person_message)

print(famous_person.lstrip())
print(famous_person.rstrip())
print(famous_person.strip())

import this

bicycles = ['trek','cannodale','redline','specialized']
print(bicycles)

print(bicycles[0])

print(bicycles[0].title())

print(bicycles[1])
print(bicycles[3])

print(bicycles[-1])
print(bicycles[-2])
print(bicycles[-3])

message = f"My first bicycle was a {bicycles[0].title()}"

print(message)

family=["박재명","고금자","박혜란","박소영","박수완"]
print(family[0])
print(family[1])
print(family[2])
print(family[3])
print(family[4])

message=f"My family is five person {family[0],family[1],family[2],family[3],family[4]}"
print(famous_person_message)

transport = ["버스", "자가용", "택시", "지하철","오토바이"]
print(transport)
mylist = f"나는 혼다 {transport[4]}를 갖고 싶습니다."
print(mylist)

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0] = 'ducai'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)


brand=[]
brand.append('honda')
brand.append('yamaha')
brand.append('suzuki')
print(brand)

brand.insert(3,'ducati')
print(brand)

del brand[0]
print(brand)

popped_brand=brand.pop()
print(brand)
print(popped_brand)

motorcycles1=['honda','yamaha','suzuki']
last_owned=motorcycles1.pop()
print(f"The last motocycle I owned was a {last_owned.title()}")

first_owned = motorcycles1.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}")

motorcycles2=['honda','yamaha','suzuki']
motorcycles2.remove('suzuki')
print(motorcycles2)


#too_expensive = 'ducati'
#motorcycles2.remove(too_expensive)
#print(motorcycles2)
#print(f"\nA {too_expensive.title()} is too expensive for me.")

cars=['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

cars.sort(reverse = True)
print(cars)
print(sorted(cars))
print(len(cars))

for car in cars: #확장형 for문
    print(car)
    print(f"my car is a {car}")

for cars2 in cars:
    print('my car\n')
    for c2 in cars:
        print()
print("for문 종료")



