string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'
for n in range(10):
    print(string_A)

print()

for n in range(1,10):
    if n % 2 == 0:
        print(string_B)
    else:
        print(string_A)

for n in range(1,10):
    print('x'*n)

for n in range(1,10):
    if n % 2 == 0:
        print('x'*n)
    else:
        print('o'*n)