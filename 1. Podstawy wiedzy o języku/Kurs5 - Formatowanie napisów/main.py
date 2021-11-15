# 1
helloMessage = 'Hello %s!'
# 2
print(helloMessage % ('Kate'))
print(helloMessage % ('Chris'))
# 3
helloMessage = 'Hello {0:s}!'
# 4
print(helloMessage.format('Kate'))
print(helloMessage.format('Chris'))
# 5
helloMessage = '%s has %d %s'
# 6
print(helloMessage % ('Kate', 1, 'animal'))
print(helloMessage % ('Chris', 100000, '$'))
# 7
helloMessage = '{0:s} has {1:d} {2:s}'
# 8
print(helloMessage.format('Kate', 1, 'animal'))
print(helloMessage.format('Chris', 100000, '$'))
# 9
line = '%20s costs %6d €'
# 10
print(line % ('ICE CREAM', 3))
print(line % ('TRIP TO VENICE', 119))
print(line % ('PIZZA HAWAI', 6))
# do lewej strony
line = "{0:20s} costs {1:6d} €"
print(line.format('ICE CREAM', 3))
print(line.format('TRIP TO VENICE', 119))
print(line.format('PIZZA HAWAII', 6))
# 11
line = '%s %d'
print(line % ('ICE CREAM', 3))
print(line % ('TRIP TO VENICE', 119))
print(line % ('PIZZA HAWAI', 6))