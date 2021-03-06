print("========================================================================================")
#옆으로 합치기

import pandas as pd
import numpy as np

adf=pd.DataFrame({"x1":["A", "B", "C"], "x2": [1, 2, 3]})
print(adf)
print("========================================================================================")

bdf=pd.DataFrame({"x1":["A", "B", "D"], "x2": ["T", "F", "T"]})
print(bdf)
print("========================================================================================")

k=pd.merge(adf, bdf, how='left', on='x1')  #좌측 기준
print(k)



print("========================================================================================")

kk=pd.merge(adf, bdf, how='right', on='x1')   #우측 기준
print(kk)


print("========================================================================================")

kkk=pd.merge(adf, bdf,how='inner', on='x1')   #둘다 해당되는 값만 merge
print(kkk)

print("========================================================================================")

kkkk=pd.merge(adf, bdf,how='outer', on='x1')  #다 가져오고 없는값은 null값으로 처리
print(kkkk)

print("========================================================================================")
print(adf.x1.isin(bdf.x1))  #두 열의 값이 일치하면 T 아니면 F,값을 필터링 해서 join
a=adf[adf.x1.isin(bdf.x1)]
print(a)

print("========================================================================================")
aa=adf[~adf.x1.isin(bdf.x1)]    #위의 값은 제외하고 가져온다~
print(aa)

print("========================================================================================")

ydf=pd.DataFrame({"x1":["A", "B", "C"], "x2": [1, 2, 3]})
print(ydf)

zdf=pd.DataFrame({"x1":["B", "C", "D"], "x2": [2, 3, 4]})
print(zdf)
print("========================================================================================")

l=pd.merge(ydf, zdf)    #두개의 공통된 값만 조인, 이너조인
print(l)
print("========================================================================================")

ll=pd.merge(ydf, zdf, how='outer')    #전부 다 조인, 이너조인
print(ll)

lll=pd.merge(ydf, zdf, how='outer', indicator=True)    #전부 다 조인, 이너조인, 인디케이터는 어떻게 합쳐진지 보여주는 열이 생김
print(lll)

print("========================================================================================")
#레프트 온리 값만 가져오고, merge열을 드랍한다.
b=pd.merge(ydf, zdf, how='outer', indicator=True).query('_merge == "left_only"').drop(columns=['_merge'])
print(b)












