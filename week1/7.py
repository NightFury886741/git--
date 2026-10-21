target=5025
count=0
while count<10:
    guess=int(input("猜数字："))
    count+=1
    if guess==target and count==1:
        print("狗运！")
        break
    elif guess==target and count<=3:
        print("运气不错")
        break
    elif guess==target and count<=5:
        print("运气一般")
        break
    elif guess==target and count<=10:
        print("今天别出门了")
        break
    elif guess>target:
        print("大了")
    elif guess<target:
        print("小了")
else:
    print("次数已用完，游戏失败，没救了！")