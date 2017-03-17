#Список словарей "класс с оценками"
school_list = [ {'school_class':'4a','scores':[3,4,5,5,3]},
				{'school_class':'4б','scores':[4,4,5,5,5]},
				{'school_class':'4в','scores':[3,3,4,3,5]},
				{'school_class':'5a','scores':[4,4,5,4,4]},
				{'school_class':'5б','scores':[5,5,5,5,4]},
				{'school_class':'5в','scores':[4,4,5,5,4]},
				{'school_class':'6a','scores':[5,4,4,5,3]},
				{'school_class':'6б','scores':[3,2,5,3,4]}]
#Создаём переменные средняя оценка класса и средняя оценка школы
#average_scores_class  = 0
average_scores_school = 0
#Считаем среднии оценки
#for i in range(len(school_list)):
for klass in school_list:
	average_scores_class  = 0
	#for j in range(len(school_list[i].get('scores'))):
	for j in range(len(klass.get('scores'))):
		#Складываем все оценки в классе
		#average_scores_class += school_list[i].get('scores')[j]
		average_scores_class += klass.get('scores')[j]
	#Считаем среднюю оценку класса
	#average_scores_class = average_scores_class / len(school_list[i].get('scores')) 	
	average_scores_class = average_scores_class / len(klass.get('scores')) 	
	#Складываем все среднии оценки классов
	average_scores_school += average_scores_class
	#Печатаем среднюю оценку класса
	print('Средняя оценка класса ' + klass.get('school_class').upper() + ': ' + str(average_scores_class))  
	#Обнуляем среднюю оценку класса для нового цикла
	#average_scores_class = 0
#Считаем среднюю оценку по школе
average_scores_school = average_scores_school / len(school_list)
#Печатаем среднюю оценку школы
print('..........ИТОГО...........')
print('Средняя оценка школы ' + str(average_scores_school))  