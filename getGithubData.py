import json
import gitapi

repos = gitapi.getSugarRepos()
contributors = []
print(repos)

for repo in repos:
    repoowner = (repos[repo])['owner']
    repocontributors = gitapi.getRepoContributors(repo, repoowner)
    for contributor in repocontributors:
        contributors.append(contributor)

with open('output.csv', 'w') as file:
    for x in contributors:
        file.write(x+"\n")
