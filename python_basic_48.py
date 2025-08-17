class MenuItem:
    def info(self):
        return self.name + ': ¥' + str(self.price)

    # get_total_price メソッドを定義してください
    # ただし引数は順にself, countとしてください。
    # get_total_priceメソッドの中で、インスタンス変数priceと引数countの値をかけた結果を、変数total_priceに代入してください。
    # get_total_priceメソッドの中で、変数total_priceの値を戻り値として返してください。
    def get_total_price(self,count) :
        total_price = self.price * count
        return total_price



menu_item1 = MenuItem()
menu_item1.name = 'サンドイッチ'
menu_item1.price = 500

print(menu_item1.info())

# menu_item1に対してget_total_priceメソッドを呼び出し、その戻り値を変数resultに代入してください。
# 引数の値は数値の4としてください。
result = menu_item1.get_total_price(4)



# 「 合計は〇〇円です 」となるように出力してください
print('合計は' + str(result) + '円です')