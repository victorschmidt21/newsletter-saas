from services.email_send import sendEmails
from templates.email_template import getTemplate
from services.agent_ranker.agent import getArticlesIa
from services.article_fetcher import ArticleFetcher
import schedule
import time

articleFetcher = ArticleFetcher() 
def articles():
    articlesFilter = articleFetcher.getArticles()
    articlesTeste = []   
    for i in articlesFilter:
        articlesTeste.append(i['title'])
    sentence = "\n".join(articlesTeste)
    articles = getArticlesIa(sentence)
    print(articles)
    # template = getTemplate(articles)
    # sendEmails(template)
    return "Email enviado com sucesso"

# schedule.every(5).seconds.do(articles)

# while True:
#     schedule.run_pending()
#     time.sleep(1)

articles()


    