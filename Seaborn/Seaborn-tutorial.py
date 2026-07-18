import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

print(sns.get_dataset_names())
penguins = sns.load_dataset('penguins')
print(penguins.head())
print(penguins['species'].value_counts())
print(penguins['island'].value_counts())

# Scatter Plot
sns.set_style('ticks')
sns.set_context('notebook')
sns.scatterplot(data = penguins, x='flipper_length_mm', y='body_mass_g', hue='island',palette='Dark2') # hue='island' -> which penguin belongs to which island
sns.scatterplot(data = penguins, x='flipper_length_mm', y='body_mass_g', hue='sex') # hue='island' -> which penguin belongs to which sex
sns.despine(left=True) # the axis line hide and show
plt.show()

# Scatter Plot -> to visualize 2 features
sns.scatterplot(data=penguins, x='species', y='body_mass_g', hue='island',style='sex',alpha=0.5) # style will define sex between male and female
plt.show()                                                                                       # alpha -> it will decrease the opacity of the data points by default and wherever ther is an overlap, it is going to have a higher opacity of the data point

# Strip Plot -> gives better data spread than Scatter Plot
sns.stripplot(data=penguins, x='species', y='body_mass_g', hue='island', dodge=True,jitter=True) # dodge -> hue category spread jitter -> randomly spread data points horizontally 
plt.show()

# Swarm Plot -> gives a swarm shape to the data & this helps in reading data more efficiently
sns.set_context('talk')
sns.swarmplot(data=penguins, x='species', y='body_mass_g', hue='island')
sns.despine()
plt.show()

# Histogram -> to visualize only 1 feature
sns.histplot(data=penguins,x='body_mass_g',shrink=0.9, hue='sex',multiple='stack') # shrink -> means gap between the bars 1 means no gap
plt.show()                                                                         # multiple -> How should these sex categories be displayed?

# Regression Plot -> helps us to see the relationshiop b/w 2 variables & fits a regression line i.e a linear line via all data points
sns.regplot(data=penguins, x='body_mass_g', y='flipper_length_mm', scatter=False,color='red') # scatter=False -> data points will hide only line will show
plt.show()

# Line Plot
sns.set_style('whitegrid')
sns.lineplot(data=penguins, x='body_mass_g', y='flipper_length_mm', hue='island',style='sex') # style -> based on line style categorize
plt.show()

# Joint Plot -> combine two different plots
sns.jointplot(data=penguins, x='body_mass_g', y='flipper_length_mm') # scatterplot and histogram
sns.jointplot(data=penguins, x='body_mass_g', y='flipper_length_mm', hue='sex') # density plot
sns.jointplot(data=penguins, x='body_mass_g', y='flipper_length_mm', hue='island', kind='kde') # (Kernel Density Estimation) concentration of data points at a particular place
sns.jointplot(data=penguins, x='body_mass_g', y='flipper_length_mm', hue='island', kind='scatter')
sns.jointplot(data=penguins, x='body_mass_g', y='flipper_length_mm', kind='reg')
plt.show()

# Bar Plot
sns.barplot(data=penguins, x='species', y='body_mass_g', hue='sex', palette=['pink','skyblue'],estimator=np.sum) # estimator -> What calculation should I perform on the y-values before drawing each bar? By Default it is - np.mean
plt.show()

# Count Plot
sns.countplot(data=penguins, x='species', hue='island') # count each species
plt.show()

# Box Plot -> used for detecting Outliers -> (extremely low/extremly high) values in a particular (column/feature)
sns.boxplot(data=penguins, x='species', y='body_mass_g',hue='sex')
plt.show()

# Violin Plot -> Similar to Box Plot but this uses (KDE)
sns.violinplot(data=penguins, x='species', y='body_mass_g',hue='sex', split=True, inner='box') # split=True -> Display both hue categories within a single violin by splitting it into two halves. By default, each hue category is shown as a separate violin
plt.show()                                                                                     # inner -> Controls what appears inside the violin : box,quartile,None,point,stick

# Swarm Plot on Top of Violin Plot -> swarm plot inside violin plot
sns.violinplot(data=penguins, x='species', y='body_mass_g', palette='pastel')
sns.swarmplot(data=penguins, x='species', y='body_mass_g', color='black', hue='island', size=3, palette='dark')
plt.show() 

# KDE Plot -> it is a probability density function of continuous/non-parametric data (Smooth Version of Histogram) -> Helps to see where the data is concentrated (peaks) and how it spreads
sns.kdeplot(data=penguins,x='body_mass_g', hue='species', fill=True) # fill -> color inside each hue category line drawn
plt.show()

# Heatmap(Only Numerical Columns) -> 2-D color coded matrix that shows the relationships/patterns b/w 2 variables
print(penguins.head())
columns = ['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g']
sns.heatmap(data=penguins[columns].corr(),annot=True,cmap='Blues',vmin=-0.2, linewidth='2', linecolor='black') # corr -> co-relation -ve -> one increases another decreases and vice-versa
plt.show()                                                         # annot=True -> value label inside each box
                                                                   # vmin=-0.2 -> negative co-relation will start from -0.2

# Rug Plot -> adds small ticks/lines along the axis that we defines representing diff. data points. Generally used along with histograms,kde plots
sns.rugplot(data=penguins, y='body_mass_g', hue='species', palette='Set2', height=0.2)
plt.show()

# Pair Plot -> Grid of Plots that shows the relationship b/w all the numerical variables in a data frame
sns.pairplot(data=penguins[columns]) # even if we pass categorical/non-numerical columns it will automatically filters them
sns.pairplot(data=penguins, hue='sex', palette='Set2', diag_kind='hist') # even if we pass categorical/non-numerical columns it will automatically filters them
plt.show()                                                              # diag_kind='kde'/'hist' -> this will show the diagnol plots as kde/hist plot

# Pair Grid -> subplot Grid for plotting pairwise relationships in a dataset
graph = sns.PairGrid(data=penguins, hue='sex', palette='Set2')
graph.map_upper(sns.scatterplot) # upper triangle
graph.map_lower(sns.kdeplot) # lower triangle
graph.map_diag(sns.histplot) # diagnol
graph.add_legend()
plt.show()  