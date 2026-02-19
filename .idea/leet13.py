def fun():
    digits=[9]
    sum=0
    output=[]
    for i in digits:
        sum=sum*10+i
    sum+=1
    for j in str(sum):
        output.append(int(j))
    return output

print(fun())
