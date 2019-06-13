# CLASS:
#   SummaryModel - model for summary data
# FIELDS:
#   budget_analysis_list - list of BudgetAnalysisModels
#   overall_net - overall net gain/loss
#   overall_remain - overall remaining balance for income

class SummaryModel:
    def __init__(self,
                budget_analysis_list=[],
                overall_net = 0,
                overall_remain = 0):
                self.budget_analysis_list = budget_analysis_list
                self.overall_net = overall_net
                self.overall_remain = overall_remain