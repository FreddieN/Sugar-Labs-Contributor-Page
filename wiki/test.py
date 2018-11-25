import json

contributors = []

with open("out.json", "r") as file:
    wikijson = (json.loads(file.read()))
    contributors = wikijson

print(contributors[1])

with open("members.csv", "w") as file:
    for x in contributors:
        file.write(x["userid"]+","+x["name"]+","+str(x["editcount"])+"\n")