#import the necessary libraries 

import pandas as pd
import numpy as np
import scipy.stats
import datetime as dt
from sklearn import linear_model
from pickle import dump
from pickle import load

# Import code packages
from log import get_logger

#import plotting parameters
import matplotlib.pyplot as plt
from matplotlib import dates as mpl_dates
from matplotlib.dates import DateFormatter
# Handle date time conversions between pandas and matplotlib
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()



#####################################################################################################
#Purpose        -  This function will load the model from given path
#Input   
#model_path     -  model path
#model_name     -  Name of the model
#Output
#model_obj      -  Loaded model obj
#exec_status    -  execution status for the function

 
#####################################################################################################

def load_model(model_path,model_name):
    try:
    
        model_obj = load(open(model_path+model_name, 'rb'))
        
        return model_obj, True
    except:
        return None, False

#####################################################################################################
#Purpose        -  This function will make prediction and return result to client
#Input   
#model_obj      -  model Obj
#Output
#pred_list      -  Prediction result list
#exec_status    -  execution status for the function

 
#####################################################################################################

def get_predictions(model_obj,df):
    try:
        pred_list =[]
        
        #making predictions
        prediction = model_obj.predict(df)
        pred_list.append(prediction)
        prediction_proba = model_obj.predict_proba(df)
        pred_list.append(prediction_proba)
        
        return pred_list, True
    except:
        return None, False
        
        

#####################################################################################################
#Purpose        -  This function will generate sample data
#Input   
#Output
#sample_data      -  generated sample data
#exec_status    -  execution status for the function

 
#####################################################################################################

def get_sample_data():
    #create sample data
    data = {'CLMSEX':1,'CLMINSUR':1,'SEATBELT':1,'CLMAGE':1,'LOSS':10000}
    sample_data = pd.DataFrame(data,index = [0])
    return sample_data
    
        

#####################################################################################################
#Purpose        -  This function will save the plot file
#Input   
#df             -  Data to be plotted
#chk_flag       -  Plot is for individual column or whole dataframe
#col_name       -  Name of the column to plot
#file_name      -   Name of the plot file
#Output

#mal_probe_list -  
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
        
    
    
