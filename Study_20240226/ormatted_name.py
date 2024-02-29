def get_formatted_name(first_name, middle_name, last_name) :
    """실제 이름을 깔끔한 형식으로 반환합니다"""
    if middle_name : #빈스트링이면 FALSE로 간주
        full_name = f"{first_name} {middle_name} {last_name}"
    else : 
        full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john','lee','hooker') 
print(musician)