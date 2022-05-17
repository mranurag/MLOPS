<h1 align="center">Sample DS project setup</h1>


## Description
Analytical rule engine to analyze the condenser unit (Power plant) data in order to identify the probable issues and suggesting the next point of action to resolve these issues to ensure maximum productivity.  



## Contents of repository 
Important ingridents / must have
**src** : Contains model source code and api starting ponits

**Artifacts** : Contains all the generated feature artifacts

**notebook** : Contains all the ipython notebooks

**environment.yml** : Contains all the python dependancies

**properties.yaml** : Configuration properties file having key-value pairs


## Steps to run

### Setup the python virtual environment
Run below commands to execute environment.yml file

First command will create a virtual environment in which code in repo can be executed

Seconds command will activate the newly created vertual environment

> conda env create -f environment.yml

> conda activate anom_env


### Setup peroperties.yml

For configuration parameters properties.yml file is maintained having different sections.


### Feature calculation

#### From inside **/src/code**

- to run the feature calculation api
> python main.py

### Prediction 

#### From inside **/src/code**

 - to run the prediction,
 > python3 newpred.py


    

