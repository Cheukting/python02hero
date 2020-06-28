class Basket:

    def __init__(self):
      self.content = []
      self.add_multi_items = self.add_items

    def __add_item(self, item):
      self.content.append(item)
      print(f"{item} is added to basket.")

    def add_items(self, *args):
        """This method add items to the content"""
        for item in args:
            self.__add_item(item)

my_basket = Basket()

my_basket.__add_item("toilet papers")
print("My basket: ", my_basket.content)
