import requests

def getRepoStats(owner,repo):
    url=f"https://api.github.com/repos/{owner}/{repo}"
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "Repository not found or Rate limit exceeded", "status": response.status_code}
    
    res=response.json()

    return {
        "name": res["name"],
        "stars": res["stargazers_count"],
        "forks": res["forks_count"],
        "open_issues": res["open_issues_count"],
        "watchers": res["watchers_count"]
    }