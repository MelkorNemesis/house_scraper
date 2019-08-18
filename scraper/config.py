from scraper.scrapers import SeznamReality, IdnesReality

__path_s_reality_950_up = "/hledani/prodej/domy/pamatky-jine,rodinne-domy,zemedelske-usedlosti/brno,blansko,brno-venkov,vyskov?plocha-od=0&plocha-do=10000000000&cena-od=0&cena-do=7500000&plocha-pozemku-od=950&plocha-pozemku-do=10000000000"
# path_s_reality_empty = "/hledani/prodej/domy/pamatky-jine,rodinne-domy,zemedelske-usedlosti/brno,blansko,brno-venkov,vyskov?plocha-od=0&plocha-do=10000000000&cena-od=0&cena-do=7500000&plocha-pozemku-od=1250&plocha-pozemku-do=1250"
__path_idnes_reality_950_up = "/s/prodej/domy/samostatne/cena-do-7500000/?s-l=VUSC-116%3BOKRES-3701%3BOKRES-3702%3BOKRES-3703%3BOKRES-3712&s-qc%5BgroundAreaMin%5D=990&s-qc%5Blocality%5D%5B0%5D=VUSC-116&s-qc%5Blocality%5D%5B1%5D=OKRES-3701&s-qc%5Blocality%5D%5B2%5D=OKRES-3702&s-qc%5Blocality%5D%5B3%5D=OKRES-3703&s-qc%5Blocality%5D%5B4%5D=OKRES-3712"

scrapers = [
    SeznamReality(__path_s_reality_950_up),
    IdnesReality(__path_idnes_reality_950_up)
]
