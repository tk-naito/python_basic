# 3つの関数のコードを python_basic_40_utils.py に移してください（こちらのコードは消してください）


# python_basic_40_utils.py をモジュールとして読み込んでください
import python_basic_40_utils

print('じゃんけんをはじめます')
player_name = input('名前を入力してください：')
print('何を出しますか？（0: グー, 1: チョキ, 2: パー）')
player_hand = int(input('数字で入力してください：'))

# utils モジュール内の関数 validate を呼び出してください
if python_basic_40_utils.validate(player_hand):
    computer_hand = 1

    if player_name == '':
        # utils モジュール内の関数 print_hand を呼び出してください
        python_basic_40_utils.print_hand(player_hand)
    else:
        # utils モジュール内の関数 print_hand を呼び出してください
        python_basic_40_utils.print_hand(player_hand, player_name)

    # utils モジュール内の関数 print_hand を呼び出してください
    python_basic_40_utils.print_hand(computer_hand, 'コンピュータ')
    
    # utils モジュール内の関数 judge を呼び出してください
    result = python_basic_40_utils.judge(player_hand, computer_hand)
    print('結果は' + result + 'でした')
else:
    print('正しい数値を入力してください')