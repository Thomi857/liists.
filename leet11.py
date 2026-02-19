def fun():
    x=-6789
    sign=1 if x>=0 else -1
    result=int(str(abs(x))[::-1])*sign
    if result<-2**31 or result>2**31-1:
        return 0
    return result

print(fun())