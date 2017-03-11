def get_answer(question):
	answers = {'hello':'Hello bro!','how are you?':'i am good', 'goodbye':'I will see you'}
	return answers[question.lower()]
your_question = input('Enter your question: ')
print(get_answer(your_question))
