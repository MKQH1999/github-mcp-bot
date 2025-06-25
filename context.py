# class ContextHandler:
#     def create_from_issue(self, payload):
#         repo = payload["repository"]["full_name"]
#         issue = payload["issue"]
#         return {
#             "repo": repo,
#             "issue_number": issue["number"],
#             "title": issue["title"],
#             "body": issue["body"],
#             "user": issue["user"]["login"],
#         }

class ContextHandler:
    def create_from_issue(self, payload):
        repo = payload["repository"]["full_name"]
        issue = payload["issue"]
        user_login = issue.get("user", {}).get("login", "unknown-user")  # تأكد من وجود المفتاح user

        return {
            "repo": repo,
            "issue_number": issue["number"],   # صححت المفتاح إلى number بدل issue_number
            "title": issue["title"],
            "body": issue["body"],
            "user": user_login,
        }
