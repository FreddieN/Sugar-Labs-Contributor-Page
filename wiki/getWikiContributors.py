import urllib

import json

url = "https://wiki.sugarlabs.org/api.php" #uses wikimedia api to retrieve data
req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"}) #user agent required to pass basic site checks
con = urllib.request.urlopen( req )
html = con.read().decode("utf-8")
rjson = ""

with open("output.txt", "w") as file:
    lastuser = {}
    count = 1
    req = urllib.request.Request(
        url+"?action=query&list=allusers&format=json&aulimit=500&auprop=editcount", 
        data=None, 
        headers={
            'User-Agent': 'Magic Browser'
        }
    )
    with urllib.request.urlopen(req) as response:
        r = response.read().decode('utf-8')
        rjson = json.loads(r)['query']['allusers']
        lastuser = str(rjson[-1]['name'].encode("raw_unicode_escape").decode("ascii")) #last user required to enumerate to the next page
        oldlastuser = ""
        while (lastuser not in oldlastuser): #check to see if all users have been retrieved
            oldlastuser = lastuser
            req = urllib.request.Request(
            url+("?action=query&list=allusers&format=json&aulimit=500&auprop=editcount|blockinfo&aufrom="+lastuser), 
            data=None, 
            headers={
                'User-Agent': 'Magic Browser'
            })
            print(url+("?action=query&list=allusers&format=json&aulimit=500&auprop=editcount|blockinfo&aufrom="+lastuser))
            with urllib.request.urlopen(req) as response:
                r = response.read().decode('utf-8')
                rjson = rjson + json.loads(r)['query']['allusers']
                count = len(rjson)
                lastuser = str(rjson[-1]['name'].encode("raw_unicode_escape").decode("ascii"))

contributors = []

for x in rjson:
    if(int(x['editcount']) > 10 and x.get('blockid') is None): #checks to see if user has more than 10 edits and whether they are blocked (this removes most bots)
        contributors.append(x)

with open("out.json", "w") as file:
    file.write(json.dumps(contributors))