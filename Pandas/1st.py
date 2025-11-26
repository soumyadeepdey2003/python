import pandas as pd

a=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'] )
print(a)

DDS=pd.DataFrame({"names":["soumya","pranab","samit","rana"],"Marks":[100,35,78,92]})
print(DDS)
print(pd.concat([DDS,DDS]))
print(pd.merge(DDS,DDS,on="names"))
d1=pd.read_csv("Pandas/data.csv")
print(d1)
print(d1.head())
print(d1.tail())
print(d1.describe())
print(d1.info())
print(d1["Pulse"])
print(type(d1["Pulse"]))

print(d1[["Pulse","Calories"]])

for i in range(0,20):
    print(d1.iloc[i])


# This help Drop all the Blank Data entry related row
print(d1.dropna())
# Fillna Is a function through which we can Fulfil The blank spaces in the CSV file But if we do inplace is equal to true then it originally reflects the change into the original File but if you don't write 
# inplace is equal to true then It will only use for the calculation of us but not directly reflect on the file
d1.fillna(d1.mean(),inplace=True)

d1["Zeros"]=[0 for i in range(len(d1))]
d1["Zeros"]=d1["Zeros"].astype(int)
def sum(a):
    return a+1

d1["Zeros+1"]=d1["Zeros"].apply(sum)
print(d1)

d1.to_csv("Pandas/result.csv")
d1.to_csv("Pandas/resultwithoutindex.csv",index=False)


