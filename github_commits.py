# github_commits.py
from dataclasses import dataclass
from typing import List, Optional, Callable, Any, Dict
import requests

GITHUB_API = "https://api.github.com"

@dataclass(frozen=True)
class RepoCommits:
    repo: str
    commits: int

class GitHubApiError(Exception):
    pass

def _get_json(url: str, params: Optional[dict] = None) -> Any:
    headers = {"Accept": "application/vnd.github+json"}
    r = requests.get(url, params=params, headers=headers, timeout=10)

    if r.status_code == 404:
        raise GitHubApiError(f"Not found: {url}")
    if r.status_code == 403:
        # Often rate limit when unauthenticated
        raise GitHubApiError("Forbidden (possible rate limit).")
    if r.status_code != 200:
        raise GitHubApiError(f"HTTP {r.status_code} calling {url}")

    return r.json()

def get_repos_and_commits(username: str, per_page: int = 100, max_pages: int = 20) -> List[RepoCommits]:
    # 1) List repos for the user: GET /users/{username}/repos [web:2]
    repos_url = f"{GITHUB_API}/users/{username}/repos"
    repos = _get_json(repos_url, params={"per_page": per_page, "page": 1})

    if not isinstance(repos, list):
        raise GitHubApiError("Unexpected repos response format.")

    results: List[RepoCommits] = []

    for repo_obj in repos:
        repo_name = repo_obj.get("name")
        if not repo_name:
            continue

        # 2) List commits for each repo: GET /repos/{owner}/{repo}/commits [web:6]
        commits_url = f"{GITHUB_API}/repos/{username}/{repo_name}/commits"

        total = 0
        for page in range(1, max_pages + 1):
            commits = _get_json(commits_url, params={"per_page": per_page, "page": page})
            if not isinstance(commits, list):
                raise GitHubApiError("Unexpected commits response format.")

            total += len(commits)

            # Pagination stop condition (if fewer than per_page, last page) [web:6]
            if len(commits) < per_page:
                break

        results.append(RepoCommits(repo=repo_name, commits=total))

    return results

if __name__ == "__main__":
    user = input("GitHub username: ").strip()
    for rc in get_repos_and_commits(user):
        print(f"Repo: {rc.repo} Number of commits: {rc.commits}")
