import github3

gh = github3.GitHub()
org = gh.organization('conda-forge')
with open('cf-graph/names.txt', 'w') as f:
    for repo in org.iter_repos():
        f.write(repo.full_name)

