from send_email import sendEmails
from template_email import getTemplate
from agent_saas.agent import getArticlesIa 
from articles import getArticles
import schedule
import time

def articles():
    print("passou aqui")
    articlesFilter = getArticles()
    articlesTeste = []   
    for i in articlesFilter:
        articlesTeste.append(i['title'])
    sentence = "\n".join(articlesTeste)
    articles = getArticlesIa(sentence)
    template = getTemplate(articles)
    sendEmails(template)
    return "Email enviado com sucesso"

# schedule.every(1).monday.at("19:15").do(articles)
schedule.every(5).seconds.do(articles)

while True:
    schedule.run_pending()
    time.sleep(1)




    