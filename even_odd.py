def is_even(num):
    if num%2 == 0:
        return True
    else:
        return False    


starting = 0
user_input = int(input("Limit : "))
print(type(user_input))
# while starting <= user_input:
#     if is_even(starting):
#         print(f"{starting} is even")
#     else:
#         print(f"{starting} is odd")
#     starting+=1    

for num in range(0,user_input):
    if is_even(num):
        print(f"{num} is even")
    else:
        print(f"{num} is odd")