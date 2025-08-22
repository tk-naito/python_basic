
# menu_item.py から MenuItem クラスを読み込んでください
# fromとimportを用いて、python_basic_52_menu_item.pyのMenuItemクラスを読み込んでください。

from python_basic_52_menu_item import MenuItem

menu_item1 = MenuItem('サンドイッチ', 500)

print(menu_item1.info())

result = menu_item1.get_total_price(4)
print('合計は' + str(result) + '円です')