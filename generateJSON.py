import json
import gitapi
import datetime

repos = gitapi.getSugarRepos() # gather all repos made by sugarlabs org
contributors1 = [] 
count = 0

for repo in repos: # gather contributors for each repo - this takes a while make sure to have api key
    count = count+1
    print(str(count)+"/"+str(len(repos))+" Fetching data from "+repo)
    repoowner = (repos[repo])['owner']
    repocontributors = gitapi.getRepoContributors(repo, repoowner)
    for contributor in repocontributors:
        contributors1.append(contributor)

final = {} # move current data to dictionary format for JSON
final['opensource'] = {}
final['members'] = {}
contributors = {}
contributors['opensource'] = {}
contributors['members'] = {}

for x in contributors1:
    (contributors['opensource'])[x.strip()] = {}
print("Importing members.csv") # import members.csv (manual entry)
with open('members.csv', 'r') as file:
    for x in file:
        x = x.strip()
        row = x.split(",")
        (contributors['members'])[row[0]] = {}
        ((contributors['members'])[row[0]])["desc"] = row[1]
print("Sorting lists...") # sort all lists by alphabetical order
for key in sorted(contributors['opensource'].keys()):
    (final['opensource'])[key] = {}
for key in sorted(contributors['members'].keys()):
    (final['members'])[key] = (contributors['members'])[key]
    
print("Generating Timestamp...")
final['dategen'] = datetime.datetime.today().strftime('%Y-%m-%d') # attach timestamp to display at bottom of page
conjson = json.dumps(final)

with open('clists.json', 'w') as file: # save file
    file.write(str(conjson))
print("clists.json was generated")
