# with open('name.text',encoding='utf-8') as file:
      txt.read
#     for line in file:
#         print(line)


# print('A')
# print('B')

# def add(a,b):
#     return a+b

# print(add(1,2))


import csv
with open('grade.csv') as file:
   reader=csv.reader(file,delimiter=',')
   for line in reader:
      print(line)
      