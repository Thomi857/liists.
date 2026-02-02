def fun(int):
    count = 0
    for i in range(1,int+1):
        if i % 7 ==0 or i%3==0 or i%5==0:
            count+=i
        else:
            continue

    return count

print(fun(7))