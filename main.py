from itertools import product

from utils.file_handler import save_json
from utils.thread_pool_worker import worker_for_product_details
from models.Category import Category
from scraper.TsScraper import TsScraper
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class MenuHandler:
    def __init__(self):
        self.scraper = TsScraper()
        self.categories = self.scraper.get_categories()


    def navigate_categories(self, categories: list[Category]):
        while True:
            clear()
            print('\nCategories:')
            for idx, cat in enumerate(categories, 1):
                print(f'({idx}) {cat.name}')

            print(f'({len(categories) + 1}) Go Back')

            try:
                choice = int(input('Choose a category: ').strip())
            except ValueError:
                print('Invalid input. Please enter a number.')
                continue

            if choice == len(categories) + 1:
                return


            elif 1 <= choice <= len(categories):
                selected = categories[choice - 1]
                self.category_action_screen(selected)
            else:
                print('Invalid option. Please try again.')


    def category_action_screen(self, category: Category):
        while True:
            clear()
            print(f'\nSelected: {category.get_breadcrumbs()}')
            print('(1) Browse Subcategories')
            print('(2) Fetch Products in This Category')
            print('(3) Go Back')

            choice = input('>> ').strip()

            if choice == '1':
                if category.children:
                    self.navigate_categories(category.children)
                else:
                    print("No subcategories to browse.")
            elif choice == '2':

                products = self.scraper.get_products(category.url)
                worker_for_product_details(products)  # getting details from individual pages
                save_json(
                    f'products_{category.name}',
                    [p.get_json() for p in products]  # casting product objects into json
                )
                print(f'\rjson file generated successfully\n data count {len(products)}')
                exit()

            elif choice == '3':
                return
            else:
                print("Invalid option.")


    def scrape_everything(self):
        products = self.scraper.get_products()
        worker_for_product_details(products)
        save_json(
            f'products',
            [p.get_json() for p in products]
        )
        print(f'\rjson file generated successfully\n data count {len(products)}')
        exit()


    @staticmethod
    def show_main_menu():
        print('Please enter the number of the operation you wish to perform:')
        prompt = ('(1) Scrape By Category\n'
                  '(2) Scrape Everything\n'
                  '(3) Exit\n'
                  '>>')
        return input(prompt)


    def handle_operation(self, operation):
        operations = {
            '1': lambda: self.navigate_categories(self.categories),
            '2': self.scrape_everything,
            '3': self.exit_program
        }
        operation_function = operations.get(operation, self.invalid_option)
        operation_function()


    @staticmethod
    def exit_program():
        print('Exiting the program...')
        exit()


    @staticmethod
    def invalid_option():
        print('\nInvalid option. Please try again.')


    @staticmethod
    def return_to_main_menu():
        input('\nPress Enter to return to the main menu...')


    def run(self):
        while True:
            operation = self.show_main_menu()
            self.handle_operation(operation)


if __name__ == '__main__':
    mh = MenuHandler()
    mh.run()
