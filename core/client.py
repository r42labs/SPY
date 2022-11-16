from abc import ABC, abstractmethod
import asyncio
import httpx

class IClient(ABC):
    @abstractmethod
    def run(self, *urls):
        pass

class AsyncClient(IClient):

    async def get(self, url, client):
        response = await client.get(url)
        html = response.text
        return html


    async def fetch(self, urls):
        async with httpx.AsyncClient(http2=True) as client:
            tasks = [
                self.get(url, client)
                for url in urls
            ]

            responses = await asyncio.gather(*tasks)
            self.responses = responses

    def run(self, urls):

        asyncio.run(self.fetch(urls))
        return self.responses



