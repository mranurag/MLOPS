#import the necessary libraries 

import pandas as pd
import numpy as np
import scipy.stats
from adtk.data import validate_series
from adtk.detector import LevelShiftAD
import datetime as dt
from sklearn import linear_model

# Import code packages
from log import get_logger
import DB_utilities as dbo

#import plotting parameters
import matplotlib.pyplot as plt
from matplotlib import dates as mpl_dates
from matplotlib.dates import DateFormatter
# Handle date time conversions between pandas and matplotlib
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()




#####################################################################################################
#Purpose        -  This function will save the plot file
#Input   
#df             -  Data to be plotted
#chk_flag       -  Plot is for individual column or whole dataframe
#col_name       -  Name of the column to plot
#file_name      -   Name of the plot file
#Output

#mal_probe_list -  List having names of malfunctioning probes
#####################################################################################################

def save_plot(df,chk_flag,col_name,file_name,plot_title,x_title,y_title):
    
    plt.rcParams["figure.figsize"] = (20,5)
    if not chk_flag:
        plt.plot_date(df.index,df[col_name],linestyle='solid')

        plt.gcf().autofmt_xdate()
        date_format = mpl_dates.DateFormatter('%d-%m-%Y')
        plt.gca().xaxis.set_major_formatter(date_format)
        
    else:
        df.plot()
    plt.title = plot_title
    plt.xlabel(x_title)
    plt.ylabel(y_title)
    plt.savefig(file_name)
        
    
    
