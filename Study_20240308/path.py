# import os
# from pathlib import Path  

# path = Path('./aaa/a.txt')
# print(path)

# dir_path = Path('./aaa')
# print(os.path.isdir(dir_path))  #path에 파일이 존재하는지 확인


# for d in os.listdir():
#     print(d,os.path.isdir(d))
#     if '.txt' in d:
#         print('FOUND!')


# #경로를 끊어서 쓰는것 (파일 이름만 가져와서 쓰는것)
        
# print(Path('./aaa/b.txt').split())  #경로를 끊는법
# #['.','aaa','b.txt']


# print(os.path.split(Path('./aaa/b.txt')))

#파일 만들기
import os
from pathlib import Path
path = Path ('./aaa/aa.txt')
with open(path, 'w') as file:   #w와 a의 차이
    file.write('a\n')
    file.write('aa\n')
    file.write('aaa')


path = Path ('./aaa/aa.txt')
if path.exists(): #방어코드 
    with open(path) as file:
        for line in file:
            print(line)

try:
    with open(path) as file:
        for line in file:
            print(line)

except Exception as e :
    print(e)

