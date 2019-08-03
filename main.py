from scrapers import SeznamReality
from pprint import pprint
import asyncio

host_s_reality = "https://www.sreality.cz"
path_s_reality = "/hledani/prodej/domy/pamatky-jine,rodinne-domy,zemedelske-usedlosti,vily/brno,blansko,brno-venkov,vyskov?plocha-od=0&plocha-do=10000000000&cena-od=0&cena-do=7500000&plocha-pozemku-od=950&plocha-pozemku-do=10000000000"
path_s_reality_empty = "/hledani/prodej/domy/pamatky-jine,rodinne-domy,zemedelske-usedlosti/brno,blansko,brno-venkov,vyskov?plocha-od=0&plocha-do=10000000000&cena-od=0&cena-do=7500000&plocha-pozemku-od=1250&plocha-pozemku-do=1250"

scrapers = [
    SeznamReality(host_s_reality, path_s_reality),
    SeznamReality(host_s_reality, path_s_reality_empty)
]


async def main():
    pprint('Running...')

    for scraper in scrapers:
        async for item in scraper.get_items():
            pprint(item)

    pprint('Stopping...')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
