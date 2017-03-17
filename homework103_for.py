#создаём новый список из 10 элементов
#new_list = [i for i in range(10)]
#new_list = list(range(10))
new_list = [3, 54, 5, 21, 7, 8, 3, 1, 5, 1]
#выводим элементы списка, увеличенные на 1
#for i in range(len(new_list)):
#В python в большинстве случаев итерация по индексам вообще не нужна, лучше итерировать сразу по значениям
for i in new_list:
	#print(new_list[i]+1)
	print(i+1)