from config import MONTHLY, DAILY
from budget import Budget

payday = 24

budgetList =  [
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
					'Pets'
				]
            ),
            Budget(
                name = 'Wants',
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

incomeList = [
	'Deposits',
    'Interest',
    'Return',
    'Salary',
    'Savings',
]