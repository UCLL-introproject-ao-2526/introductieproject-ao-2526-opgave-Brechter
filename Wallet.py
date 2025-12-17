class Bundle:
    def __init__(self, money):
        self.__amount = money

    @property
    def amount(self):
        return self.__amount
    
    @amount.setter
    def amount(self, value):
        self.__amount = value

    def AddMoney(self, money):
        self.amount += money

wallet = Bundle(100)
table = Bundle(0)