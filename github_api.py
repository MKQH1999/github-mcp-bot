from github import Github

class GitHubClient:
    def __init__(self, token):
        self.gh = Github(token)

    def post_issue_comment(self, repo_full_name, issue_number, body):
        repo = self.gh.get_repo(repo_full_name)
        issue = repo.get_issue(number=issue_number)
        issue.create_comment(body)
