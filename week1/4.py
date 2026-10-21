height=float(input("身高（米）："))
weight=float(input("体重（公斤）："))
bmi=weight/(height*height)
print("BMI为:",bmi)
if bmi<18.5:
    print("偏瘦")  
elif bmi<24:
    print("正常") 
elif 24<=bmi<28:
    print("偏胖")
else:
    print("肥胖")