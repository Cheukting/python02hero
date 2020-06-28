class Person:
    def __init__(self):
        print("creating person")
        self.__name='unknow'
    @property
    def name(self):
        print("calling getter")
        return self.__name
    @name.setter
    def name(self, value):
        print("calling setter")
        self.__name=value
    @name.deleter
    def name(self):
        print('Deleting..')
        del self.__name

me = Person()
me.name = "Cheuk"
del me.name
