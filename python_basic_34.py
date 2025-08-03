def print_hand(hand, name='ゲスト'):
    print(name + 'は' + hand + 'を出しました')

print('じゃんけんをはじめます')

# input を用いて入力を受け取り、変数 player_name に代入してください('名前を入力してください：'と表示されたあとに入力を受け取れるようにしてください。)
player_name = input('名前を入力してください：')
                   

# 変数 player_name の値によって関数 print_hand の呼び出し方を変更してください。変数player_nameが空文字''の場合、関数print_handの呼び出し時に第2引数を省略してください。第1引数は「グー」とします。
if player_name == '' :
    print_hand('グー')
# 変数player_nameが空文字でない場合('名前を入力してください：'で名前を入力した場合)、関数print_handの呼び出し時に、第2引数に変数player_nameを追加してください。
else :
    print_hand('グー',player_name)