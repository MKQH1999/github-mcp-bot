from github import Github

class ProjectTracker:
    def __init__(self, token):
        self.gh = Github(token)

    def get_context(self, repo_name):
        repo = self.gh.get_repo(repo_name)

        open_issues = repo.get_issues(state="open")
        issues_summary = [f"#{i.number}: {i.title}" for i in open_issues]

        pull_requests = repo.get_pulls(state="open")
        pr_summary = [f"#{pr.number}: {pr.title} by {pr.user.login}" for pr in pull_requests]

        branches = repo.get_branches()
        branch_names = [b.name for b in branches]

        return {
            "repo": repo_name,
            "issues": issues_summary,
            "prs": pr_summary,
            "branches": branch_names
        }
