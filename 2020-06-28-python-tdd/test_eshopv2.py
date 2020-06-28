from hypothesis import given
from hypothesis.strategies import integers, text
from eshopv2 import Basket, Database

class TestBasket:
    def test_init_basket(self):
        my_db = Database()
        user_name = "cheuk"
        content = []
        my_basket = Basket(user_name, my_db)
        assert my_basket._name == user_name
        assert my_basket._content == []
        assert my_basket._id == 0

    def test_2_baskets(self):
        my_db = Database()
        basket1 = Basket("cheuk", my_db)
        basket2 = Basket("amy", my_db)
        assert basket1._id == 0
        assert basket2._id == 1

    @given(text())
    def test_add_item_to_bsk(self, item):
        my_db = Database()
        user_name = "cheuk"
        my_basket = Basket(user_name, my_db)
        my_basket.add_item(item)
        assert my_basket._content == [item]

class TestDatabase:
    def test_init_database(self):
        my_db = Database()
        assert my_db._all_baskets == []

    @given(integers(0,999))
    def test_add_basket(self, bsk_id):
        my_db = Database()
        my_db.add_basket(bsk_id)
        assert my_db._all_baskets == [bsk_id]
