#1
chanels={'Google':1480,'Email':300,'Natural Traffic':440,'TV Spot':700}
print(chanels)
#2
print(chanels['Email'])
#3
chanelsUpdate={'Natural Traffic':520,'News':600}
#4
chanels.update(chanelsUpdate)
print(chanels)
#5
print(chanels.keys())
#6
print(chanels.pop('Email'))
print(chanels)