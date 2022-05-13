import json
user = '{"name":"kamal","age":"22","varsity":"diu"}'
print(user)

dict = json.loads(user)
print(type(dict))
print(dict)

for data in dict :
    print(data,dict[data])
