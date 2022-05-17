
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
import flask
import configparser
import logging
import pandas as pd
import numpy as np
import streamlit as st 
from sklearn.linear_model import LogisticRegression
from pickle import dump
from pickle import load
from flask import request
# Import code packages
import feature_utility as util

from flask import Flask
app = Flask(__name__)

@app.route('/api/v1/getQ/', methods=['GET'])
def getQ():
    model_obj, exec_status = util.load_model(model_path,model_name)
    CLMSEX = int(request.args.get('CLMSEX'))
    CLMINSUR = int(request.args.get('CLMINSUR'))
    SEATBELT = int(request.args.get('SEATBELT'))
    CLMAGE = int(request.args.get('CLMAGE'))
    LOSS = int(request.args.get('CLMAGE'))
    class_out=""
    data = {'CLMSEX':CLMSEX,'CLMINSUR':CLMINSUR,'SEATBELT':SEATBELT,'CLMAGE':CLMAGE,'LOSS':LOSS}
    sample_data = pd.DataFrame(data,index = [0])
    df = sample_data #util.get_sample_data()
    pred_list,exec_status = util.get_predictions(model_obj,df)
    if(exec_status):
        class_out=str(pred_list[0][0])
    else:
        class_out="UNCLASSIFIED"
    return "predicted class is "+ class_out

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
    app.run(debug=True, host = "0.0.0.0")
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
            data = {'CLMSEX':1,'CLMINSUR':1,'SEATBELT':1,'CLMAGE':1,'LOSS':10000}
            sample_data = pd.DataFrame(data,index = [0])
            df = sample_data #util.get_sample_data()
            pred_list,exec_status = util.get_predictions(model_obj,df)
            
            if exec_status:
                print("predicted class is "+ str(pred_list[0][0]))

       
        