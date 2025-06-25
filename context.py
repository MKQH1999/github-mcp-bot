class ContextHandler:
    def create_from_issue(self, payload):
        repo = payload["repository"]["full_name"]
        issue = payload["issue"]
        return {
            "repo": repo,
            "issue_number": issue["number"],
            "title": issue["title"],
            "body": issue["body"],
            "user": issue["user"]["login"],
        }
