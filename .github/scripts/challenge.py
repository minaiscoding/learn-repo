import sys
import yaml


CATEGORIES=['web','reverse','pwn','linux','misc','osint','programming','crypto','forensics']
DIFFICULTY=['easy','ezmed','medium','medhard','hard','extreme']


with open(f"{sys.argv[1]}/{sys.argv[2]}/challenge.yml", "r") as stream:
    try:
    	challenge=yaml.safe_load(stream)
    except yaml.YAMLError as exc:
    	print(exc)
    	sys.exit(1)


# Author validation
if "author" not in challenge.keys():
    print("The author of the challenge is missing.")
    sys.exit(1)

if len(challenge["author"])==0:
    print("The author field can't be empty.")
    sys.exit(1)

# Category validation
if "category" not in challenge.keys():
    print("The category of the challenge is missing.")
    sys.exit(1)

if challenge['category'] not in CATEGORIES:
    print("The category of the challenge is unkown.")
    sys.exit(1)

# Difficulty validation
if "difficulty" not in challenge.keys():
    print("The difficulty of the challenge is missing.")
    sys.exit(1)

if challenge['difficulty'] not in DIFFICULTY:
    print("The difficulty of the challenge is unkown.")
    sys.exit(1)

# Flag validation
if "flags" not in challenge.keys():
    print("The flag of the challenge is missing.")
    sys.exit(1)

if len(challenge["flags"][0])==0:
    print("The author field can't be empty.")
    sys.exit(1)