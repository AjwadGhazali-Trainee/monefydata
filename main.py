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

def main():
    budgetList = getBudgetList()
    tranDf = getTransactionDataFrame()
    daysSinceLastPayday = getDaysSinceLastPayday()
    summaryModel = {}
    summaryModel[BUDGET_LIST] = []
    summaryModel[OVERALL_NET] = 0
    summaryModel[OVERALL_REMAIN] = 0
    summaryModel[SUGGESTED_PERDAY] = 0

    for budget in budgetList:
        budgetAnalysisModel = {}
        budgetAnalysisModel[BUDGET_NAME] = ''
        budgetAnalysisModel[BUDGET_ALLOCATION] = 0
        budgetAnalysisModel[BUDGET_EXPECTED_EXPENSE] = 0
        budgetAnalysisModel[BUDGET_ACTUAL_EXPENSE] = 0
        budgetAnalysisModel[BUDGET_NET] = 0
        budgetAnalysisModel[BUDGET_REMAIN] = 0

        allocatedBudget = getAllocatedBudget(budget.allocation, tranDf)
        expectedExpense = getExpectedExpenseToDate(allocatedBudget, daysSinceLastPayday)
        actualExpense = getActualExpense(budget.categoryList, tranDf)
        net = expectedExpense - actualExpense
        remainingBalance = allocatedBudget - actualExpense

        budgetAnalysisModel[BUDGET_NAME] = budget.name
        budgetAnalysisModel[BUDGET_ALLOCATION] = allocatedBudget
        budgetAnalysisModel[BUDGET_EXPECTED_EXPENSE] = expectedExpense
        budgetAnalysisModel[BUDGET_ACTUAL_EXPENSE] = actualExpense
        budgetAnalysisModel[BUDGET_NET] = net
        budgetAnalysisModel[BUDGET_REMAIN] = remainingBalance

        summaryModel[BUDGET_LIST].append(budgetAnalysisModel)
        summaryModel[OVERALL_NET] += budgetAnalysisModel[BUDGET_NET]
        

def getBudgetList():
    return []

def getAllocatedBudget(allocationPercentage, dataFrame):
    return 1

def getTransactionDataFrame():
    return True

def getDaysSinceLastPayday():
    return 1

def getExpectedExpenseToDate(allocationAmount, daysSinceLastPayday):
    return 1

def getActualExpense(categoryList, dataFrame):
    return 1