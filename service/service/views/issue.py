from service import method
from service.db import User, Issue, Keyword, IssueKeyword

@method("issue.list")
def recent_issues(args):
    return dict(articles=list(Issue.select().order_by(Issue.time.desc()).limit(100)))

@method("issue.list_all")
def all_issues(args):
    return dict(articles=list(Issue.select()))

@method("tag.for_issue")
def issue_tags(args):
    return dict(tags=[i.word for i in Keyword.select().where(Keyword.article == Issue.get(args["aid"]))])
