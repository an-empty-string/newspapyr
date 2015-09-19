from service import method
from service.db import User, Article, ArticleVote, ArticleKeywordVote, Keyword

@method("article.list")
def recent_articles(args):
    return dict(articles=list(Article.select().order_by(Article.time.desc()).limit(100)))

@method("article.list_all")
def all_articles(args):
    return dict(articles=list(Article.select()))

def user_article_vote(args, score):
    try:
        ArticleVote.delete().where(ArticleVote.article.id == args["aid"]).execute()
        ArticleVote.create(user=User.get(args["uid"], article=Article.get(args["aid"]), score=1))
    except:
        return False

@method("article.like")
def like_article(args):
    return dict(success=user_article_vote(args, 1))

@method("article.dislike")
def dislike_article(args):
    return dict(success=user_article_vote(args, -1))

@method("tag.for_article")
def article_tags(args):
    return dict(tags=[i.word for i in Keyword.select().where(Keyword.article == Article.get(args["aid"]))])

def tag_article_vote(args, score):
    # the foreign keys are real
    try:
        ArticleKeywordVote.delete().where(ArticleKeywordVote.article_keyword.article.id == args["aid"] & ArticleKeywordVote.article_keyword.keyword.word == args["word"] & ArticleKeywordVote.user.id == args["uid"]).execute()
        article = Article.get(args["aid"])
        user = User.get(args["uid"])
        ak = list(ArticleKeyword.select().where(ArticleKeyword.article.id == args["aid"] & ArticleKeyword.keyword.word == args["word"]))
        if not ak:
            k = list(Keyword.select().where(Keyword.word == args["word"]))
            if not k:
                k = [Keyword.create(word=args["word"])]
            ak = [ArticleKeyword.create(article=article, keyword=k)]
        ArticleKeywordVote.create(user=user, article_keyword=ak[0], score=score)
        return True
    except:
        return False

@method("tag.upvote")
def upvote_tag(args):
    return dict(success=tag_article_vote(args, 1))

@method("tag.downvote")
def downvote_tag(args):
    return dict(success=tag_article_vote(args, 0))
