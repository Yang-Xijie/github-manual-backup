# Manually backup GitHub repos

1. [install GitHub CLI](https://github.com/cli/cli#installation)
   - `brew install gh`
2. login
   - `gh auth login`
3. [list repositories for the authenticated user](https://docs.github.com/en/rest/repos/repos#list-repositories-for-the-authenticated-user)
   - `gh api "user/repos?type=all&sort=created&per_page=100&page=1" > output/repos.json`
4. run python script
   - `python3 main.py`
