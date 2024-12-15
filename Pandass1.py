import pandas as pd

#========== Series ===================================

# import pandas as pd
# hrithik = [1, 2, 3, 4, 5]
# new_hrithik = pd.Series(hrithik)
# print(new_hrithik)

# ####  Using Indexing
# import pandas as pd
# hrithik = [1, 2, 3, 4, 5]
# new_hrithik = pd.Series(hrithik, index=['a','b','c','d','e'])
# print(new_hrithik)

# ### Labling == Use to access a specified element
# import pandas as pd
# hrithik = [1, 2, 3, 4, 5]
# new_hrithik = pd.Series(hrithik, index=['a','b','c','d','e'])
# print(new_hrithik)
# print(new_hrithik['c'])

# ### Dictionary
# hrithik={
#     'day1':2000,
#     'day2':2500,
#     'day3':3000
# }
# new_hrithik=pd.Series(hrithik)
# print(new_hrithik)

# ### Using Indexing Dictionary
# hrithik={
#     'day1':2000,
#     'day2':2500,
#     'day3':3000
# }
# new_hrithik=pd.Series(hrithik,index=['day1','day3'])
# print(new_hrithik

#======== Data Frame ================================

 ## Data Frame      Data set in Pandas are usally multidemsionall table and they are called dataframe
 # its is 2D array
 # Series are like columes and Dataframe is hole table
# create two Data frame

# hrithik={
#     "cal":[400,200,500,600],
#     "dur":[500,900,100,300]
# }
# new_hrithik=pd.DataFrame(hrithik)
# print(new_hrithik)

# locate Row -> loc attribute

hrithik={
    "cal":[400,200,500,600],
    "dur":[500,900,100,300]
}
new_hrithik=pd.DataFrame(hrithik)
print(new_hrithik.loc[3])

