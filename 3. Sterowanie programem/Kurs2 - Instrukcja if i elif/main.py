#1
lajki=130
shares=500
MIN_LIKES=500
MIN_SHARES=100
if lajki>=500 and shares>=100:
    print('CENA OBNIZONA')
elif lajki<500 and shares<100:
    print('BRAK LAJKOW I SHAROW')
elif lajki<500:
    print('BRAK LAJKOW')
else:
    print('BRAK SHAROW')
#2
isburger=True
isbigsoda=True
isweekend=False
if isbigsoda and isburger and not isweekend:
    print('KUPON NA BURGERA!!!')
elif not isbigsoda and not isburger and isweekend:
    print('NI MA KUPONU. NIE MA BURGERA, NIE MA BIG SODA I JEST WEEKEND.')
elif not isbigsoda and not isburger:
    print('NI MA KUPONU. NIE MA BURGERA I NIE MA BIG SODA.')
elif not isbigsoda and isweekend:
    print('NI MA KUPONU. NIE MA BIG SODA I JEST WEEKEND.')
elif not isburger and isweekend:
    print('NI MA KUPONU. NIE MA BURGERA I JEST WEEKEND.')
elif not isbigsoda:
    print('NI MA KUPONU. NIE MA BIG SODA.')
elif not isburger:
    print('NI MA KUPONU. NIE MA BURGERA.')
else:
    print('NI MA KUPONU. JEST WEEKEND')