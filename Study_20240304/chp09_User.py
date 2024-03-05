class User:
    def __int__(self,first_name,lsat_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
      print("f저의 이름은{first_name}{last_name}입니다.")

    def greet_user(self):
      print("f{first_name}{last_name}님 환영합니다.")

name=User('Park','Hyeran')

describe_user()
