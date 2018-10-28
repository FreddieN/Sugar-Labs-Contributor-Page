final = {} # move current data to dictionary format for JSON
final['opensource'] = {}
final['members'] = {}
contributors = {}
contributors['opensource'] = {}
contributors['members'] = {}

print("Importing members.csv") # import members.csv (manual entry)
with open('members.csv', 'r') as file:
    for x in file:
        x = x.strip()
        row = x.split(",")
        (contributors['members'])[row[0]] = {}
        ((contributors['members'])[row[0]])["desc"] = row[1]
