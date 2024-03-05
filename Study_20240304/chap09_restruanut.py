class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name}은{self.cuisine_type}을 제공합니다.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name}이 문을 열었습니다.")  


DB_restaurant=Restaurant('COZYHOUS','Western')

DB_restaurant.open_restaurant()
DB_restaurant.describe_restaurant()

DB_restaurant.restaurant_name


class IceCreamStand(Restaurant):
    def __init__(self, name, ctype, flavors):
        super().__init__(name,ctype)
        self.flavors = flavors
    
    def show_flavors(self):
        print(f"맛이 {}".format(self.flavors))
        print(f"맛이 {self.flavors}")

new_reset = Restaurant()
ice_Cream = IceCreamStand('Italy','pizza','매운맛')
ice_Cream.show_flavors()

