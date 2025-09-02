import requests
from typing import List, Dict


class ArticleFetcher:
    BASE_URL = "https://www.tabnews.com.br/api/v1/contents"

    def __init__(self, keyword: str = "pitch", per_page: int = 100, max_pages: int = 2):
        self.keyword = keyword.lower()
        self.per_page = per_page
        self.max_pages = max_pages
        self.session = requests.Session()

    def filter_title(self, article: Dict) -> bool:
        title = article.get("title", "").lower()
        return self.keyword in title

    def get_articles(self) -> List[Dict]:
        articles = []

        for page in range(1, self.max_pages + 1):
            url = f"{self.BASE_URL}?per_page={self.per_page}&strategy=new&page={page}"
            try:
                response = self.session.get(url, timeout=10)
                response.raise_for_status()
                data = response.json()
                articles.extend(data)
            except requests.RequestException as e:
                print(f"Erro ao buscar artigos na página {page}: {e}")
                continue

        articles_filter = list(filter(self.filter_title, articles))
        return articles_filter

    def close(self):
        self.session.close()

