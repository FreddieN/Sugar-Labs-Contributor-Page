import urllib.request
import json

skip = ['lybniz-graph-plotter-activity'] #skip any activites - this one causes problem

with open('gitoauth.json', 'r') as file: #import githuboauth - see readme for details
    rjson = ""
    for line in file:
        rjson = rjson+line
    oauthdetsdict = json.loads(rjson)
    oauthdets = "client_id="+oauthdetsdict["githubclientid"]+"&client_secret="+oauthdetsdict["githubclientsecret"]

def getSugarRepos(): # gets all repos for sugar
    count = 1
    page = 1
    repos = {}
    while count != 0: # github api works in page system keeps going until no records left
        with urllib.request.urlopen('https://api.github.com/orgs/sugarlabs/repos?per_page=100&page='+str(page)+"&"+oauthdets) as response:
           r = response.read().decode('utf-8')
           rjson = json.loads(r)
           page += 1
           count = len(rjson)
           for repo in rjson:
               reponame = repo['name']
               repoowner = (repo['owner'])['login']
               if not(reponame in skip):
                   repos[reponame] = {}
                   (repos[reponame])['owner'] = repoowner
    print("Gathered "+str(len(repos))+" Repos")
    return repos

def getRepoContributors(reponame, repoowner): # returns the contributors for that repo
    print('https://api.github.com/repos/'+repoowner+'/'+reponame+'/stats/contributors'+oauthdets)
    with urllib.request.urlopen('https://api.github.com/repos/'+repoowner+'/'+reponame+'/stats/contributors'+"?"+oauthdets) as response:
        r = response.read().decode('utf-8')
        rjson = json.loads(r)
        contributors = {}
        for contributor in rjson:
            contributors[(contributor['author'])['login']] = contributor['total']
        return contributors

