import random

class Dice :
    def __init__(self):
      print("주사위 던지기를 시작합니다.")

    def roll_dice(self,i,j):
      print(random.randrange(1,i+1))

D=Dice()
D.roll_dice(6,10)

D.roll_dice(10,10)

D.roll_dice(20,10)