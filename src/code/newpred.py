
# -*- coding: utf-8 -*-
"""

"""

""" Import packages """

# Import system packages 
import warnings
warnings.filterwarnings('ignore')


# Import packages related system
import sys
sys.path.append('../utility/')
import os
import shutil
import time
import configparser
import logging
import pandas as pd
import numpy as np
import streamlit as st 
from sklearn.linear_model import LogisticRegression
from pickle import dump
from pickle import load

# Import code packages
import DB_utilities as dbo
import feature_utility as util


# Function to initialise all the global variables at the server startup
def initialise_vars_train():
    
    try:
        global output_path,input_path,model_path,log_path,model_name
        configParser = configparser.RawConfigParser()   
        configFilePath = '../../properties.yaml'
        configParser.read(configFilePath)
        output_path = configParser.get('hex_anomaly_detection','output_path')
        log_path = configParser.get('hex_anomaly_detection','log_path')
        model_path = configParser.get('hex_anomaly_detection','model_path')
        model_name  = configParser.get('hex_anomaly_detection','model_name')
        input_path = configParser.get('hex_anomaly_detection','input_path')
        
        
        
        return "Initialization complete"
    
    except Exception as e:
        return "Exception occured while initialisation "+ str(e)
    


# Main function call to launch the api. Api is running at port 5010
if __name__ == '__main__':
    str_response = initialise_vars_train()
    
    print(str_response)
    
    
    sts =True 
    status ="Success"
            
    if not sts:
        get_logger(logger,"Error",repo_path +" couldn't be created")
    elif status == "Error in connection":
        get_logger(logger,"Error","DB connection couldn't be established")
    
    else:
    
    
        #Loading the model
		
        model_obj, exec_status = util.load_model(model_path,model_name)
        
        if exec_status :
            df = util.get_sample_data()
            pred_list,exec_status = util.get_predictions(model_obj,df)
            
            if exec_status:
                print("predicted class is "+ str(pred_list[0][0]))

       
        