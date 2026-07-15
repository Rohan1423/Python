import pandas as pd

df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9],[10,11,12]], columns=["A","B","C"], index=["x","y","z","xz"])
print(df.head(1))
print(df.tail())
print(df.index.tolist())
print(df.info())
print(df.describe())
print(df.nunique()) # unique value in each col
print(df['A'].unique())
print(df.shape)
print(df.size)

coffee = pd.read_csv('./Pandas/warmup-data/coffee.csv') # we can also paste the url directly
print(coffee)

# Accessing Data with Pandas
print(coffee)
print(coffee.head(6)) # to get top 6
print(coffee.tail()) #  to get bottom 5
print(coffee.sample(10,random_state=1)) # to get 10 random data & random_state makes "random" operations repeatable rather than truly different each time i.e it will give same random values
print(coffee["Day"])
print(coffee.Day)

# To Access specific values using loc and iloc
# .loc/.iloc[row,col]
print(coffee.loc[0:5,["Day","Units Sold"]])
print(coffee.loc[:])
print(coffee.iloc[0,0])
print(coffee.iloc[0:5,0:2])
print(coffee.iloc[1,1])

# Change index name 
coffee.index = coffee["Day"]
print(coffee)
print(coffee.loc[["Monday","Thursday"],["Day","Units Sold"]])

# Setting Data Fram Value 
coffee.loc[1:3,"Units Sold"]=10
print(coffee)

# To Access single  value using at and iat
print(coffee.at[0,"Units Sold"])
print(coffee.iat[0,0])

# Sort Data
print(coffee.sort_values("Units Sold"))
print(coffee.sort_values(["Units Sold", "Coffee Type"],ascending=False))
print(coffee.sort_values(["Units Sold", "Coffee Type"],ascending=[0,1]))

# Iterating over a Data frame with a for loop
for index, row in coffee.iterrows(): # loose some performance with this
    print(index)
    print(row)
    print(row["Units Sold"])
    print("\n\n\n\n\n\n\n\n")


bios = pd.read_csv("./Pandas/data/bios.csv")

# Filtering Data
print(bios.head())
print(bios.tail()) 
print(bios.loc[bios["height_cm"] > 215,['name','height_cm']])   
print(bios[(bios['height_cm'] > 215) & (bios['born_country']=='USA')])
print(bios[bios['name'].str.contains('keith|patrick',case =False)])
print(bios.query('born_country == "USA"' and 'born_city == "Seattle"'))

# Adding/Removing Columns from a Data Frame
coffee['price'] = 4.99  # adding new column
print(coffee)

import numpy as np # to use where condition

coffee['new_price'] = np.where(coffee['Coffee Type'] == 'Espresso', 3.99, 5.99)
print(coffee)

print(coffee.drop(columns = ['price'])) # show modified data without price column
print(coffee) # again it willl show all data i.e with price column

# To actually modify the original data we need to pass inplace=True
coffee.drop(columns=['price'],inplace=True) # this coffee = coffee.drop(columns=['price']) will also do same
coffee = coffee[['Day', 'Coffee Type', 'Units Sold', 'new_price']] # this will only keep these cols
print(coffee)

coffee_new = coffee # both of them points to the same memory so doing any changes in coffee_new will do those chages in the original coffee also
coffee_new['new_col'] = "new"
print(coffee_new)
print(coffee)

coffee_new = coffee.copy() # now doing changes in coffee_new will not affect the original coffee
coffee_new['new_col'] = "new"
print(coffee_new)
print(coffee)

coffee['revenue'] = coffee['Units Sold'] * coffee['new_price']
print(coffee)

# Rename Column
coffee.rename(columns={'new_price':'price'},inplace=True)
print(coffee)

# Some more Add/Remove
bios_new = bios.copy()
bios_new['first_name'] = bios_new['name'].str.split(' ').str[0] # this will split the string into two parts from where there is gap and after that it will store the 0 index i.e the value before the gap in this new col
print(bios_new.query('first_name == "Keith"'))

bios_new['born_datetime'] = pd.to_datetime(bios_new['born_date'],format="%Y-%m-%d")
print(bios_new)

bios_new['born_year'] = bios_new['born_datetime'].dt.year
print(bios_new[['name','born_year']])

# Adding Custom Column -> Applying Custom Functions
bios_new['height_category'] = bios['height_cm'].apply(lambda x: 'Short' if x < 165 else ('Average' if x < 185 else 'Tall'))
print(bios_new)

def categorize_athelete(row):
    if row['height_cm'] < 175 and row ['weight_kg'] < 70:
        return 'Lightweight'
    
    elif row['height_cm'] < 185 and row ['weight_kg'] <= 80:
        return 'Middleweight'
    
    else:
        return 'Heavyweight'
    
bios['Category'] = bios.apply(categorize_athelete, axis=1)    
print(bios)

# Merging & Concatenating Data
nocs = pd.read_csv('./Pandas/data/noc_regions.csv')

