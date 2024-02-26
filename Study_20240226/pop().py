mortorcycles = ['honda','yamaha','suzuki'] 
print(mortorcycles)

popped_motorcycle= mortorcycles.pop()
print(mortorcycles)
print(popped_motorcycle)

last_owned = mortorcycles.pop()
print(last_owned)
print(f"The last motocycle I owned was a {last_owned.title()}.")

first_owned= mortorcycles.pop(0)
print(first_owned)
print(f"The first motorcycle I owned was a {first_owned.title()}")

customer = ["박예슬", "김미례", "최진향"]
customer[2]='박혜란'
print(customer)

popped_customer=customer.pop()
print(popped_customer)


print("더 큰 테이블을 찾았습니다.")

customer = ["박예슬", "김미례", "최진향"]
customer.insert(0,"박지수")
print(customer)

customer.insert(2,"이시은")
print(customer)

customer.append("탁희준")
print(customer)

#print(f"저희집에 놀러 오세요. 이번달 말에 {customer().title}님")

print(customer)
name = customer[0]
print(f"{name} 저희집에 놀러오세요 이번달 말에")

name= customer[1]
print(f"{name} 저희집에 놀러오세요 이번달 말에")

name = customer[2]
print(f"{name} 저희집에 놀러오세요 이번달 말에")

name = customer[3]
print(f"{name} 저희집에 놀러오세요 이번달 말에")

name= customer[4]
print(f"{name} 저희집에 놀러오세요 이번달 말에")

name = customer[5]
print(f"{name} 저희집에 놀러오세요 이번달 말에")

print("저녁식사에 손님 두명만 초대할 수 있습니다.")

popped_customer=customer.pop()
print(popped_customer)

print(customer)

customer.pop()
print(customer)

customer.pop()
print(customer)

customer.pop()
print(customer)

visit=customer[0]
print(f"{visit} 초대가 취소되지 않았으니, 방문해주세요")

visit=customer[1]
print(f"{visit} 초대가 취소되지 않았으니, 방문해주세요")

print(customer)
del customer[0]
print(customer)

del customer[1]
print(customer)