import matplotlib.pyplot as plt
import pandas as pd

# Line Plot
x =[1,2,3]
y =[4,5,6]

plt.plot(x,y)
plt.grid()
plt.show()

# Pyplot API

# Univariate(1-Column) - Numercial - Line Plot, Histogram, Box Plot
data = {
    "Salary" : [25000,30000,37000,28000,39000,48000,55000,52000,35000,26000,27000,31000,20000,22000,24000,30000,25000,18000,20000,22000]
}

df = pd.DataFrame(data)
print(df.head())
print(df.shape)
plt.plot(df['Salary'],color='red',marker='*',linestyle=':',linewidth='2')
plt.grid()
plt.show()

# Histogram
plt.hist(df['Salary'])
plt.show()

plt.hist(df['Salary'],bins=5,color='green')
plt.grid()
plt.show()

# Box Plot
plt.boxplot(df['Salary'])
plt.show()

df.loc[20] = [0] # Outlier (extreme value -> smaller than min / larger than max)

plt.boxplot(df['Salary'])
plt.show()

df.drop(index=20, inplace=True)

# Univariate(1-Column) - Categorical - Pie Chart, Count Plot
df['dept'] = ['HR','IT','Finance','HR','Finance','IT','HR','Finance','IT','HR']*2 # *2 means 10 ele x2 = total 20 ele
print(df.head())

# Pie Chart 
count = df['dept'].value_counts()
print(count)

plt.pie(count,labels=count.index,autopct="%1.1f",explode=[0,0.1,0],shadow=True) # explode -> to separate any particular section explode=[HR,IT,Finance] her IT is separated by 0.1 distance
plt.axis('equal') # if u think ur pie chart is not a complete circle then this will make it
plt.show()

# Count Plot
plt.bar(count.index,count,color=['green','black','red'])
plt.show()

# Bivariate(2-Column) - 2 Numerical - Scatter Plot, Line Plot, Bar Plot
df['Age'] = [22,25,29,24,30,35,40,36,28,22]*2 # *2 means 10 ele x2 = total 20 ele
print(df.head())

# TO VISUALIZE SALARY AND AGE COLUMN

# Scatter Plot
plt.scatter(df['Age'],df['Salary'],color='orange') # positive corelation -> when age and salary are increasing together
plt.show()

# Line Plot
plt.plot(df['Age'],df['Salary'],color='yellow',marker='o',linewidth='2') # will not be very easy to understand as Age values are not sorted and are passed randomly in data
plt.grid()
plt.show()

sort_age = df.sort_values('Age')
plt.plot(sort_age['Age'],df['Salary'],color='yellow',marker='o',linewidth='2') # will be easy to understand as Age values are now sorted
plt.grid()
plt.show()

# Bar Plot
plt.bar(sort_age['Age'],df['Salary'],color='green',align='edge')
plt.show()

# Bivariate(2-Column) - 1 Numerical - 1 categorical - Box Plot, Pie Chart, Bar Plot
hr_sal = df[df['dept']=='HR']['Salary']
print(hr_sal)

it_sal = df[df['dept']=='IT']['Salary']
print(hr_sal)

fin_sal = df[df['dept']=='Finance']['Salary']
print(hr_sal)

# Box Plot
plt.boxplot([hr_sal,it_sal,fin_sal],label=['HR','IT','Finance'])
plt.legend()
plt.show()

# Pie Chart
salary_by_dept = df.groupby('dept')['Salary'].sum()
print(salary_by_dept)

plt.pie(salary_by_dept,labels=salary_by_dept.index,autopct='%1.2f',shadow=True,explode=[0.1,0,0.1])
plt.axis('equal')
plt.show()

# Bar Plot
hr_mean = sum(hr_sal)/len(hr_sal)
it_mean = sum(it_sal)/len(it_sal)
fin_mean = sum(fin_sal)/len(fin_sal)

plt.bar(['HR','IT','Finance'],[hr_mean,it_mean,fin_mean],color=['green','black','red'])
plt.grid()
plt.show()



# Multivariate(3-Column) - 3 Numerical - Bubble Plot
df['experience'] = [1,2,4,1.5,5,8,12,10,4,1,1.2,2,3,1.8,5.5,4.5,3.2,7,8,10]
print(df.head())

# Bubble Plot - same scatter plot - for 3rd Column(experience) it will define it using bubble
plt.scatter(df['Age'],df['Salary'],df['experience']*20,color='skyblue',edgecolor='black')
plt.title('Age vs Salary vs Experience')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.grid()
plt.show() # smallest bubble will show 1 year of experience and largest bubble will show 12 years of experience

# Multivariate(3-Column) - 2 Numerical - 1 Categorical - Scatter Plot
color = {'HR':'yellow','IT':'blue','Finance':'orange'}

for dept,color in color.items(): # dept -> 'HR' color -> 'yellow'
    df_dept = df[df['dept']== dept]
    plt.scatter(df_dept['Age'],df_dept['Salary'],c = color, label = dept)
plt.legend()
plt.show()



# Object-Oriented API
fig, axs = plt.subplots(1,3, figsize = (15,5)) # 1 -> figure 3 -> sub-plots (10,5) -> (x,y)


# Line Plot
axs[0].plot(sort_age['Age'],df['Salary'],color='red',marker='*',linewidth=2,markersize=2)
axs[0].grid()
axs[0].set_title('Line Plot')
axs[0].set_xlabel('Age')
axs[0].set_ylabel('Salary')


# Histogram
axs[1].hist(df['Salary'],bins=5,color='skyblue')
axs[1].set_title('Histogram')
axs[1].set_xlabel('Salary')
axs[1].set_ylabel('Frequency')


# Box Plot
axs[2].boxplot(df['Salary'])
axs[2].set_title('Box Plot')
axs[2].set_xlabel('Salary')
# To save a particular figure in my Environment -> run before plt.show()
plt.savefig('Multipleplots.png') # we can use any format/ we can define path also in file name
plt.show()

# Some more scenarios
dataa = {
    'Year' : [2020,2021,2022,2023],
    'Sales' : [100,150,200,250],
    'Profit' : [20,30,40,50],
    'Expenses' : [80,120,160,200]
}

# If we want to visualize Sales,Profit,Expenses all together with reference to the Year in one chart
df2 = pd.DataFrame(dataa)
plt.plot(df2['Year'],df2['Sales'],label='Sales') # x -> Year , y -> Sales
plt.plot(df2['Year'],df2['Profit'],label='Profit') # x -> Year , y -> Profit
plt.plot(df2['Year'],df2['Expenses'],label='Expenses') # x -> Year , y -> Expenses

plt.title('Financial Analysis')
plt.xlabel('Year')
plt.ylabel('Amount')
plt.legend()
plt.show()

# 3-D Plot
ax = plt.axes(projection='3d')

ax.scatter(df['Age'],df['Salary'],df['experience'])
ax.set_title('3-D Scatter Plot')
ax.set_xlabel('Age')
ax.set_ylabel('Salary')
ax.set_zlabel('Experience')
plt.show()