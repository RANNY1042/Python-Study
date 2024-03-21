from random import randint

class Die:
    
    def __init__(self, num_sides=6):
        """6면체 주사위"""
        self.num_sides = num_sides
        
    def roll(self):
        """1에서 주사위 면 수 까지의 임의의 숫자를 반환합니다."""
        return randint(1, self.num_sides)
    