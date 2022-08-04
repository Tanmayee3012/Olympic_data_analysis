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

class No_of_medals_idxia_won:
    def no_of_medals_of_idxia(self):  # Display the details of the Number of Medals Won by India
        df_idxia = df.loc[df['Country']=='India']
        print(df_idxia)
    def plot_no_of_medals_idxia(self): # Plot the graph of the Number of Medals Won by India
        fig,ax = plt.subplots(figsize = (20,10))
        idxices = 1 # Numbers of pairs of bars you want
        idx = np.arange(idxices) # Position of bars on x-axis
        wd = 0.3 #wd of bars
        df_idxia = df.loc[df['Country']=='India']
        ax.bar(idx, df_idxia['Gold Medal'], data=df_idxia, width=wd, color = '#C49133', label = 'Gold')
        ax.bar(idx+wd, df_idxia['Silver Medal'], data=df_idxia, width=wd, color = '#828A95', label = 'Silver')
        ax.bar(idx+2*wd, df_idxia['Bronze Medal'], data=df_idxia, width=wd,  color = '#914E24', label = 'Bronze')
        plt.title('Medals won by India in Tokyo Olympics', fontweight = 'bold', fontsize=20)
        plt.xlabel('India', fontsize = 10, fontweight = 'bold')
        plt.ylabel('No of Medals', fontsize = 10, fontweight = 'bold')
        plt.legend(fontsize = 20)
        plt.tick_params(axis='x', labelbottom=False)
        plt.tight_layout()
        plt.show()
    def display_dataset(self): # Display the Data Set Details
        print(df.shape)
        print(df['Country'].unique())
        no_of_countries = len(df['Country'].unique())
        print(no_of_countries)
        print(df)


# obj = No_of_medals_idxia_won()
# obj.no_of_medals_of_idxia()
# obj.plot_no_of_medals_idxia()
# obj.display_dataset()