#1
musclePain=False
fever=True
weakness=True
#2
if musclePain and fever and weakness:
    print('suspicion of influenza')
else:
    print('The flu is unlikely')
#3
if musclePain and fever and weakness:
    print('suspicion of influenza')
elif weakness and (not fever or not musclePain):
    print('Just take a rest!')
else:
    print('You may be cold')
#4
isMan=True
#5
if weakness and fever and musclePain or isMan and (weakness or musclePain or fever):
    print('suspicion of influenza')
elif weakness and (not fever or not musclePain):
    print('Just take a rest!')
else:
    print('You may be cold')
#6
isCheckCompleted=True
print('CHECK IS COMPLETED' if isCheckCompleted else 'CHECK NOT DONE YET')
isCheckCompleted=False
print('CHECK IS COMPLETED' if isCheckCompleted else 'CHECK NOT DONE YET')