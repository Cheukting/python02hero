class Basket:

    def __init__(self, database, name, address):
        self.id = len(database.keys())+1
        self.name = name
        self.address = address
        self.content = []
        self.add_multi_items = self.add_items
        database[self.id] = self

    def _add_item(self, item):
        self.content.append(item)
        print(f"{item} is added to basket.")

    def add_items(self, *args):
        """This method add items to the content"""
        for item in args:
            self._add_item(item)

database = {}

my_basket = Basket(database, "Cheuk", "123 Williton Street, London, UK")
my_basket.add_items("toilet papers")
print("My basket: ", my_basket.content)

print(database[1].name)
