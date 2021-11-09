drive='c:\\' #c:\
folder='scripts\\python\\'
file='myscript.py'
path=drive+folder+file
print(path) #c:\scripts\python\myscript.py
justText="text with\nnewline"
print(justText) #text with(nowa linia)newline
justText=r"text with\nnewline" #r jak raw(surowy)
print(justText) #text with\nnewline
justText="Mc Donald's"
print(justText) #Mc Donald's
#justText='Mc Donald's' - błąd
line='He said "I like Python!"'
print(line,'\n') #He said "I like Python!"

#ZADANIA
print('ZADANIA')
#1
print('\nZadanie 1')
firstName='Kasia'
famillyName='Sowa'
lastName='Mrugała'
newName=firstName+' '+famillyName+' '+lastName
print(newName)
#2
print('\nZadanie 2')
music='"Universal Fanfare" Jerry Goldsmith "Happy Together" Garry Bonner "I\'m a Man" Steve Winwood'
print(music)
#3
print('\nZadanie 3')
music='"Universal Fanfare" Jerry Goldsmith\n"Happy Together" Garry Bonner\n"I\'m a Man" Steve Winwood'
print(music)
#4
print('\nZadanie 4')
print('(\\(\\')
print('( -,-)')
print('O_(")(")')