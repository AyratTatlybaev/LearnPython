age = int(input('Пожалуйста, введите Ваш возраст: '))
if 0 < age < 3:
	print('Малыш')
elif 3 <= age < 6:
	print('Пора в детский садик')
elif 6 <= age < 18:
	print('Пора в школу')
elif 18 <= age < 22:
	print('Грызём гранит науки в универе')
elif 22 <= age < 65:
	print('Работаем товарищи')
else:
	print('Пенсия!!') 