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
        return self.soup.find('span',string='კატეგორია:').find_next_sibling().get_text()

    def _get_description(self):
        return (self.soup.find('div',attrs={'class':'small_desc'})
                .find('p').get_text().strip())

    def _get_brand(self):
        pass

    def _get_image(self):
        pass

    def get_details(self):
        """todo"""
        self.soup = Scraper.fetch_and_parse_page(self.url)

        self.category = self._get_category()
        self.description = self._get_description()
        self.brand = self._get_brand()
        self.image = self._get_image()

    def __str__(self):
        """todo"""
        return (f'name: {self.name}\n'
                f'price: {self.price}\n'
                f'url: {self.url}\n')