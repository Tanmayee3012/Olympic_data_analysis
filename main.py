# Importing Modules
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

# Importing all the python files contaning the code
from ritika import *
from anshuman import *
from satyam import *
from soumalya import *
from tanmayee import *

obj = DataAnalysis()
obj.PrintDataframe(10)
obj.ShapeDataframe()
obj.Columns()
obj.Info()
obj.isNull()
obj.Describe()
obj.Histogram()
obj.Kde()
obj.disCountries()
obj.heatMap()
obj.ScatterPlot()
obj.swarmPlotT()
obj.swarmPlotG()
obj.swarmPlotS()
obj.swarmPlotB()
obj.barPlot()


k = bar_graph()
k.total_medals()
k.gold_medals()
k.silver_medals()
k.bronze_medals()
k.all_medals()

p1 = Pie_Donut_chart()
p1.Total_Medals()
p1.Gold_Medals()
p1.Silver_Medals()
p1.Bronze_Medals()



obj = No_of_medals_idxia_won()
obj.no_of_medals_of_idxia()
obj.plot_no_of_medals_idxia()
obj.display_dataset()


ob = Medals_display()
ob.Top_15_Bronze()
ob.Top_15_Gold()
ob.Top_15_Silver()