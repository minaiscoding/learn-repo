import sys
from ruamel import yaml 
# Author : Hinami.

# examine challenge.yaml
with open(f"{sys.argv[1]}/{sys.argv[2]}/challenge.yml", "r") as stream:
    try:
        challenge=yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
        sys.exit(1)

# open the counter file and create if it doesn't exist
try:
    file = open(f'{sys.argv[1]}/counter.yaml','r')
except FileNotFoundError:
    file = open(f'{sys.argv[1]}/counter.yaml','w')
    file.writelines(['Challenges : 0\n','Per category:\n','Per difficulty:\n'])
    file.close()
    file = open(f'{sys.argv[1]}/counter.yaml','r')
data = yaml.round_trip_load(file)
data['Challenges'] = data['Challenges']+1 

######################################################

# update categories
category = challenge['category']
pos = list(data.keys()).index('Per category') +1
if category not in data.keys():
    data.insert(pos, category, 1,comment='New category added')
else:
    data[category] = data[category] + 1


# update difficulty
difficulty = challenge['difficulty']
pos = list(data.keys()).index('Per difficulty') +1
if difficulty not in data.keys():
    data.insert(pos, difficulty, 1)
else:
    data[difficulty] = data[difficulty] + 1
    

file.close()

# updating the file

with open(f'{sys.argv[1]}/counter.yaml','w') as file:
    data.fa.set_block_style() 
    documents = yaml.round_trip_dump(data, file)




