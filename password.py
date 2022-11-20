time = 0
time = int(time)
while time < 3:
	password = input('請輸入密碼: ')
	time = time + 1
	if password == 'a123456': # quit
		break
	else:
		print('密碼錯誤_請再輸入一次')