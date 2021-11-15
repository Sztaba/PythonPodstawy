atext='This is a text.'
print(atext.endswith('ext')) #False
print(atext.endswith('ext.')) #True
print(atext.islower()) #False
print(atext.upper()) #THIS IS A TEXT.
print(atext.upper().isupper()) #True
print(atext.find('is')) #2 - pierwsze znalezienie
print(atext.find('is',3)) #5 - drugi argument mówi od którego znaku zacząć szukać
print(atext.replace('a','4')) #This is 4 text.
print(atext.replace('a','4').replace('i','1').replace('e','3')) #Th1s 1s 4 t3xt.
print(atext.split(' ')) #['This','is','a','text.'] - dzieli tekst ze względu na pewnien podnapis
somethingLikeNumber='1000'
print(somethingLikeNumber.isdigit()) #True - czy liczba całkowita
print(somethingLikeNumber.isdecimal()) #True - czy liczba całkowita lub z przecinkiem
print(somethingLikeNumber.isalpha()) #False - czy składa się z samych liter
print(somethingLikeNumber.isalnum()) #True - czy składa się z liter lub cyfr
print()

#ZADANIA
print('ZADANIA')
#1
quote='A good programmer is someone who always looks both ways before crossing a one-way street'
#2
print(quote.upper())
#3
print(quote.lower())
#4
print(quote.endswith('street'))
#5
print(quote.isupper())
#6
print(quote.upper().isupper())
#7
print(quote.find('one'))
#8
print(quote.replace('one','1'))
#9
print(quote.replace('one','1').replace('both','2'))
#10
print(quote.split(' '))
#11
print(quote.isdigit())
print(quote.isdecimal())
print(quote.isalpha())
print(quote.isalnum())
