from python_basic_60_menu_item import MenuItem

class Food(MenuItem):
    # info メソッドを定義してください
    # infoメソッドの中で、以下の文字列を戻り値として返してください。
    # self.name + ': ¥' + str(self.price) + ' (' + str(self.calorie) + 'kcal)'

    
    
    def calorie_info(self):
        print(str(self.calorie) + 'kcalです')