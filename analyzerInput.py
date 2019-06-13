from config import MONTHLY, DAILY
from budget import Budget

payday = 24

budgetList =  [
            Budget(
                name = 'Wants',
                percentage = 0.23,
                frequency = MONTHLY,
                categoryList = [
					'Gift',
					'Gifts',
					'Entertainment',
					'Clothes',
					'Sports',
					'Haircut',
					'Book',
					'Pets',
                    'PC'
				]
            ),
            Budget(
                name = 'Daily',
                percentage = 0.5,
                fixedExpense = 3500+269,
                categoryList = [
					'Food',
					'Transport',
					'Eating out',
					'Communications',
					'Health'
				]
            ),
		]

exclude = [
            Budget(
                name = 'Savings',
                percentage = 0.12,
                frequency = MONTHLY
            ),
            Budget(
                name = 'Emergency',
                percentage = 0.15,
                frequency = MONTHLY
            ),
]

incomeList = [
	'Deposits',
    'Interest',
    'Return',
    'Salary',
    'Savings',
]