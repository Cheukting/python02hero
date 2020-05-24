class Basket:

    def __init__(self, database, name, address):
        self.__id = len(database.keys())+1
        self.__name = name
        self.__address = address
        self.__content = []
        self.add_multi_items = self.add_items
        database[self.__id] = self

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, input):
        if type(input) != str:
            raise ValueError("Name need to be a string")
        self.__name = input

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, input):
        if type(input) != str:
            raise ValueError("Address need to be a string")
        self.__address = input

    @property
    def content(self):
        print("In the basket there are:")
        for item in self.__content:
            print(item)
        return self.__content

    @content.setter
    def content(self, input):
        if type(input) != list:
            raise ValueError("Content need to be a list")
        self.__content = input

    def _add_item(self, item):
        self.__content.append(item)
        print(f"{item} is added to basket.")

    def add_items(self, *args):
        """This method add items to the content"""
        for item in args:
            self._add_item(item)

database = {}

my_basket = Basket(database, "Cheuk", "123 Williton Street, London, UK")
my_basket.add_items("toilet papers")
my_basket.content = ["coffee beans", "toiler papers"]
the_content = my_basket.content
print("My basket: ", my_basket.content)

#print(database[1].address)
