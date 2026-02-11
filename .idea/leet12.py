# def fun():
#     x=27
#     z=10
#     sign=1 if z>=0 else -1
#     count=0
#     while x>=abs(z):
#         x-=abs(z)
#         count+=1
#     return count*sign

# print(fun())

users = ["guest","guest", "user", "admin"]

for u in users:
    users = [u for u in users if u != "guest"]
    # if u == "guest":
    #     users.remove(u)
print(users)