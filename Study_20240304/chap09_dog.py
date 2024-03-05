class Dog:
    """개를 표현하는 클래스"""

    def __init__(self,name,age) : 
        self.name = name  #속성 > 자바의 클래스 field
        self.age = age
        self._price = 100

    def sit(self):
        print(f"{self.name} is 앉기")   #클래스내에서는 self 

my_dog = Dog('Willie', 6)  #생성자 호출 > 인스턴스 생성 > __init__() 함수가 자동으로 호출
my_dog.sit()   #recieve object  클래스의 모든 메서드는 self를 지정하게함 

print(f"개이름은 {my_dog.name}+{my_dog._price}")   #클래스 밖에서는
your_dog = Dog('Lucy',3)
your_dog.sit()
print(f"너의 개는 {your_dog.name}")