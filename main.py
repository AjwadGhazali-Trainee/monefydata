import pandas as pd
import numpy as np
import glob
import os
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def recentPayday(date=datetime.now(), payday=24):
    thisPayday = date - relativedelta(months=0, day=payday)
    lastPayday = date - relativedelta(months=1, day=payday)
    if (date - thisPayday).days >= 0:
        return thisPayday
    return lastPayday

def strToDate(str):
    return datetime.strptime(str, "%Y/%m/%d")

def getMostRecentCsv():
    return max(glob.iglob("*.csv"), key=os.path.getmtime)

print(getMostRecentCsv())
