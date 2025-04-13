from scraper.Scraper import Scraper


class Category:
    def __init__(self,name,url):
        self.name: str = name
        self.url: str = url

        self.parent: Category | None = None
        self.children: list[Category] | None = []


    def add_child(self, child: 'Category'):
        child.parent = self
        self.children.append(child)


    def get_breadcrumbs(self):
        return self.name if self.parent is None else \
            f'{self.parent.get_breadcrumbs()} > {self.name}'


    def __str__(self):
        return str({
            'name': self.name,
            'breadcrumb': self.get_breadcrumbs(),
            'url': self.url,
            'children': [str(child) for child in self.children]
        })

    def print_tree(self,depth = 0):
        print(depth*'   '+ self.name)
        if self.children:
            for c in self.children:
                c.print_tree(depth+1)


