#1
lajki=1300
shares=505
MIN_LIKES=500
MIN_SHARES=100
cena=1000
if lajki>=MIN_LIKES and shares>=MIN_SHARES:
    print("CENA OBNIZONA")
else:
    print("NADAL DROGO :) BO NI MA LAJKOW LUB SHAROW")
#2
isPizzaOrdered=True
isBigDrinkOrdered=True
isWeekend=True
if isPizzaOrdered == True and isBigDrinkOrdered == True and isWeekend == True:
    print('WYGRALES KUPON NA BURGERA')
else:
    print('DZIEKUJEMY I ZAPRASZAMY PONOWNIE')
#3
diskSize=140
diskSizeUsed=123
fileSize=10
if fileSize+diskSizeUsed<=diskSize:
    print('File can be downloaded')
else:
    print('Not enough space on disk')