bios_latest = pd.merge(bios, nocs, left_on='born_country', right_on='NOC', how='left', suffixes=['_bios','_nocs'])
print(bios_latest)

bios_latest.rename(columns={'region':'born_country_full'},inplace=True)

print(bios_latest[bios_latest['NOC_bios'] == bios_latest['born_country_full']][['name','NOC_bios','born_country_full']])

# Concantenation
usa = bios[bios['born_country'] == 'USA'].copy()
print(usa)

gbr = bios[bios['born_country'] == 'GBR'].copy()
print(gbr)

new_data_combine = pd.concat([usa,gbr])
print(new_data_combine.head())
print(new_data_combine.tail())

results = pd.read_csv('./Pandas/data/results.csv')

combined_df = pd.merge(results, bios, on='athlete_id', how='left') # here we only passed  on='athlete_id' as this athlete_id is same in both left_on and right_on
print(combined_df)

# Handling Null Values
coffee.loc[[1,2], 'Units Sold'] = np.nan # it will make 0th & 1st row's Unit Sold col values as Nan
coffee.loc[[4,5], 'Coffee Type'] = np.nan # it will make 0th & 1st row's Unit Sold col values as Nan
print(coffee)

# To check which values are Nan
print(coffee.isna())
print(coffee.isna().sum())

coffee = coffee.fillna(1000) # fill the nan values with 1000
print(coffee)

# To Conditionally fill the Nan values
coffee = coffee.fillna(coffee['Units Sold'].mean())
print(coffee)

coffee['Units Sold'] = coffee['Units Sold'].interpolate() # interpolate -> if there's a pattern in the data it will continue that -> looks at the neighbour values
print(coffee)

# Drop the full rows or only that particular values which are Nan
print(coffee.dropna()) # it will delete all the rows having any Nan Value in any column 
print(coffee)

print(coffee.dropna(subset=['Units Sold'],inplace=True)) # subset ->  # it will delete only those rows whose Units Sold's column having Nan value
print(coffee)

# To get only those rows having any Nan value in Units Sold column
print(coffee[coffee['Units Sold'].isna()])

# To get only those rows having any Non-Nan value in Units Sold column
print(coffee[coffee['Units Sold'].notna()])

# Aggregating Data -> combine things, grouping things, use pivot table etc.
print(bios['born_city'].value_counts()) # it will count in born_city column which city is how many times eg. Budapest -> 1378
print(bios[bios['born_country']=='USA']['born_region'].value_counts().tail(25)) # it will count born_region column which region is how many times but only for USA born_country eg. New York -> 990

# groupby
print(coffee.groupby(['Coffee Type'])['Units Sold'].sum()) # it will group same coffee type then it will calculate the total sum of Units Sold for that particular coffee type
print(coffee.groupby(['Coffee Type'])['Units Sold'].mean()) # it will group same coffee type then it will calculate the mean of Units Sold for that particular coffee type

# agg function -> (aggregate) method is designed for: applying different aggregation functions to different columns in a single groupby() operation.
print(coffee.groupby(['Coffee Type','Day']).agg({'Units Sold':'sum','price':'mean'})) # it will group same coffee type and Days together then it will calculate the total sum of Units Sold and mean of the price for that particular coffee type

# Pivot -> rearranging data so that it becomes easier to read and analyze.
pivot = coffee.pivot(columns="Coffee Type", index='Day', values='revenue')
print(pivot)
print(pivot.loc['Monday','Latte'])
print(pivot.sum())
print(pivot.sum(axis=1))

bios['born_date'] = pd.to_datetime(bios['born_date'])
bios['month_born'] = bios['born_date'].dt.month
bios['year_born'] = bios['born_date'].dt.year
print(bios.groupby([bios['year_born'],bios['month_born']])['name'].count().reset_index().sort_values('name',ascending=False))

# Advanced Functionality
coffee['yesterday_revenue'] = coffee['revenue'].shift(2) # shift() -> move the values in the revenue column down by 2 rows
print(coffee)

coffee['pct_change'] = coffee['revenue'] / coffee['yesterday_revenue'] * 100
print(coffee)

coffee['cumulative_sum'] = coffee['revenue'].cumsum() # cumsum() -> Each value is the sum of the current value and all previous values
print(coffee)

latte = coffee[coffee['Coffee Type'] == 'Latte'].copy()
latte["Last_3_days_Units_Sold"] = latte['Units Sold'].rolling(3).sum() # rolling(3) -> Calculate the 3-row moving sum of the Revenue column
print(latte)

# rank() assigns a rank (position) to each value based on its order
bios['height_rank'] = bios['height_cm'].rank() # Smallest value gets Rank 1 by default
print(bios.sort_values(['height_rank'],ascending=False))
print(bios.sort_values(['height_rank']).sample(10)[['name','height_rank']]) # sample() -> Randomly selects 10 rows from the sorted DataFrame
