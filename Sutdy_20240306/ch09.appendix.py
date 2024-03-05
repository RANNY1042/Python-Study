class Shape:
    def __init__(self,base,height):
        self.__base = base 
        self.__height = height

    @property #decorator for getter 
    def get_base(self):
        return self.__base 
    
    @height.setter 
    def set_height(self,value):
        self.__height = value

def get_data():
    return 1,2,3

_,a,b = get_data()

a=[1,2,3]
b=[11,22,33]
mylist = [*a,*b]  ## 병합
print(mylist)

c = ['a','b']
z = zip(a,c)
print(list(z))

##getter, setter 를 정의하는데 decorator 사용

