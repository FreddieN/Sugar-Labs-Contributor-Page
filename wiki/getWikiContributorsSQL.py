import mysql.connector
import json

# Database setup place mediawiki database details here
mwdb = mysql.connector.connect(
  host="192.168.56.101",
  user="mediawiki",
  passwd="testpass",
  database="my_wiki"
)

contributors = {}

c = mwdb.cursor()
c.execute("SELECT * FROM user") # Get all users
result = c.fetchall()

for x in result:
    c = mwdb.cursor()
    c.execute("SELECT * FROM ipblocks WHERE ipb_user = "+str(x[0]))
    result = c.fetchall()
    if(not(len(result) > 0) and x[13] > 10): # Checks to see if user is blocked and has more than 10 edits
        contributors[x[0]] = {  # Compiles dictionary object for each user
            "username": x[1].decode("utf-8"),
            "realname": x[2].decode("utf-8"),
            "email": x[6].decode("utf-8"),
            "editcount": x[13]
        }

with open("outSQL.json", "w") as file:
    file.write(json.dumps(contributors)) # Outputs contributors to JSON