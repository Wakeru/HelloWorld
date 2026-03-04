# test_github_commits.py
import unittest
from unittest.mock import patch
from github_commits import get_repos_and_commits, RepoCommits, GitHubApiError

class FakeResponse:
    def __init__(self, status_code, payload):
        self.status_code = status_code
        self._payload = payload
    def json(self):
        return self._payload

class TestGitHubCommits(unittest.TestCase):

    @patch("github_commits.requests.get")
    def test_one_repo_three_commits(self, mock_get):
        # /users/{u}/repos then /repos/{u}/{repo}/commits page 1
        mock_get.side_effect = [
            FakeResponse(200, [{"name": "RepoA"}]),
            FakeResponse(200, [{}, {}, {}]),
        ]
        out = get_repos_and_commits("Wakeru", per_page=100, max_pages=5)
        self.assertEqual(out, [RepoCommits(repo="RepoA", commits=3)])

    @patch("github_commits.requests.get")
    def test_pagination(self, mock_get):
        mock_get.side_effect = [
            FakeResponse(200, [{"name": "RepoA"}]),
            FakeResponse(200, [{}] * 100),  # page 1 full
            FakeResponse(200, [{}] * 7),    # page 2 partial -> stop
        ]
        out = get_repos_and_commits("Wakeru", per_page=100, max_pages=5)
        self.assertEqual(out[0].commits, 107)

    @patch("github_commits.requests.get")
    def test_user_not_found(self, mock_get):
        mock_get.return_value = FakeResponse(404, {"message": "Not Found"})
        with self.assertRaises(GitHubApiError):
            get_repos_and_commits("Wakeru")

if __name__ == "__main__":
    unittest.main()
