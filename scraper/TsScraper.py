import bs4

from models.Category import Category
from scraper.Scraper import Scraper


class TsScraper(Scraper):
    def __init__(self):
        super().__init__(
            'https://www.citadeli.com',
            'T'
        )


    def get_categories(self):
        url = self._URL + '/products'
        soup = self._fetch_and_parse_page(url)
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
