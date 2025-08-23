from python_basic_61_menu_item import MenuItem

class Drink(MenuItem):
    def info(self):
        return self.name + ': ¥' + str(self.price) + ' (' + str(self.amount) + 'mL)'