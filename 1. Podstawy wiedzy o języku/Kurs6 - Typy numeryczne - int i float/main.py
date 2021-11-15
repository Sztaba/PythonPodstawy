# 1
name = 'Hubert'
# 2
age = 19
# 3
daysInYear = 365
# 4
message = '%s is %d years old, so is about %d days old'
# 5
print(message%(name, age, daysInYear * age))
# 6
name='Mikołaj'
age=21
print(message%(name, age, daysInYear * age))
# 7
message = '{0:s} is {1:d} years old, so is about {2:d} days old'
# 8
print(message.format(name, age, daysInYear * age))
#9
m='%d divided by %d is %d and the rest is %d'
x=1234567890
y=12345
print(m%(x,y,x//y,x%y))