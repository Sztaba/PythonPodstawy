#1
numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]
i=0
while i<len(numbers)-1:
    print(numbers[i],numbers[i+1])
    if numbers[i]**2==numbers[i+1]:
        print('\tFOUND',numbers[i],numbers[i+1])
    i+=1
#2
i=0
while i<len(numbers)-2:
    print(numbers[i],numbers[i+1],numbers[i+2])
    if numbers[i]**2==numbers[i+1] and numbers[i+1]**2==numbers[i+2]:
        print('\tFOUND',numbers[i],numbers[i+1],numbers[i+2])
    i+=1
#3
texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
i=0
while i<len(texts)-1:
    print(texts[i],texts[i+1])
    if len(texts[i])==len(texts[i+1]):
        print('\tFOUND',texts[i],texts[i+1])
    i+=1