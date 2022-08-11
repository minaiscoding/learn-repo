

import sys
cat = 'reverse'
dif = 'hard'
data = ['Challenges : 0\n', 'Reverse : 0\n', 'Crypto : 0\n', 'per dif:\n', 'Easy : 0\n', 'Hard : 0\n']

with open(sys.argv[1],'r') as file:
    data = file.readlines()
    num = str(int(data[0][-2])+1) 
    data[0] = f'Challenges : {num}\n'
    print(data)
    match cat.upper():
        case 'CRYPTO':
            num = str(int(data[2][-2])+1) 
            data[2] = f'Crypto : {num}\n' 
# string doesn't support item assignment that's why i'm rewriting the whole line
        case 'REVERSE':
            num = str(int(data[1][-2])+1) 
            data[1] = f'Reverse : {num}\n'
    match dif.upper():
        case 'EASY':
            num = str(int(data[4][-2])+1) 
            data[4] = f'Easy : {num}\n'
        case 'HARD':
            num = str(int(data[5][-2])+1) 
            data[5] = f'Hard : {num}\n'
with open('./save.txt','w') as file:
    for line in data:
        file.write(line)


