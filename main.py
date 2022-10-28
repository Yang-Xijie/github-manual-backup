import json
import subprocess


with open("./output/repos.json") as f:
    repos = json.loads(f.read())
print(len(repos))
for repo in repos:
    print(repo["ssh_url"])
