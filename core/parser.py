from abc import ABC, abstractmethod
from parsel import Selector
import pandas as pd

class IParser:
    @abstractmethod
    def parse(self, html):
        pass

class BaseParser(IParser):
    def parse(self, response):
        data = {}

        response = Selector(response)

        for unique_field in self.unique_fields:
            data[unique_field[0]] = response.css(unique_field[1]).get()

        for field in self.fields:
            data[field[0]] = response.css(field[1]).getall()

        return pd.DataFrame(data)


        


