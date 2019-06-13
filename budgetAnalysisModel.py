from config import DAILY

# CLASS:
#   BudgetAnalysisModel - model for budget analysis data
# FIELDS:
#   name - name for the budget
#   allocation - allocated budget based on perecentage allocation and income
#   expected_expense - expected expense to date
#   actual_expense - actual expense based on transaction data
#   net - net gain/loss
#   remain - remaining balance for the budget
#   frequency - frequency of budget (DAILY, WEEKLY, MONTHLY)
#   suggestion - suggested budget for remaining days before next payday

class BudgetAnalysisModel:
    def __init__(self, name='',
                allocation=0,
                expected_expense=0,
                actual_expense=0,
                net=0,
                remain=0,
                frequency = DAILY,
                suggestion = 0):
                self.name = name
                self.allocation = allocation
                self.expected_expense = expected_expense
                self.actual_expense = actual_expense
                self.net = net
                self.remain = remain
                self.frequency = frequency
                self.suggestion = suggestion