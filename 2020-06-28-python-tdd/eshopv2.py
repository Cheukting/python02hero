class Database:
    def __init__(self):
        self._all_baskets = []

    def add_basket(self, bsk_id):
        self._all_baskets.append(bsk_id)

class Basket:
    def __init__(self, user_name, db):
        self._name = user_name
        self._content = []
        my_id = len(db._all_baskets)
        self._id = my_id
        db.add_basket(my_id)

    def add_item(self, item):
        self._content.append(item)
