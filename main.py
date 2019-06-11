from config import BUDGET_LIST
from config import OVERALL_NET
from config import OVERALL_REMAIN
from config import SUGGESTED_PERDAY
from config import BUDGET_NAME
from config import BUDGET_ALLOCATION
from config import BUDGET_EXPECTED_EXPENSE
from config import BUDGET_ACTUAL_EXPENSE
from config import BUDGET_NET
from config import BUDGET_REMAIN
from datetime import datetime, timedelta	
from dateutil.relativedelta import relativedelta
import pandas as pd
import glob
import os

def main():
    # initializing inputs
    incomeList = getIncomeList()
    budgetList = getBudgetList()
    tranDf = getTransactionDataFrame()
    recentPayday = getRecentPayday()

    # filtering dataframe
    tranDf = tranDf[tranDf['date'] >= recentPayday]

    # initializing summary model
    summaryModel = {}
    summaryModel[BUDGET_LIST] = []
    summaryModel[OVERALL_NET] = 0
    summaryModel[OVERALL_REMAIN] = 0

    for budget in budgetList:
        # initializing budget analysis model
        budgetAnalysisModel = {}
        budgetAnalysisModel[BUDGET_NAME] = ''
        budgetAnalysisModel[BUDGET_ALLOCATION] = 0
        budgetAnalysisModel[BUDGET_EXPECTED_EXPENSE] = 0
        budgetAnalysisModel[BUDGET_ACTUAL_EXPENSE] = 0
        budgetAnalysisModel[BUDGET_NET] = 0
        budgetAnalysisModel[BUDGET_REMAIN] = 0
        budgetAnalysisModel[SUGGESTED_PERDAY] = 0

        # computations
        allocatedBudget = budget.allocation * getIncome(incomeList, tranDf)
        expectedExpense = getExpectedExpenseToDate(allocatedBudget, recentPayday, nextPayday)
        actualExpense = getActualExpense(budget.categoryList, tranDf)
        net = expectedExpense - actualExpense
        remainingBalance = allocatedBudget - actualExpense

        # saving budget analysis model
        budgetAnalysisModel[BUDGET_NAME] = budget.name
        budgetAnalysisModel[BUDGET_ALLOCATION] = allocatedBudget
        budgetAnalysisModel[BUDGET_EXPECTED_EXPENSE] = expectedExpense
        budgetAnalysisModel[BUDGET_ACTUAL_EXPENSE] = actualExpense
        budgetAnalysisModel[BUDGET_NET] = net
        budgetAnalysisModel[BUDGET_REMAIN] = remainingBalance
        budgetAnalysisModel[SUGGESTED_PERDAY] = remainingBalance/(nextPayday - datetime.now()).days

        # updating summary model
        summaryModel[BUDGET_LIST].append(budgetAnalysisModel)
        summaryModel[OVERALL_NET] += budgetAnalysisModel[BUDGET_NET]
        summaryModel[OVERALL_REMAIN] += budgetAnalysisModel[BUDGET_REMAIN]

    outputAnalysisReport(summaryModel)
        

def getBudgetList():
    return []

def getIncomeList():
    return []

def getTransactionDataFrame():
    mostRecentCsv = max(glob.iglob("*.csv"), key=os.path.getmtime)
    df = pd.read_csv(mostRecentCsv)
    df['date'] = pd.to_datetime(format="%d/%m/%Y",arg=df['date'])
    return df

def getRecentPayday(date=datetime.now(), payday=24):
    thisPayday = date - relativedelta(months=0, day=payday)
    lastPayday = date - relativedelta(months=1, day=payday)
    if (date - thisPayday).days >= 0:
        return thisPayday.replace(hour=0,minute=0,second=0,microsecond=0)
    return lastPayday.replace(hour=0,minute=0,second=0,microsecond=0)

def getNextPayday(date=datetime.now(), payday=24):
    thisPayday = date + relativedelta(months=0, day=payday)
    nextPayday = date + relativedelta(months=1, day=payday)
    if (date - thisPayday).days >= 0:
        return nextPayday.replace(hour=0,minute=0,second=0,microsecond=0)
    return thisPayday.replace(hour=0,minute=0,second=0,microsecond=0)

def getIncome(incomeList, df):
    incomes = df[df['category'].isin(incomeList)]
    return incomes['amount'].sum()

def getExpectedExpenseToDate(allocationAmount, recentPayday, nextPayday):
    budgetPerDay = allocationAmount/(nextPayday - recentPayday).days
    return budgetPerDay * (datetime.now() - recentPayday).days

def getActualExpense(categoryList, df):
    expenses = df[df['category'].isin(categoryList)]
    return expenses['amount'].sum()

def outputAnalysisReport(summaryModel):
    with open('AnalysisReport.txt', 'w') as f:
        print(BUDGET_LIST, file=f)
        for budgetAnalysisModel in summaryModel[BUDGET_LIST]:
            for k, v in budgetAnalysisModel.iterItems():
                print(k + ' : ' + v,file=f)
        print(OVERALL_NET + ' : ' + summaryModel[OVERALL_NET], file=f)
        print(OVERALL_REMAIN + ' : ' + summaryModel[OVERALL_REMAIN], file=f)