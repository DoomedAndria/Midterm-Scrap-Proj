import bs4

from models.Category import Category
from scraper.Scraper import Scraper


class Product:
    def __init__(self, name, price, url):
        self.name = name
        self.price = price
        self.url = url
        self.category = None
        self.description = None
        self.brand = None
        self.image = None

        self.soup: bs4.element.Tag | None = None


    def _get_category(self):
        try:
            return self.soup.find('span', string='კატეგორია:').find_next_sibling().get_text()
        except AttributeError:
            return None


    def _get_description(self):
        return (self.soup.find('div', attrs={'class': 'small_desc'})
                .find('p').get_text().strip())


    def _get_brand(self):
        try:
            return (self.soup.find('div', attrs={'class': 'product_info'})
                    .find_all('li')[1].find('a').get_text())
        except (IndexError,AttributeError):
            return None


    def _get_image(self):
        return (self.soup.find('div', attrs={'class': 'main_image'})
                .find('a').get('href'))


    def get_details(self):
        self.soup = Scraper.fetch_and_parse_page(self.url)

        self.category = self._get_category()
        self.description = self._get_description()
        self.brand = self._get_brand()
        self.image = self._get_image()


    def get_json(self):
        return {
            'name': self.name,
            'price': self.price,
            'url': self.url,
            'category': self.category,
            'description': self.description,
            'brand': self.brand,
            'image': self.image
        }


    def __str__(self):
        return (f'name: {self.name}\n'
                f'price: {self.price}\n'
                f'url: {self.url}\n'
                f'category: {self.category}\n'
                f'description: {self.description}\n'
                f'brand: {self.brand}\n'
                f'image: {self.image}\n')
