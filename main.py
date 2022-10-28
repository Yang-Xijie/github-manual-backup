from datetime import datetime
import json
import os
import subprocess

with open("./output/repos.json") as f:
    repos = json.loads(f.read())
print(f"{len(repos)} repositories found")

backup_folder = f'backup-{datetime.now().strftime("%Y%m%d-%H%M%S")}'
for repo in repos:
    repo_ssh_url = repo["ssh_url"]
    repo_full_name = repo["full_name"]
    print(f"start with repository {repo_full_name}")

    repo_folder = f"./{backup_folder}/{repo_full_name}"
    os.makedirs(repo_folder)
    subprocess.run([f"""git clone {repo_ssh_url} {repo_folder}"""], shell=True)
