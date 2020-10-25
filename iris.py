import pandas as pd
import seaborn as sns

df = sns.load_dataset("iris")
print(df.head())

print(df[['sepal_width','sepal_length','species']])  #three columns

print(df['sepal_width'])  #one column
print(df.sepal_width)     #same above

print(df.filter(regex='_'))  #rows that have underbar '_' in their name
print(df.filter(regex='es$'))   #end by -es
print(df.filter(regex='^se'))   #begining with Sepal
print(df.filter(regex='^sp[1-5]$'))    #sp---1~5
print(df.filter(regex='^(?!species$).*'))    #except(-*) species

# '\.'              Matches strings containinga period'.'
# 'Length$'         Matches strings ending with word 'Length'
# '^Sepal'          Matches strings beginning with the word 'Sepal''  ' \
# '^x[1-5]$'        Matches strings beginning with 'x' and ending with 1,2,3,4,5
# '^(?!Species$).*'  Matches strings except the string 'Species'

print(df.loc[:, 'sepal_width':'petal_width'])  #all rows in columns between sepal_width and petal_width
print(df.iloc[-5:, [1,2,4]])                   #last 5 rows in 1,2,4 columns

#loc: iclude that index    2:5 = 2,3,4,5
#iloc: include that index - 1   2:5 = 2,3,4


print(df.loc[df['sepal_length'] > 3, ['sepal_length','sepal_width']])





