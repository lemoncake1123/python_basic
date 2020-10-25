import pandas as pd

df= pd.DataFrame({"a" : [4 ,5, 6],
                  "b" : [7, 8, 9],
                  "c" : [10, 11, 12]},
                 index = [1, 2, 3])

print(df) #whole
print(df["a"]) #1. column
print(df.loc[1]) #1. row
print(df.loc[3, "a"]) #(3, 1)    row -> column
print(df.loc[[1,2], ["a", "b"]])

df= pd.DataFrame(
                    [[4, 7, 10],[5, 8, 11],[6, 9, 12]],
                    index=[1, 2, 3],
                    columns=['a', 'b', 'c'])   #columns indexing
print(df)

df= pd.DataFrame({"a" : [4 ,5, 6], "b" : [7, 8, 9], "c" : [10, 11, 12]},
                 index = pd.MultiIndex.from_tuples(
                                                    [('d',1),('d',2),('e',2)], names=['n','v']))   #using tuple - indexing

print(df)


#subset observations
#get some rows from a whole table
print(df[df.b > 7])    #values that are bigger than 7 in b-column


df= pd.DataFrame({"a" : [4 ,5, 6, 6],
                  "b" : [7, 8, 9, 9],
                  "c" : [10, 11, 12, 12]},
                 index = pd.MultiIndex.from_tuples(
                  [('d',1),('d',2),('e',2), ('e', 3)],
                names=['n','v']))   #using tuple - indexing
print(df)
print(df.drop_duplicates())    #del duplicated rows




df= pd.DataFrame({"a" : [4 ,5, 6], "b" : [7, 8, 9], "c" : [10, 11, 12]},
                 index = pd.MultiIndex.from_tuples(
                                                    [('d',1),('d',2),('e',2)], names=['n','v']))   #using tuple - indexing

print(df["b"] != 7)   #T/F
print(df[df["b"]!=7])    #rows that are not 7 in b-column

print(df.a.isin([5, 6])) # Are 5 and 6 in column a?, only list like values are allowed like [-]
print(df['a'].isin([5, 6]))  #same above. It is used not alphabet but korean etc..


import numpy as np
df= pd.DataFrame({"a" : [4 ,5, 6, 6, np.nan],
                  "b" : [7, 8, np.nan, 9, 9],
                  "c" : [10, 11, 12, np.nan, 12]},
                 index = pd.MultiIndex.from_tuples(
                  [('d',1),('d',2),('e',2), ('e', 3), ('e', 3)],
                names=['n','v']))   #using tuple - indexing

print(pd.isnull(df)) # finding null values
print(df['a'].isnull())#finding null values in a column
print(df['a'].isnull().sum())  # sum not nulls

#same with isnull
print(pd.notnull(df))
print(df['a'].notnull())
print(df.notnull().sum())

#[Logics]
#and,  or,   not,   xor,   any,        all
#&,    |,    ~,     ^,    df.any(),    df.all()
print(~df.a.notnull())   #example



import numpy as np
df= pd.DataFrame({"a" : [4 ,5, 6, 6, np.nan],
                  "b" : [7, 8, np.nan, 9, 9],
                  "c" : [10, 11, 12, np.nan, 12]},
                 index = pd.MultiIndex.from_tuples(
                  [('d',1),('d',2),('e',2), ('e', 3), ('e', 3)],
                names=['n','v']))   #using tuple - indexing


print(df)
print(df.tail(2))  #tail
print(df.head(2))  #head

print(df.sample(frac=0.3))   #% random sampling
print(df.sample(n=4))     #n-rows random sampling
print(df.iloc[:3])        # 0,1,2-th indexing (range) -> 0,1,2 are not name of rows


df = pd.DataFrame({'population': [59000000, 65000000, 434000, 434000, 434000, 337000, 11300, 11300, 11300],
                    'GDP': [1937894, 2583560 , 12011, 4520, 12128, 17036, 182, 38, 311],
                    'alpha-2': ["IT", "FR", "MT", "MV", "BN", "IS", "NR", "TV", "AI"]},
                    index=["Italy", "France", "Malta", "Maldives", "Brunei", "Iceland", "Nauru", "Tuvalu", "Anguilla"])
print(df)
print(df.nlargest(3, 'population'))   #France, Italy and Malta have a largest population among them.
print(df.nsmallest(3, 'population'))   #Nauru, Tuvalu and Anguilla have a smallest population among them.
