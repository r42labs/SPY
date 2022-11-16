from core.client import IClient, AsyncClient
from core.traker import ITraker, BaseTraker
from core.parser import IParser, BaseParser
import pandas as pd

class WebCrawler:
    def __init__(self, traker: ITraker, parser: IParser, 
        client: IClient = AsyncClient,
    ):
        self.client = client()
        self.traker = traker()
        self.parser = parser()

    def crawl(self, base_url: str):
        data = []
        urls = self.traker.get_urls(base_url)

        print(f'iniciando crawling de dados em {len(urls)} paginas')

        responses = self.client.run(urls)
        for response in responses:
            data.append(self.parser.parse(response))

        data = pd.concat(data)
        return data


