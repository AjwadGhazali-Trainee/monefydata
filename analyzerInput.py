from config import MONTHLY, DAILY
from budget import Budget

payday = 24

budgetList =  [
            Budget(
                name = 'Savings',
                percentage = 0.24,
                frequency = MONTHLY,
                carryOver = 8109.13,
                categoryList = [
                	'Premium (PruLife)',
                ]
            ),
			Budget(
                name = 'Emergency',
                percentage = 0.15,
                frequency = MONTHLY,
                carryOver = 8986.20,
                categoryList = [
                    'Gifts'
                ]
            ),
            Budget(
                name = 'Wants',
                percentage = 0.23,
                frequency = MONTHLY,
                carryOver = -694.18,
                categoryList = [
					'Gift',
					#'Gifts',
					'Entertainment',
					'Clothes',
					'Sports',
					#'Haircut',
					'Book',
					'Pets',
                    'PC'
				]
            ),
            Budget(
                name = 'Daily',
                percentage = 0.38,
                fixedExpense = 3500+269,
                carryOver = 743.81,
                categoryList = [
					'Food',
					'Transport',
					'Eating out',
					'Communications',
					'Health',
					'Haircut'
				]
            ),
		]

exclude = [

]

incomeList = [
	'Deposits',
    'Interest',
    'Return',
    'Salary',
    'Savings',
]