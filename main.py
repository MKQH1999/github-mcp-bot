from fastapi import FastAPI, Request
from context import ContextHandler
from gpt_agent import GPTAgent
from github_api import GitHubClient
from tracker import ProjectTracker
from reports import ProjectReporter
import os

app = FastAPI()
ctx_handler = ContextHandler()
gpt = GPTAgent(api_key=os.getenv("OPENAI_API_KEY"))
gh = GitHubClient(token=os.getenv("GITHUB_TOKEN"))

@app.post("/webhook")
async def github_webhook(req: Request):
    payload = await req.json()
    if "issue" in payload:
        ctx = ctx_handler.create_from_issue(payload)
        reply = gpt.reply_to_issue(ctx)
        gh.post_issue_comment(ctx["repo"], ctx["issue_number"], reply)
    return {"ok": True}

@app.get("/project-report/{repo_name}")
def project_report(repo_name: str):
    tracker = ProjectTracker(os.getenv("GITHUB_TOKEN"))
    context = tracker.get_context(repo_name)

    reporter = ProjectReporter(os.getenv("OPENAI_API_KEY"))
    summary = reporter.generate_report(context)

    return {"summary": summary, "context": context}
