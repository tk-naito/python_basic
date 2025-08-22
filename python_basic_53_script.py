from python_basic_53_menu_item import MenuItem

menu_item1 = MenuItem('サンドイッチ', 500)
menu_item2 = MenuItem('チョコケーキ', 400)
menu_item3 = MenuItem('コーヒー', 300)
menu_item4 = MenuItem('オレンジジュース', 200)

# 指定されたリストを変数 menu_items に代入してください
menu_items = [menu_item1,menu_item2,menu_item3,menu_item4]
# for 文を作成してください
# for文を用いて、リストmenu_itemsの要素を1つずつ取り出し、変数itemに代入してください。

for menuitem in menu_items :
    print(menuitem.info())