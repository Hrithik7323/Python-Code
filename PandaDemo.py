import pandas as pd
data={
    'name':["Hrithik","Ankit","Sachin"],
    'age':[24,22,25],
    'Salary':[50000,30000,80000]
}
df=pd.DataFrame(data)
print(df)

print("======================================")
#Accessing columes
print(df['name'])

print("======================================")
#Accessing rows
print(df.iloc[1])

print("=====================================")
#lable based indexing
print(df.loc[1,'name'])
print(df.loc[1,'age'])

print("======================================")
#Integer based Indexing
print(df.iloc[1,2])
print(df.iloc[0,1])

print("=====================================")
#Example for returning 0 to 1
import pandas as pd
data={
    'name':["Hrithik","Ankit","Sachin"],
    'age':[24,22,25],
    'Salary':[50000,30000,80000]
}
df=pd.DataFrame(data)
print(df.iloc[0,2])