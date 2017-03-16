str_one = input('Пожалуйста, введите первую строку: ')
str_two = input('Пожалуйста, введите вторую строку: ')

def compare_str(string_one,string_two):
	if string_one == string_two:
		return 1
	elif len(string_one) > len(string_two):
		return 2
	elif string_two == 'learn':
		return 3

print(compare_str(str_one, str_two))