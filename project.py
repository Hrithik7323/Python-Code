import pandas as pd
import numpy as py
import matplotlib.pyplot as plt

# dataset = pd.read_csv('cleaned.csv')
# print(dataset.head())       #show list of first 5 rows
# print(dataset.tail())       #show list of last 5 rows

# print(dataset.shape)        #show the size of data

# print(dataset.info())

# print(dataset['rating'].describe())

# print(dataset['uniprice'].describe())

# print(dataset.nunique())   #give the total no. of unique vales present in a column

# print(dataset.isnull().sum())     #checking the sum of null values


# FINDING ANSWER WITH THE DATA VISULAIZATIONS

# dataset = pd.read_csv('cleaned.csv')

# dataset.groupby('year')['amount'].count().plot(kind='bar',title='year wise sales')

# dataset.groupby('year')['amount'].sum().plot(kind='bar',title='year wise sales')

# dataset.groupby('year')['category'].count().plot(kind='bar',title='year wise sales')

# plt.xlabel("Year")
# plt.ylabel("No. of sales")
# plt.show()


#Q3
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# dataset=pd.read_csv("cleaned.csv")
# dataset2015_2018=dataset[(dataset["year"] >= 2015) & (dataset["year"]<= 2018)]

# dataset2015_2018.groupby("month")["rating"].count().plot(kind="bar",title="Year wise sales")
# plt.xlabel("Month")
# plt.ylabel("No. of Ratings")
# plt.show()


#Q4
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# dataset = pd.read_csv("cleaned.csv")
# dataset2015_2018 = dataset[(dataset["year"] >= 2015) & (dataset["year"] <= 2018)]

# dataset2015_2018.groupby('brand')['amount'].sum().plot(kind="bar", color="red", edgecolor="black", label="data")
# plt.legend()

# plt.xlabel("Brand", fontsize=12)
# plt.ylabel("Sum of Sales", fontsize=12)
# plt.title("Highest Selling Year Brand between 2015-2018", fontsize=18)

# plt.grid(axis="y", linestyle="--", alpha=0.5)
# plt.show()


# Q5
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# dataset = pd.read_csv("cleaned.csv")
# dataset2015_2018=dataset[(dataset["year"]>=2015) & (dataset["year"]<=2018)]

# dataset2015_2018.groupby("category")["year"].count().plot(kind="bar", color="green",edgecolor="black",label="data")
# plt.legend("data")

# plt.xlabel("Cagegory",fontsize=12)
# plt.ylabel("Sum of Sales", fontsize=12)
# plt.title("Highest Category sale between 2015-2018", fontsize=18)

# plt.grid(axis="y", linestyle="--", alpha=0.5)
# plt.show()



# Finding & Plotting the Top 10 Brands for Each Year Plot for 2016

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# dataset = pd.read_csv('cleaned.csv')

# fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# top_selling_2016 = dataset[dataset['year'] == 2016].groupby('brand')['rating'].count().sort_values(ascending=False).head(10)
# axs[0, 0].bar(top_selling_2016.index, top_selling_2016)
# axs[0, 0].set_title('Top selling products in 2016')
# axs[0, 0].tick_params(axis='x',rotation=45)

# plt.show()



# # Q4 What products sold the most in the three years 2016, 2017, 2018
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# dataset = pd.read_csv('cleaned.csv')

# fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# top_selling_2016 = dataset[dataset['year'] == 2016].groupby('brand')['rating'].count().sort_values(ascending=False).head(10)
# axs[0, 0].bar(top_selling_2016.index, top_selling_2016)
# axs[0, 0].set_title('Top selling Products in 2016')
# axs[0, 0].tick_params(axis='x', rotation=90)

# top_selling_2017 = dataset[dataset['year'] == 2017].groupby('brand')['rating'].count().sort_values(ascending=False).head(10)
# axs[0, 1].bar(top_selling_2016.index, top_selling_2017)
# axs[0, 1].set_title('Top selling Products in 2017')
# axs[0, 1].tick_params(axis='x', rotation=60)

# top_selling_2018 = dataset[dataset['year'] == 2018].groupby('brand')['rating'].count().sort_values(ascending=False).head(10)
# axs[1, 0].bar(top_selling_2016.index, top_selling_2018)
# axs[1, 0].set_title('Top selling Products in 2018')
# axs[1, 0].tick_params(axis='x', rotation=30)


# axs[1, 1].axis('off')

# plt.tight_layout()

# plt.show()



# x

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# dataset = pd.read_csv('cleaned.csv')

# dataset.groupby('category')['amount'].sum().sort_values(ascending=False).head(5).plot(kind='pie', autopct='%1.1f%%',title='Top 5 categeory, salespercentage=90')

# plt.show()


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('cleaned.csv')

dataset.groupby('brand')['rating'].count().sort_values(ascending=False).head(5).plot(kind='pie', autopct='%1.1f%%',title='Top 5 Brand wise salespercentage')


plt.show()

