from service import method
from service.db import User, Issue, Keyword, IssueKeyword

@method("issue.list")
def recent_issues(args):
    return dict(issues=list(Issue.select().order_by(Issue.time.desc()).limit(100)))

@method("issue.list_all")
def all_issues(args):
    return dict(issues=list(Issue.select()))

@method("issue.create")
def create_issue(args):
    Title = args["title"]
    Source = args["source"]
    Time = args["time"]
    Text = args["text"]
    return dict(uid=Issue.create(title = Title, source = Source, time = Time, text = Text).id)

@method("tag.for_issue")
def issue_tags(args):
    return dict(tags=[i.word for i in Keyword.select().where(Keyword.article == Issue.get(args["aid"]))])
