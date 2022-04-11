# -*- coding: utf-8 -*-
"""
Created on Aug 17 18:26:37 2020


"""
# pip install mysql-connector-python
import mysql.connector as mysql
import pandas as pd
import datetime
import time
import os

#####################################################################################################
#Purpose        -  This function will create a directory to store run artifacts
#Input   
#Path           -  Path of repo
#Output
#status         -  Status message indication the function status
#####################################################################################################

def create_dir(path):
    try :
    
        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H_%M_%S')
        
        
        _dir = os.path.join(path, 'Artifacts%s' % timestamp)

        # create 'dynamic' dir, if it does not exist
        if not os.path.exists(_dir):
            os.makedirs(_dir)
            return True,_dir
        else:
            return False,""
    except:
        return False,""

#####################################################################################################
#Purpose        -  This function will perform some task
#Input   
#df             -  Dataframe with probe inputs
#Output
#status         -  Status message indication the check status
#mal_probe_list -  List having Some output
#####################################################################################################
def get_db_connection(database_ip,database_port,database_user,database_password,database_name):
    
    try:
        
        conn = mysql.connect(user=database_user, password=database_password,
                                      host=database_ip, port=int(database_port),
                                      database=database_name)
        return "Connection successful",conn
    
    except:
        
        return "Error in connection",None
        
        
