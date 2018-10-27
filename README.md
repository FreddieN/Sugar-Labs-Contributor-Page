# Sugar-Labs-Contributor-Page

## To set the page up on a web server:
1. Upload all files to the web dir.
1. Check the page is loading properly at the directory you have put the file in.
1. Follow instructions below to get automated contributor updates.

## Automated updates
1. You will need to either have python on the web server or upload the folder to another server and install python there.
    1. **NOTE** You will need to make sure that a Access-Control-Allow-Origin violation does not occur if using the .json on a remote endpoint.
1. You will then need to update the gitoauth.json file with a github oauth client id and secret to allow the script to make enough requests.
    1. If you do not do this, the script will most likely fail as a lot of data is requested from the GitHub API.
1. Make sure members.csv is up to date with any relevant changes. This is a manual entry method for contributors not on GitHub.
1. Run generateJSON.py - it will take a few minutes to generate the file.
    1. You can add this file to crontab on linux to automatically run the script. I would set this to once every week.
1. The script will generate a clists.json which you can point scripts/opensource.js to. Remember if remote that a Access-Control-Allow-Origin violation will occur if not setup properly

## Adding members to the member list
1. Add a name onto a new line of members.csv
    1. This could be setup so members could make pull requests to add their name, just make sure formatting is intact.