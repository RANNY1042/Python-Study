
def describe_pet(pet_name,animal_type='dog') :  #default parameter
    """반려동물 정보를 표시합니다"""
    print(f"\n I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet()
describe_pet('harry')
describe_pet(pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

