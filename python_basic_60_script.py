from python_basic_60_food import Food
from python_basic_60_drink import Drink

food1 = Food('サンドイッチ', 500)
food1.calorie = 330

# food1 に対して info メソッドを呼び出して戻り値を出力してください
print(food1.info())


# Drink クラスのインスタンスを生成して変数 drink1 に代入してください
# ただし、Drink()の引数には、以下の2つを順に指定してください。
# ・文字列のコーヒー
# ・数値の300
drink1 = Drink('コーヒー',300)

# drink1 の amount に 180 を代入してください
drink1.amount = 180

# drink1 に対して info メソッドを呼び出して戻り値を出力してください
drink1.info()