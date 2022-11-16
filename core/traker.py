from abc import ABC, abstractmethod
from parsel import Selector
import httpx

class ITraker(ABC):
    @abstractmethod
    def get_urls(self, html, client) -> list:
        pass

class BaseTraker(ITraker):
    def get_urls(self, base_url):
        urls = []

        client = httpx.Client(http2=True)
        html = client.get(base_url).text
        selector = Selector(html)

        category_urls = [
            f'{base_url}{path}' for path in 
            selector.css(self.category_selector).getall()
        ]

        for url in category_urls:
            html = client.get(url).text
            selector = Selector(html)
            pagination_urls = [
                f'{base_url}{path}' for path in
                selector.css(self.page_selector).getall()
            ]

            urls.extend(pagination_urls)

        return urls

        


