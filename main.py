from send_email import sendEmails
from agent_template.agent import getTemplate
from agent_saas.agent import getArticlesIa 
from articles import getArticles
import schedule
import time

def articles():
    print("Passou aqui em!")
    articlesFilter = getArticles()
    articlesTeste = []   
    for i in articlesFilter:
        articlesTeste.append(i['title'])
    sentence = "\n".join(articlesTeste)
    articles = getArticlesIa(sentence)
    template = getTemplate(articles)
    sendEmails(template)
    return "Email enviado com sucesso"

schedule.every(1).monday.at("19:15").do(articles)

while True:
    schedule.run_pending()
    time.sleep(1)




    