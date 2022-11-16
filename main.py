from core import crawler, parser, traker

class GameTraker(traker.BaseTraker):
    category_selector = 'div.para > a::attr(href)'
    page_selector = 'div.page > a::attr(href)'

class GameParser(parser.BaseParser):
    unique_fields = [
        ['game_plataform', 'li.active > a::text']
    ]
    fields = [
        ['game_title','span[itemprop="name"]::text']
    ]

df = crawler.WebCrawler(GameTraker, GameParser).crawl('https://www.freeroms.com')
print(df)
df.to_json(r'data.json', orient='records')
