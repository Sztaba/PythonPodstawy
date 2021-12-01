#1
i=10
silnia=1
for n in range(1,i+1):
    silnia*=n
print(silnia)

silnia=1
#2
for n in range(1,i+1):
    silnia*=n
    print(n,silnia)

#3
list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']
for i in list_noun:
    for j in list_adj:
        print(j,i)