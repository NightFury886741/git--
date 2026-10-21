for x in range(100,999):
    m=x//100
    n=x%100//10
    p=x%100%10
    if x==m**3+n**3+p**3:
        print(x,"是水仙花数")