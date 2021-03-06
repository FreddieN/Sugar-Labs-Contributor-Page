import json
import gitapi
import datetime
import csv

optout = []
with open('optout', 'r') as file:
    for line in file:
        optout.append(line)

repos = gitapi.getSugarRepos() # gather all repos made by sugarlabs org
contributors1 = [] 
count = 0

for repo in repos: # gather contributors for each repo - this takes a while make sure to have api key
    count = count+1
    print(str(count)+"/"+str(len(repos))+" Fetching data from "+repo)
    repoowner = (repos[repo])['owner']
    repocontributors = gitapi.getRepoContributors(repo, repoowner)
    for contributor in repocontributors:
        if not(contributor in optout):
            contributors1.append(contributor)

final = {} # move current data to dictionary format for JSON
final['opensource'] = {}
final['members'] = {}
contributors = {}
contributors['opensource'] = {}
contributors['members'] = {}
contributors["membersnodesc"] = {}
contributors['memberswithdesc'] = {}

for x in contributors1:
    (contributors['opensource'])[x.strip()] = {"github": x.strip()}
print("Importing members.csv") # import members.csv (manual entry)
with open('members.csv', 'r') as file:
    cread = csv.reader(file)
    for row in cread:
        (contributors['opensource'])[row[0]] = {}
        ((contributors['opensource'])[row[0]])["desc"] = row[1]
print("Sorting lists...") # sort all lists by alphabetical order
for key in sorted(contributors['opensource'].keys(), key=lambda s: s.casefold()):
    (final['opensource'])[key] = contributors['opensource'][key]
    
print("Generating Timestamp...")
final['dategen'] = datetime.datetime.today().strftime('%Y-%m-%d') # attach timestamp to display at bottom of page
conjson = json.dumps(final)

with open('clists.json', 'w') as file: # save file
    file.write(str(conjson))
print("clists.json was generated")
