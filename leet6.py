def fun():
    l1=[2,4,3]
    l2=[5,6,4]
    suml1=0
    suml2=0
    output=[]
    for i in l1:
        suml1=suml1*10+i
    for j in l2:
        suml2=suml2*10+j
    sum = suml1+suml2
    for k in str(sum):
        output.append(int(k))
    return list(reversed(output))

print(fun())
    
    
