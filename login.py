def printdebug(func):
	def __decorator(user):
		print('enter the login')
		func(user)
		print('exit the login')
	return __decorator

@printdebug
def login(user):
	print 'in login:'+user

login('jatsz')
