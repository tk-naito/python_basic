import python_basic_41_utils
# random モジュールを読み込んでください
import random

print('じゃんけんをはじめます')
player_name = input('名前を入力してください：')
print('何を出しますか？（0: グー, 1: チョキ, 2: パー）')
player_hand = int(input('数字で入力してください：'))

if python_basic_41_utils.validate(player_hand):
    # randint を用いて 0 から 2 までの数値を取得し、変数 computer_hand に代入してください
    computer_hand = random.randint(0,2)
    
    if player_name == '':
        python_basic_41_utils.print_hand(player_hand)
    else:
        python_basic_41_utils.print_hand(player_hand, player_name)

    python_basic_41_utils.print_hand(computer_hand, 'コンピューター')
    
    result = python_basic_41_utils.judge(player_hand, computer_hand)
    print('結果は' + result + 'でした')
else:
    print('正しい数値を入力してください')


# utils モジュール内の関数 validate を呼び出してください
if python_basic_41_utils.validate(player_hand):
    computer_hand = 1

    if player_name == '':
        # utils モジュール内の関数 print_hand を呼び出してください
        python_basic_41_utils.print_hand(player_hand)
    else:
        # utils モジュール内の関数 print_hand を呼び出してください
        python_basic_41_utils.print_hand(player_hand, player_name)

    # utils モジュール内の関数 print_hand を呼び出してください
    python_basic_41_utils.print_hand(computer_hand, 'コンピュータ')
    
    # utils モジュール内の関数 judge を呼び出してください
    result = python_basic_41_utils.judge(player_hand, computer_hand)
    print('結果は' + result + 'でした')
else:
    print('正しい数値を入力してください')