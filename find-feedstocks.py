import github3

gh = github3.GitHub()
org = gh.organization('conda-forge')
with open('names.txt', 'w') as f:
    for repo in org.iter_repos():
        name = repo.full_name.strip('conda-forge/')
        if 'feedstock' in name and 'feedstocks' not in name:
            f.write(name.strip('-feedstock'))
            f.write('\n')

