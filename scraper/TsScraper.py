import bs4

from models.Category import Category
from models.Product import Product
from scraper.Scraper import Scraper


class TsScraper(Scraper):
    def __init__(self):
        super().__init__(
            'https://www.citadeli.com',
            'T'
        )
        self.products_page = self.validate_url(self, '/products')


    def get_categories(self):
        url = self.products_page

        soup = self.fetch_and_parse_page(url)
        c_list = (soup.find('div', attrs={'class': 'products_filters'})
                  .select_one('div > div.categories_list')).find('ul')
        return [self.get_category_tree(c) for c in c_list.find_all('li', recursive=False)]


    def get_category_tree(self, li: bs4.element.Tag):
        a = li.find('a')
        category = Category(a.get_text().strip(), a.get('href'))
        ul = li.find('ul')
        if ul:
            for i in ul.find_all('li', recursive=False):
                category.add_child(self.get_category_tree(i))
        return category


    def get_products(self, url):
        url = self.validate_url(self, url)
        soup = self.fetch_and_parse_page(url)


        def get_last_page_num(s: bs4.element.Tag):
            pg = soup.find('div',attrs={'class':'pagination'})
            if pg:
                return int(pg.find_all('li')[-2].get_text())
            return 1

        def get_products_from_page(url_):
            soup_ = self.fetch_and_parse_page(url_)
            p_list = soup_.find('div', attrs={'class': 'products_list_inner'}).find_all('div', recursive=False)


            def get_name(pr: bs4.element.Tag):
                return (pr.find('div', attrs={'class': 'pr_left'}).find('h2')
                        .get_text().strip())


            def get_price(pr: bs4.element.Tag):
                try:
                    price = pr.find('div', attrs={'class': 'pr_left'}).find('span', attrs={'class': 'price'})
                    price = price.get_text().strip()
                except AttributeError:
                    price = ''
                return price


            def get_url(pr: bs4.element.Tag):
                url1 = pr.find('div', attrs={'class': 'pr_left'}).find('a').get('href')
                return self.validate_url(self, url1)

            return list(map(
                lambda x: Product(get_name(x),get_price(x),get_url(x)),
                p_list
            ))

        products = []

        for i in range(1,get_last_page_num(soup)+1):
            new_url = f'{url}?page={i}'
            products+=get_products_from_page(new_url)
            print(f'\r progress: {i/get_last_page_num(soup)*100}%',end='')

        return products
