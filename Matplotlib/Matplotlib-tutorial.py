import matplotlib.pyplot as plt
import pandas as pd

# Line Plot
x =[1,2,3]
y =[4,5,6]

# plt.plot(x,y)
# plt.grid()
# plt.show()

# Pyplot API

# Univariate(1-Column) - Numercial - Line Plot, Histogram, Box Plot
data = {
    "Salary" : [25000,30000,37000,28000,39000,48000,55000,52000,35000,26000,27000,31000,20000,22000,24000,30000,25000,18000,20000,22000]
}

df = pd.DataFrame(data)
print(df.head())
print(df.shape)
# plt.plot(df['Salary'],color='red',marker='*',linestyle=':',linewidth='2')
# plt.grid()
# plt.show()

# # Histogram
# plt.hist(df['Salary'])
# plt.show()

# plt.hist(df['Salary'],bins=5,color='green')
# plt.grid()
# plt.show()

# Box Plot
# plt.boxplot(df['Salary'])
# plt.show()

df.loc[20] = [0] # Outlier (extreme value -> smaller than min / larger than max)

# plt.boxplot(df['Salary'])
# plt.show()

df.drop(index=20, inplace=True)

# Univariate(1-Column) - Categorical - Pie Chart, Count Plot
df['dept'] = ['HR','IT','Finance','HR','Finance','IT','HR','Finance','IT','HR']*2 # *2 means 10 ele x2 = total 20 ele
print(df.head())

# Pie Chart 
count = df['dept'].value_counts()
print(count)

# plt.pie(count,labels=count.index,autopct="%1.1f",explode=[0,0.1,0]) # explode -> to separate any particular section explode=[HR,IT,Finance] her IT is separated by 0.1 distance
# plt.axis('equal') # if u think ur pie chart is not a complete circle then this will make it
# plt.show()

# Count Plot
# plt.bar(count.index,count,color=['green','black','red'])
# plt.show()

# Bivariate(2-Column) - Numerical - Scatter Plot, Line Plot, Bar Plot
df['Age'] = [22,25,29,24,30,35,40,36,28,22]*2 # *2 means 10 ele x2 = total 20 ele
print(df.head())

# TO VISUALIZE SALARY AND AGE COLUMN

# Scatter Plot
# plt.scatter(df['Age'],df['Salary'],color='orange') # positive corelation -> when age and salary are increasing together
# plt.show()

# Line Plot
# plt.plot(df['Age'],df['Salary'],color='yellow',marker='o',linewidth='2') # will not be very easy to understand as Age values are not sorted and are passed randomly in data
# plt.grid()
# plt.show()

sort_age = df.sort_values('Age')
# plt.plot(sort_age['Age'],df['Salary'],color='yellow',marker='o',linewidth='2') # will be easy to understand as Age values are now sorted
# plt.grid()
# plt.show()

# Bar Plot
# plt.bar(sort_age['Age'],df['Salary'],color='green',align='edge')
# plt.show()

# # Bivariate(2-Column) - Numerical - categorical - Box Plot, Pie Chart, Bar Plot
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

plt.pie(salary_by_dept,labels=salary_by_dept.index,autopct='%1.2f')
plt.axis('equal')
plt.show()

# Bar Plot
hr_mean = sum(hr_sal)/len(hr_sal)
it_mean = sum(it_sal)/len(it_sal)
fin_mean = sum(fin_sal)/len(fin_sal)

plt.bar(['HR','IT','Finance'],[hr_mean,it_mean,fin_mean],color=['green','black','red'])
plt.grid()
plt.show()