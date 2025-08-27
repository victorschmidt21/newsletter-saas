from typing import Union
from agent_basic import getArticlesIa
from fastapi import FastAPI
import requests
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/articles")
def getArticles():
    response = requests.get("https://www.tabnews.com.br/api/v1/contents?per_page=100&strategy=new")
    response2 = requests.get("https://www.tabnews.com.br/api/v1/contents?per_page=100&strategy=new&page=2")
    data = response.json()
    data2 = response2.json()
    data.extend(data2)

    articlesFilter = list(filter(filterTitle, data))
    articlesTeste = []
    for i in articlesFilter:
        articlesTeste.append(i['title'])
    sentence = "\n".join(articlesTeste)
    articles = getArticlesIa(sentence)
    return articles


def filterTitle(article):
    chave = 'pitch'
    title = article['title']
    return chave in title.lower()
    