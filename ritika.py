import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import warnings 
warnings.filterwarnings('ignore')


class Pie_Donut_chart:
    def Total_Medals(self):
        tm = pd.read_csv('C:\\Users\\ASUS\\OneDrive\\Desktop\\Tokyo-Olympics 2k21 Analysis Project\\Tokyo Medals 2021.csv')
        font1 = {'family':'serif','color':'blue','size':20}
        top_15_countries = tm['Country'][:15]
        top_15_total = tm['Total'][:15]
        wp = {'linewidth': 1, 'edgecolor' : 'green'}
        mycolors = ['Aquamarine','Bisque','BlueViolet','Lavender','Chartreuse','CornflowerBlue','Cornsilk','Crimson','Cyan','HotPink','AliceBlue','DeepSkyBlue','Gold','GreenYellow','Chocolate']
        figure = plt.figure(figsize=(15,10))
        wedges, texts, autotexts =plt.pie(top_15_total,labels=top_15_countries,colors= mycolors,shadow= True,autopct='%1.2f%%',counterclock=True,wedgeprops=wp,textprops=dict(color='magenta'))
        plt.legend(wedges,top_15_countries,title='Medals',loc='right',bbox_to_anchor = (-0.2,0.5))
        plt.setp(autotexts,size=8,weight='bold')
        plt.title('Pie Plot for Top 15 Countries - Rank By Total Medals',fontdict=font1,loc='right')
        plt.show()
    def Gold_Medals(self):
        tm = pd.read_csv('C:\\Users\\ASUS\\OneDrive\\Desktop\\Tokyo-Olympics 2k21 Analysis Project\\Tokyo Medals 2021.csv')
        font1 = {'family':'serif','color':'green','size':20}
        top_15_countries = tm['Country'][:15]
        top_15_gold_medal = tm['Gold Medal'][:15]
        wp = {'linewidth': 1, 'edgecolor' : 'GreenYellow'}
        explode = (0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0,0,0,0,0,0,0)
        mycolors = ['Aquamarine','Bisque','BlueViolet','Lavender','Chartreuse','CornflowerBlue','Cornsilk','Crimson','Cyan','HotPink','AliceBlue','DeepSkyBlue','Gold','GreenYellow','Chocolate']
        figure = plt.figure(figsize=(15,10))
        wedges, texts, autotexts =plt.pie(top_15_gold_medal,labels=top_15_countries,explode=explode,colors= mycolors,shadow= True,autopct='%1.2f%%',counterclock=True,wedgeprops=wp,textprops=dict(color='magenta'))
        plt.legend(wedges,top_15_countries,title='Medals',loc='right',bbox_to_anchor = (-0.2,0.5))
        plt.setp(autotexts,size=8,weight='bold')
        plt.title('Pie Plot for Top 15 Countries - Rank By Gold Medals',fontdict=font1,loc='right')
        plt.show()
    def Silver_Medals(self):
        tm = pd.read_csv('C:\\Users\\ASUS\\OneDrive\\Desktop\\Tokyo-Olympics 2k21 Analysis Project\\Tokyo Medals 2021.csv')
        font1 = {'family':'serif','color':'darkblue','size':20}
        top_15_countries = tm['Country'][:15]
        top_15_silver_medal = tm['Gold Medal'][:15]
        wp = {'linewidth': 1, 'edgecolor' : 'violet'}
        mycolors = ['Aquamarine','Bisque','BlueViolet','Lavender','Chartreuse','CornflowerBlue','Cornsilk','Crimson','Cyan','HotPink','AliceBlue','DeepSkyBlue','Gold','GreenYellow','Chocolate']
        figure = plt.figure(figsize=(15,10))
        wedges, texts, autotexts =plt.pie(top_15_silver_medal,labels=top_15_countries,colors= mycolors,shadow= True,autopct='%1.2f%%',counterclock=True,wedgeprops=wp,textprops=dict(color='magenta'))
        centre_circle = plt.Circle((0,0),0.75,fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
        plt.legend(wedges,top_15_countries,title='Silver Medals',loc='right',bbox_to_anchor = (-0.2,0.5))
        plt.setp(autotexts,size=8,weight='bold')
        plt.title('Donut Chart for Top 15 Countries - Rank By Siver Medals',fontdict=font1,loc='right')
        plt.show()
    def Bronze_Medals(self):
        tm = pd.read_csv('C:\\Users\\ASUS\\OneDrive\\Desktop\\Tokyo-Olympics 2k21 Analysis Project\\Tokyo Medals 2021.csv')
        font1 = {'family':'serif','color':'green','size':20}
        top_15_countries = tm['Country'][:15]
        top_15_silver_medal = tm['Gold Medal'][:15]
        wp = {'linewidth': 1, 'edgecolor' : 'violet'}
        mycolors = ['Aquamarine','Bisque','BlueViolet','Lavender','Chartreuse','CornflowerBlue','Cornsilk','Crimson','Cyan','HotPink','AliceBlue','DeepSkyBlue','Gold','GreenYellow','Chocolate']
        figure = plt.figure(figsize=(15,10))
        explode = (0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0,0,0,0,0,0,0)
        wedges, texts, autotexts =plt.pie(top_15_silver_medal,labels=top_15_countries,explode=explode,colors= mycolors,shadow= True,pctdistance=0.85,startangle=0, autopct='%1.2f%%',counterclock=True,wedgeprops=wp,textprops=dict(color='magenta'))
        centre_circle = plt.Circle((0,0),0.75,fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
        plt.legend(wedges,top_15_countries,title='Silver Medals',loc='right',bbox_to_anchor = (-0.2,0.5))
        plt.setp(autotexts,size=8,weight='bold')
        plt.title('Donut Chart for Top 15 Countries - Rank By Bronze Medals',fontdict=font1,loc='right')
        plt.tight_layout()
        plt.show()

