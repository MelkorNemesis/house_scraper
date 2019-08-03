from scrapers import SReality
from pprint import pprint
import asyncio

url_s_reality = "https://www.sreality.cz/hledani/prodej/domy/pamatky-jine,rodinne-domy,zemedelske-usedlosti/vyskov,brno-venkov,blansko,brno?navic=samostatny&plocha-od=0&plocha-do=10000000000&cena-od=0&cena-do=7500000&plocha-pozemku-od=1250&plocha-pozemku-do=10000000000"


async def main():
    pprint('Running...')

    scrapers = [
        SReality(url_s_reality)
    ]

    for scraper in scrapers:
        async for item in scraper.get_items():
            pprint(item)

    pprint('Stopping...')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()
