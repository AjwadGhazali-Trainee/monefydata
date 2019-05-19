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
        return thisPayday.replace(hour=0,minute=0,second=0,microsecond=0)
    return lastPayday.replace(hour=0,minute=0,second=0,microsecond=0)

def getMostRecentCsv():
    return max(glob.iglob("*.csv"), key=os.path.getmtime)

budgetStructure = {
    'daily' : 0.5,
    'wants' : 0.23,
    'emergency' : 0.15
}

monthly = ['House', 'Laundry', 'Phone', 'Netflix', 'Spotify']
daily = ['Food', 'Transport', 'Eating out', 'Communications', 'Health']
wants = ['Gift', 'Gifts', 'Entertainment', 'Clothes', 'Sports', 'Haircut', 'Book', 'Pets']

df = pd.read_csv(getMostRecentCsv())

recentPayday = recentPayday()

df['date'] = pd.to_datetime(format="%d/%m/%Y",arg=df['date'])

df = df[df['date'] >= recentPayday]

print(df[df['category'].isin(daily)])