contry = input('請問您是哪國人: ')
age = input('請問您的年齡: ')
age = int(age)
if contry == '台灣':
	if age >= 18:
		print('可以考駕照')
	else:
		print('不可以考駕照')
elif contry == '美國':
	
	if age >= 16:
		print('可以考駕照')
	else:
		print('不可以考駕照')
else:
	print("你只能輸入台灣或美國")
	

