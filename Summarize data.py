import pandas as pd
import seaborn as sns
import numpy as np

df=sns.load_dataset('iris')
print(df.shape)
print(df.head(2))   #show 2 rows

print("========================================================================================")
print(df['species'].value_counts())    #numbers of categorical data

print("========================================================================================")
print(len(df))      #150 rows
print(df.shape)     #(150rows, 5 columns)

print("========================================================================================")
print(df['species'].nunique())    #numbers of unique values

print("========================================================================================")
print(df.describe(include='all'))      #summary() in R
print(df.describe(include=[np.object]))      #summary() in R, showing only object-type
print(df.describe(include=[np.number]))      #summary() in R  only number


#sum()Sum values of each object.
#count()Count non-NA/null values of each object.
#median()Median value of each object.
#quantile([0.25,0.75])Quantiles of each object.
#apply(function)Apply function to each object.
#min()Minimum value in each object.
#max()Maximum value in each object.
#mean()Mean value of each object.
#var()Variance of each object.
#std()Standard deviation of each object.


print("========================================================================================")
print(df['petal_width'].sum())    #sum
print(df['petal_width'].count())    #counting
print(df['petal_width'].median())    #median
print(df['petal_width'].mean())    #mean
print(df.quantile([0.25, 0.75]))   #quantile
print(df.min())
print(df.max())
print(df.var())
print(df.std())

print("========================================================================================")
### apply function
print(df['species'].apply(lambda  x:x[:3]))   #extract 0~2th alphabets from the species column
df['species_3'] = df['species'].apply(lambda  x:x[:3]) #make a new column 'species_3'
print(df)



print("========================================================================================")
#example: make a new function that is 'lambda  x:x[:3]'
def smp(x):
    x=x[-3:]
    return x
df['species_4'] = df['species'].apply(smp)
print(df)

print("========================================================================================")


