def printdebug(func):
    def __decorator():
        print('enter the login')
        func()
        print('exit the login')
    return __decorator 
 
@printdebug  #combine the printdebug and login
def login():
    print('in login')
 
login()  #make the calling point more intuitive
