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

class Medals_display:
    def Top_15_Gold(self): # Displaying the top 15 Countries which have maximum Gold medals
        plt.figure(figsize=(20, 10))
        plt.tight_layout()
        sns.barplot(x='Gold Medal',y='Country',color = '#D1B000',data=df[:15])
        plt.title('Distribution of Gold Medals')
        plt.show()

    def Top_15_Silver(self): # Displaying the top 15 Countries which have maximum Silver medals
        plt.figure(figsize=(20, 10))
        plt.tight_layout()
        sns.barplot(x='Silver Medal',y='Country',color = '#828A95',data=df[:15])
        plt.title('Distribution of Silver Medals')
        plt.show()

    def Top_15_Bronze(self): # Displaying the top 15 Countries which have maximum Bronze medals
        plt.figure(figsize=(20, 10))
        plt.tight_layout()
        sns.barplot(x='Bronze Medal',y='Country',color = '#914E24',data=df[:15])
        plt.title('Distribution of Bronze Medals')
        plt.show()


# ob = Medals_display()
# ob.Top_15_Bronze()
# ob.Top_15_Gold()
# ob.Top_15_Silver()