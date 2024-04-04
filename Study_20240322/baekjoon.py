#data = list(map(int,input().split()))

# s=list(map(int,(input().split())))
# n=len(s)
# print(n)
# print(s)
# v=input()
# result = list(s).count(v)  #s.count(v)
# if v in list(s):   #if(result>0): 
#     print(result)

# s = list(map(int,input().split()))
# n=len(s)
# print(n)
# print(s)

# v=int(input())

# print(s.count(v))

# v = int(input())
# result = s.count(v)
# print(result)

n=int(input())
s= list(map(int,input().split()))
v= int(input())

count = 0

for i in range(n):
    if s[i] == v:
        
        count += 1

print(count)