# Manually backup GitHub repos

1. [install GitHub CLI](https://docs.github.com/en/rest/quickstart#getting-started-using-github-cli)
   - `brew install gh`
2. login
   - `gh auth login`
3. [GitHub API | List repositories for a user](https://docs.github.com/en/rest/repos/repos#list-repositories-for-a-user)
   - `gh api users/Yang-Xijie/repos > output/repos.json`
4. run python script
   - `python3 main.py`
