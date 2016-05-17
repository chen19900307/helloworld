def printdebug(func):
	def __decorator(user):
		print('Enter the login')
		result = func(user)
		print('
