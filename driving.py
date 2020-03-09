country = input('Please input your country: ')
age = input('Please input your age: ')
age = int(age)
if country == 'Taiwan' or 'TW':
	if age >= 18:
		print('You can own a driving license')
	else:
		print('You cannot own a driving license')
elif country == 'Indonesia' or 'IDN':
	if age >= 20:
		print('You can own a driving license')
	else:
		print('You cannot own a driving license')
elif country == 'USA' or 'US' or 'the US':
	if age >= 16:
		print('You can own a driving license')
	else:
		print('You cannot own a driving license')