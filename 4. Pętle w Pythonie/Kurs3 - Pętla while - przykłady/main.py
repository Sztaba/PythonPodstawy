#1
number=0
while number<50:
    print(number*2+1)
    number+=1
#2 i #3
import random
my_number = random.randint(0,20)
guess=-1
trials=0
print('Guess my number!')
while guess!=my_number:
    guess=int(input())
    trials+=1
    if guess==my_number:
        print('GRATULACJE - ZGADLES ZA',trials,'RAZEM')
    elif guess>my_number:
        print('SORRY - MOJA LICZBA JEST MNIEJSZA NIŻ TWÓJ STRZAL')
    else:
        print('SORRY - MOJA LICZBA JEST WIĘKSZA NIZ TWÓJ STRZAL')