import requests

def filterTitle(article):
    chave = 'pitch'
    title = article['title']
    return chave in title.lower()

def getArticles():
    articles = []
    urls = ['https://www.tabnews.com.br/api/v1/contents?per_page=100&strategy=new', 'https://www.tabnews.com.br/api/v1/contents?per_page=100&strategy=new&page=2']

    for url in urls:
        response = requests.get(url)
        data = response.json()
        articles.extend(data)
        
    articlesFilter = list(filter(filterTitle, articles))
    return articlesFilter

