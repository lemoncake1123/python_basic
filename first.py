#print('Hello! study python')


#for num in range(1,21):
#    print(num,'mal training')



tp=0
ages=[22,21,17,32,4,28,19,8]

for age in ages:
    if age>=20:
        tp=tp+5000
    elif age>10:
        tp=tp+2000
    else:
        tp=tp+2500
print(tp)


ages=[22,21,17,32,4,28,19,8]
num=0
while num <3:
    for age in ages:
        if age>=20:
            tp=tp+5000
        elif age>10:
            tp=tp+2000
        else:
            tp=tp+2500
    num=num+1
    print(num,'times', tp)
