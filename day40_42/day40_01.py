import json
from pprint import pprint

with open('data/mount-data.json', 'r') as file:
    r = file.read()

r2 = r.replace("'",'"')
r2 = r2.replace("False", '"False"')
r2 = r2.replace("True", '"True"')

data = json.loads(r2)

print(data['mounts']['collected'])

boolean_properties=['isAquatic','isFlying','isGround','isJumping']

for item in data['mounts']['collected']:
    for prop in boolean_properties:
        if item[prop] == 'True':
            item[prop] = True
        else:
            item[prop] = False

print(data['mounts']['collected'])

pprint(data)

