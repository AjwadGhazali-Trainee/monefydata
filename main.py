import pandas as pd
import numpy as np
import glob
import os
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def recentPayday(date, payday):
    thisPayday = date - relativedelta(months=0, day=payday)
    lastPayday = date - relativedelta(months=1, day=payday)
    if (date - thisPayday).days >= 0:
        return thisPayday
    return lastPayday

def recentPayday(payday):
    return recentPayday(datetime.now(), payday)

def strToDate(str):
    return datetime.strptime(str, '%Y/%m/%d')


