with open('./name.text',encoding='utf-8') as file:
    for line in file:
        print(line)
print('A')
print('B')

def add(a,b):
    return a+b

print(add(1,2))