from python_basic_61_menu_item import MenuItem

class Food(MenuItem):
    # __init__ メソッドを定義してください
    # 引数にname, price, calorieを受け取れるようにしてください。
    # 以下をそれぞれ代入してください
    # ・self.nameに引数nameの値
    # ・self.priceに引数priceの値
    # ・self.calorieに引数calorieの値
    def __init__(self, name, price, calorie):
        self.name = name
        self.price = price
        self.calorie = calorie



    
    def info(self):
        return self.name + ': ¥' + str(self.price) + ' (' + str(self.calorie) + 'kcal)'
    
    def calorie_info(self):
        print(str(self.calorie) + 'kcalです')