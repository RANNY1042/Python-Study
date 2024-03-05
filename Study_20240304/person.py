class Person : 
    def __init__(self,name,age,address):
        self.name=name
        self.age = age
        self.address = address
        self.weight = [65,67,70,71]    #공개 속성
        self.height = 170
        self.__vision = 1.0   #private 속성
        print("{}객체가 생성됨".format(self.name))

    def __call__(self):
        return self.weight / self.heigt **2

    def  __len__(self):
        return len(self.weight)

    def show_person_vision(self):
        print("시력은 {}".format(self.__vision))

    def __eq__(self,other):
        return self.address == other.address

    def __str__(self): #Person은 객체 출력시 필요한것은 string
        return "{}\t{}\t{}".format(self.name,self.age,)

    def __getitem__(self, indx):
        return self.weight[indx]
    
    @classmethod  ##decorator    / 자바용어는 annotation
    def printing(cls):
        print("객체수는 {}".format(cls.count)) 

    def __del__(self):
        print("객체 {}이 소멸됨".format(self.name))
        Person.count += 1  

Person('guest',11,'jeju')

new_person = Person('hong',20,'busan')
otehr_person = Person('kim',30,'masan')
Person.printing() ##클래스 메소드 호출
new_person.printing()

print(f'Person 객체의 나이는**{new_person.age:5}***')
print("객체의 타입은{}".format(isinstance(new_person,Person)))
print(f"현재 체중은 {new_person[2]}")
print(f"{otehr_person.count} 객체가 생성됨")