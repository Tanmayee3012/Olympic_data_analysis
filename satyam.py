# Importing Modules
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

# Reading the Data-Set Contained in the Same Folder
df = pd.read_csv(
    "C:\\Users\\ASUS\\OneDrive\\Desktop\\Tokyo-Olympics 2k21 Analysis Project\\Tokyo Medals 2021.csv")


class DataAnalysis:
    def PrintDataframe(self, rows):  # Displaying the Specified Number of rows in Data-frame
        print(df.head(rows), " \n")

    def ShapeDataframe(self):  # Displaying the total Rows and Columns of Of the Data set
        print(df.shape, " \n")

    def Columns(self):  # Displaying the total Columns
        print(df.columns, " \n")

    def Info(self):  # Display the Info about the data
        print(df.info, " \n")

    def isNull(self):  # Checking for Null values in the data set
        print(df.isnull().sum(), " \n")

    def Describe(self):  # Displaying the Detailed Statistical Analysis of the Data Set
        print(df.describe(), " \n")

    def Histogram(self):  # Displaying the Histogram Plot of the Data Set
        f, ax = plt.subplots(figsize=(20, 5))
        print(sns.distplot(df['Total']))
        plt.xlabel("Density")
        plt.ylabel("Total Medals")
        plt.title("Histogram for Total medals")
        plt.show()

    def Kde(self):  # Displaying the KDE Plot of the probability density of the Data Set
        f, ax = plt.subplots(figsize=(20, 5))
        sns.kdeplot(df['Total'])
        plt.xlabel("Total Medals")
        plt.ylabel("Density")
        plt.title("KDE Plot for Total medals")
        plt.show()

    # Displaying the first 10 Countries in order of decreasing Total Medals
    def disCountries(self):
        print(df['Country'].value_counts().index[:10])

    def heatMap(self):  # Displaying the Correlation HeatMap of the Data Set
        plt.figure(figsize=(10, 10))
        heatmap = sns.heatmap(df.corr(), annot=True)
        heatmap.set_title('Correlation Heatmap', fontdict={
                          'fontsize': 12}, pad=12)
        plt.show()

    def ScatterPlot(self):  # Displaying the Scatter Plot of the Data Set
        plt.figure(figsize=(20, 200))
        x = np.array(df['Total'])
        x = x[:30]
        y = np.array(df['Country'])
        y = y[:30]
        colors = np.random.randint(30, size=(30))
        plt.scatter(x, y, c=colors, cmap='nipy_spectral')
        plt.colorbar()
        plt.show()

    def swarmPlotT(self): # Displaying the Swarm Plot for the Total Medals in the Data Set
        plt.figure(figsize=(20, 10))
        sns.swarmplot(x='Total', y='Country', hue='Country', data=df[:30])
        plt.show()

    def swarmPlotG(self): # Displaying the Swarm Plot for the Gold Medals in the Data Set
        plt.figure(figsize=(20, 10))
        sns.swarmplot(x='Gold Medal', y='Country', hue='Country', data=df[:30])
        plt.show()

    def swarmPlotS(self): # Displaying the Swarm Plot for the Silver Medals in the Data Set
        plt.figure(figsize=(20, 10))
        sns.swarmplot(x='Silver Medal', y='Country',
                      hue='Country', data=df[:30])
        plt.show()

    def swarmPlotB(self): # Displaying the Swarm Plot for the Bronze Medals in the Data Set
        plt.figure(figsize=(20, 10))
        sns.swarmplot(x='Bronze Medal', y='Country',
                      hue='Country', data=df[:30])
        plt.show()

    def barPlot(self): # Bar Plot of the Total Medals of all Countries
        plt.figure(figsize=(20,20))
        plt.tight_layout()
        plt.yticks(fontsize=5)
        sns.barplot(x='Total', y='Country', data=df)
        plt.title('All countries by medals')
        plt.show()


