
import json
data = '{"name":"Kim","age":23}'
member={"name":"Lee","age":24}

# with open('member2.json','w')as w_file:
#     json.dump(data,w_file)


d2 = json.dumps(member)
print(d2, type(d2))

d3 = json.loads(d2)
print(d3, type(d3). d3["name"])

import pickle

with open('dump_member.pk','w') as w_file:
    pickle.dump([1,2,3,4,5], w_file)

with open('dump_member.pk','rb') as r_file:
    data = pickle.load(r_file)



