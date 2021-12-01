#1
data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']
for d in data:
    print(d.upper())

#2
for d in data:
    elements=d.split(':')
    print(elements[0].upper(),elements[1])

#3
for d in data:
    elements=d.split(':')
    if elements[0]=='Error':
        print(elements[1].upper())
    else:
        print(elements[1])
