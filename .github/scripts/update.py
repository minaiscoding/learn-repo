import sys
import yaml


with open(f"{sys.argv[1]}/{sys.argv[2]}/challenge.yml", "r") as stream:
    try:
        challenge=yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
        sys.exit(1)


# update the counter
with open(f'{sys.argv[1]}/counter.yaml','r') as file:
    data = yaml.full_load(file)
    num = data['Challenges']+1 
    print(data)
    data['Challenges'] = num
    match challenge['category'].upper():
        case 'WEB':
            num =data['web']+1 
            data['web'] = num 
        case 'REVERSE':
            num = data['reverse']+1
            data['reverse'] = num
        case 'PWN':
            num = data['pwn']+1
            data['pwn'] = num
        case 'LINUX':
            num = data['linux']+1
            data['linux'] = num
        case 'MISC':
            num = data['misc']+1
            data['misc'] = num
        case 'OSINT':
            num = data['osint']+1
            data['osint'] = num
        case 'PROGRAMMING':
            num = data['programming']+1
            data['programming'] = num
        case 'CRYPTO':
            num = data['crypto']+1
            data['crypto'] = num
        case 'FORENSICS':
            num = data['forensics']+1
            data['forensics'] = num
    match challenge['difficulty'].upper():
        case 'EASY':
            num = data['easy']+1
            data['easy'] = num
        case 'EZMED':
            num = data['ezmed']+1
            data['ezmed'] = num
        case 'MEDIUM':
            num = data['medium']+1
            data['medium'] = num
        case 'MEDHARD':
            num = data['medhard']+1
            data['medhard'] = num
        case 'HARD':
            num = data['hard']+1
            data['hard'] = num
        case 'EXTREME':
            num = data['extreme']+1
            data['extreme'] = num
print(data)
with open(f'{sys.argv[1]}/counter.yaml','w') as file:
    documents = yaml.dump(data, file,sort_keys=False)