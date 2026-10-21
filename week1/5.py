price=input("多少钱：")
price=int(price)
count=input("数量：")
count=int(count)
total=price*count
if total>=100:
    total=total*0.8
elif total>=50:
    total=total*0.9
elif total>=30:
    total=total*0.95
else:
    total=total
print("总价为:",total)