from python_basic_59_menu_item import MenuItem

class Food(MenuItem):
    # calorie_info メソッドを定義してください
    # calorie_infoの中で、以下をコンソールに出力してください。
    # str(self.calorie) + 'kcalです'
    def calorie_info(self):
        print(str(self.calorie) + 'kcalです')