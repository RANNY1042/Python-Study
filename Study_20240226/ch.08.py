def greet_user(username):   #def greet_user(): 들여쓴 행은 모두 함수바디
    """단순한 인사말을 표시합니다."""
    print(f"hello, {username.title()}")
    username = 'kim'

input_name = 'jesse'
greet_user("jesse") #함수호출
input_name = 'kim' ### 값이 변경이 아니라 변수를 다시설정 
#help(greet_user)
#print(greet_user.__doc__) 