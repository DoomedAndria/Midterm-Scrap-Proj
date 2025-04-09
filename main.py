from scraper.TsScraper import TsScraper

if __name__ == '__main__':
    ts = TsScraper()
    cs = ts.get_categories()
    for c in cs:
        print(c)

