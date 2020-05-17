import pytest
from .e_shop import Basket

database = {}

class TestBasket:

    def test_create_basket(self):
        my_basket = Basket(database, "Cheuk", "123 Williton Street")

        assert my_basket.id == 1
        assert my_basket.name == "Cheuk"
        assert my_basket.address == "123 Williton Street"
        assert my_basket.content == []

    def test_add_item(self):
        my_basket = Basket(database, "Cheuk", "123 Williton Street")
        my_basket._add_item("apple")
        assert my_basket.content == ["apple"]

    def test_add_items(self):
        my_basket = Basket(database, "Cheuk", "123 Williton Street")
        item_list = ['apple', 'orange']
        my_basket.add_items(*item_list)
        assert my_basket.content == item_list
