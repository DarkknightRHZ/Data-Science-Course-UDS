import os
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC
from sklearn import svm
from sklearn.model_selection import cross_validate
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, ExtraTreesRegressor
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.metrics import average_precision_score
#from numpy import loadtxt
#from keras.models import Sequential
#from keras.layers import Dense
#import pandas as pd
#import numpy as np

def predict_shopping_duration(param):
    rf_duration = pickle.load(open('RF_duration.pkl', 'rb'))

    return rf_duration.predict([[param[0],param[1],param[2],param[3],param[4],param[5],param[6],param[7],param[8],param[9],param[10]]])

def predict_shopping_amount(param):
    rf_amount = pickle.load(open('RF_amount.pkl', 'rb'))

    return rf_amount.predict([[param[0],param[1],param[2],param[3],param[4],param[5],param[6],param[7],param[8],param[9],param[10]]])

    
