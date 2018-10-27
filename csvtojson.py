import json
import datetime

final = {}
final['opensource'] = {}
final['members'] = {}
contributors = {}
contributors['opensource'] = {}
contributors['members'] = {}

with open('output.csv', 'r') as file:
    for x in file:
        (contributors['opensource'])[x.strip()] = {}
with open('members.csv', 'r') as file:
    for x in file:
        (contributors['members'])[x.strip()] = {}

for key in sorted(contributors['opensource'].keys()):
    (final['opensource'])[key] = {}
for key in sorted(contributors['members'].keys()):
    (final['members'])[key] = {}

final['dategen'] = datetime.datetime.today().strftime('%Y-%m-%d')
conjson = json.dumps(final)

with open('output.json', 'w') as file:
    file.write(str(conjson))
