# Food クラスと Drink クラスをそれぞれ読み込んでください
from python_basic_58_food import Food
from python_basic_58_drink import Drink


# Food クラスのインスタンスを生成して変数 food1 に代入してください
# Food()の引数には、以下の2つを順に指定してください。
# ・文字列のサンドイッチ
# ・数値の500
food1 = Food('サンドイッチ',500)


# food1 に対して info メソッドを呼び出して戻り値を出力してください
print(food1.info())

# Drink クラスのインスタンスを生成して変数 drink1 に代入してください
# Drink()の引数には、以下の2つを順に指定してください。
# ・文字列のコーヒー
# ・数値の300
drink1 = Drink('コーヒー',300)

# drink1 に対して info メソッドを呼び出して戻り値を出力してください
print(drink1.info())