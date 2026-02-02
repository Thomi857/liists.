def fun():
    nums=[1,5,0,2,-3]
    product=1
    for i in nums:
        product*=i
    if product<0:
        return -1
    elif product>=1:
        return 1
    else:
        return 0

print(fun())