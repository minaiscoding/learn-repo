import sys
from ruamel import yaml 
# Author : Hinami.
# Functions needed
DIFFICULTIES = ['Easy','Ezmid','Midium','Medhard','Hard','Extreme']

def init_category(cat:str,data):
    try:
        if category not in data.keys():
           data.insert(1, cat, [{'Easy': 0},{'Ezmid':0},{'Medium': 0},{'Medhard':0},{'Hard': 0},{'Extreme': 0}], comment='This is the phone number')
    except AttributeError: # AKA the file was empty
        data = yaml.round_trip_load(
f'''{category} :
- Easy: 0
- Ezmid: 0
- Medium: 0
- Medhard: 0
- Hard: 0
- Extreme: 0
'''
    )
    return data

def num_dif(dif:str):
    return DIFFICULTIES.index(dif)
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

# initialise the file with one category so that  'data' won't be a nonetype (avoiding attributes errors )

    file = open(f'{sys.argv[1]}/counter.yaml','x')
    file.close()
    file = open(f'{sys.argv[1]}/counter.yaml','r')
data = yaml.round_trip_load(file)



######################################################

# update categories
category = challenge['category'].capitalize()
data = init_category(category,data)

# update difficulty

difficulty = challenge['difficulty'].capitalize()
try:
    data[category][num_dif(difficulty)][difficulty] +=  1
except KeyError:
    print("The difficulty is written wrong or doesn't exist")
    sys.exit(1)

file.close()

# updating the file

with open(f'{sys.argv[1]}/counter.yaml','w') as file:
    data.fa.set_block_style() 
    documents = yaml.round_trip_dump(data, file)




