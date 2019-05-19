import glob
import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from config import *

# PROCESS: Gets most recent csv data in the directory.
# RETURN: data frame object from csv data with dates converted to date objects.
def getMostRecentData():
    mostRecentCsv = max(glob.iglob(COMMON_ALL_FILE_SELECT + COMMON_DATA_SRC_CSV), key=os.path.getmtime)
    df = pd.read_csv(mostRecentCsv)
    df[COLUMN_DATE] = pd.to_datetime(format=COMMON_DATE_FORMAT, arg=df[COLUMN_DATE])   
    return df

# PROCESS: Gets the most recent payday from a given date
# PARAMS: date - date from which the most recent payday will be calculated.
#         df - dataframe containing the paydays.
# RETURN: date of most recent payday
def getLastPayday(date=datetime.now(),df=None):
    if df == None:
        return date
    df = df[df[COLUMN_CATEGORY] == CATEGORY_SALARY]
    df = df[df[COLUMN_DATE] >= date]
    return max(df[COLUMN_DATE])

# PROCESS: Gets expense data so far since last payday.
# RETURN: data frame object containing recent expense data.
def getRecentExpenseData(date=datetime.now()):
    df = getMostRecentData()
    lastPayday = getLastPayday(date, df)
    return df[df[COLUMN_DATE] >= lastPayday]