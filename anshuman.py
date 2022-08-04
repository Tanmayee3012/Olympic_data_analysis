import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import warnings

from pandas.io.parsers import read_csv 
warnings.filterwarnings('ignore')

class bar_graph:
    
    def total_medals(self):
        qr = pd.read_csv('C:\\Users\\ASUS\\OneDrive\\Desktop\\Tokyo-Olympics 2k21 Analysis Project\\Tokyo Medals 2021.csv')
        top_15_country_names = qr['Country'][:15]
        top_15_total_medals = 0
        top_15_total_medals += qr['Gold Medal'][:15]
        top_15_total_medals += qr['Silver Medal'][:15]
        top_15_total_medals += qr['Bronze Medal'][:15]

        idx = 15
        index = np.arange(idx)
        wd = 0.3
        fig,rsv = plt.subplots(figsize = (20,10))
        r0 = rsv.bar(index, top_15_total_medals, data=qr,width=wd,color = '#000D6B', label = 'Medals')

        plt.title('Total Medals won by top 15 Countries at Olympics', fontweight = 'bold', fontsize=25)
        plt.xlabel('Country Name', fontsize = 10, fontweight = 'bold')
        plt.ylabel('No of Medals', fontsize = 10, fontweight = 'bold')
        plt.legend(fontsize = 20)

        rsv.tick_params(axis='both', which='major', labelsize=15)

        rsv.bar_label(r0, padding=3)

        plt.xticks(index+wd/2,top_15_country_names,fontsize=8,rotation=45)
        plt.tight_layout()
        plt.show()

    def gold_medals(self):
        qr = pd.read_csv('C:\\Users\\ASUS\\OneDrive\\Desktop\\Tokyo-Olympics 2k21 Analysis Project\\Tokyo Medals 2021.csv')
        top_15_country_names = qr['Country'][:15]
        top_15_gold_medals = qr['Gold Medal'][:15]

        idx = 15
        index = np.arange(idx)
        wd = 0.3
        fig,rsv = plt.subplots(figsize = (20,10))
        r1 = rsv.bar(index, top_15_gold_medals, data=qr,width=wd,color = '#FCCF5B', label = 'Gold')

        plt.title('Gold Medals won by top 15 Countries at Olympics', fontweight = 'bold', fontsize=25)
        plt.xlabel('Country Name', fontsize = 10, fontweight = 'bold')
        plt.ylabel('No of Medals', fontsize = 10, fontweight = 'bold')
        plt.legend(fontsize = 20)

        rsv.tick_params(axis='both', which='major', labelsize=15)

        rsv.bar_label(r1, padding=3)

        plt.xticks(index+wd/2,top_15_country_names,fontsize=8,rotation=45)
        plt.tight_layout()
        plt.show()
        
    def silver_medals(self):
        qr = pd.read_csv('C:\\Users\\ASUS\\OneDrive\\Desktop\\Tokyo-Olympics 2k21 Analysis Project\\Tokyo Medals 2021.csv')
        top_15_country_names = qr['Country'][:15]
        top_15_silver_medals = qr['Silver Medal'][:15]

        idx = 15
        index = np.arange(idx)
        wd = 0.3
        fig,rsv = plt.subplots(figsize = (20,10))
        r2 = rsv.bar(index, top_15_silver_medals, data=qr,width=wd,color = '#C8C2BC', label = 'Silver')

        plt.title('Silver Medals won by top 15 Countries at Olympics', fontweight = 'bold', fontsize=25)
        plt.xlabel('Country Name', fontsize = 10, fontweight = 'bold')
        plt.ylabel('No of Medals', fontsize = 10, fontweight = 'bold')
        plt.legend(fontsize = 20)

        rsv.tick_params(axis='both', which='major', labelsize=15)

        rsv.bar_label(r2, padding=3)
        
        plt.xticks(index+wd/2,top_15_country_names,fontsize=8,rotation=45)
        plt.tight_layout()
        plt.show()
        
    def bronze_medals(self):
        qr = pd.read_csv('C:\\Users\\ASUS\\OneDrive\\Desktop\\Tokyo-Olympics 2k21 Analysis Project\\Tokyo Medals 2021.csv')
        top_15_country_names = qr['Country'][:15]
        top_15_bronze_medals = qr['Bronze Medal'][:15]

        idx = 15
        index = np.arange(idx)
        width = 0.3
        fig,rsv = plt.subplots(figsize = (20,10))
        r3 = rsv.bar(index, top_15_bronze_medals, data=qr,width=width,color = '#CD7F32', label = 'Bronze')

        plt.title('Bronze Medals won by top 15 Countries at Olympics', fontweight = 'bold', fontsize=25)
        plt.xlabel('Country Name', fontsize = 10, fontweight = 'bold')
        plt.ylabel('No of Medals', fontsize = 10, fontweight = 'bold')
        plt.legend(fontsize = 20)

        rsv.tick_params(axis='both', which='major', labelsize=15)

        rsv.bar_label(r3, padding=3)

        plt.xticks(index+width/2,top_15_country_names,fontsize=8,rotation=45)
        plt.tight_layout()
        plt.show()
        
    def all_medals(self):
        qr = pd.read_csv('C:\\Users\\ASUS\\OneDrive\\Desktop\\Tokyo-Olympics 2k21 Analysis Project\\Tokyo Medals 2021.csv')
        top_15_country_names = qr['Country'][:15]
        top_15_gold_medals = qr['Gold Medal'][:15]
        top_15_silver_medals = qr['Silver Medal'][:15]
        top_15_bronze_medals = qr['Bronze Medal'][:15]

        idx = 15
        index = np.arange(idx)
        fig,rsv = plt.subplots(figsize = (20,10))
        wd = 0.3
        r1 = rsv.bar(index, top_15_gold_medals, data=qr,width=wd,color = '#FCCF5B', label = 'Gold')
        r2 = rsv.bar(index+wd, top_15_silver_medals, data=qr,width=wd,color = '#C8C2BC', label = 'Silver')
        r3 = rsv.bar(index+wd+wd, top_15_bronze_medals, data=qr,width=wd,color = '#CD7F32', label = 'Bronze')

        plt.title('All Medals won by top 15 Countries at Olympics', fontweight = 'bold', fontsize=25)
        plt.xlabel('Country Name', fontsize = 10, fontweight = 'bold')
        plt.ylabel('No of Medals', fontsize = 10, fontweight = 'bold')
        plt.legend(fontsize = 20)

        rsv.tick_params(axis='both', which='major', labelsize=15)

        rsv.bar_label(r1, padding=3)
        rsv.bar_label(r2, padding=3)
        rsv.bar_label(r3, padding=3)

        plt.xticks(index+wd/2,top_15_country_names,fontsize=10,rotation=45)
        plt.tight_layout()
        plt.show()


