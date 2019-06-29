from config import MONTHLY, DAILY
from budget import Budget

payday = 24

budgetList =  [
            Budget(
                name = 'Savings',
                percentage = 0.12,
                frequency = MONTHLY,
                carryOver = 0,
                categoryList = [
                	'Premium (PruLife)',
                ]
            ),
			Budget(
                name = 'Emergency',
                percentage = 0.15,
                frequency = MONTHLY,
                carryOver = 0
            ),
            Budget(
                name = 'Wants',
                percentage = 0.23,
                frequency = MONTHLY,
                carryOver = 0,
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
                carryOver = 0,
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

]

incomeList = [
	'Deposits',
    'Interest',
    'Return',
    'Salary',
    'Savings',
]