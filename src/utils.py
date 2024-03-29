import os
import sys
import dill

import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression, Lasso,Ridge,ElasticNet
from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error

from src.exception import CustomException
from src.logger import logging

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e, sys)