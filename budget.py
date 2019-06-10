from config import MONTHLY, DAILY

payday = 24

budgetList =  [
			{
				'name': 'Savings',
				'percentage': 0.12,
				'frequency': MONTHLY,
				'prededuct': 0,
				'categoryList': [
				
				]
			},
			{
				'name': 'Emergency',
				'percentage': 0.15,
				'frequency': MONTHLY,
				'prededuct': 0,				
				'categoryList': [
				
				]
			},
			{
				'name': 'Wants',
				'percentage': 0.23,
				'frequency': MONTHLY,
				'prededuct': 0,
				'categoryList': [
					'Gift',
					'Gifts',
					'Entertainment',
					'Clothes',
					'Sports',
					'Haircut',
					'Book',
					'Pets'
				]
			},
			{
				'name': 'Daily',
				'percentage': 0.5,
				'frequency': DAILY,
				'prededuct': 3500+269,
				'categoryList': [
					'Food',
					'Transport',
					'Eating out',
					'Communications',
					'Health'
				]
			}
		]