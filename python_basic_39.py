def validate(hand):
    if hand < 0 or hand > 2:
        return False
    return True

def print_hand(hand, name='ゲスト'):
    hands = ['グー', 'チョキ', 'パー']
    print(name + 'は' + hands[hand] + 'を出しました')

# 関数 judge を定義してください
# judgeという名前の関数を定義して、引数を受け取れるようにしてください。
# ただし、第１引数に対応する仮引数名をplayer
# 第２引数に対応する仮引数名をcomputerとしてください。
def judge(player,computer) :
    if player == computer :
        return '引き分け'
    elif player == 0 and computer == 1:
         return '勝ち'
    elif player == 1 and computer == 2:
          return '勝ち'
    elif player == 2 and computer == 0:
        return '勝ち'
    else :
        return '負け'


    # player と computer の比較結果によって条件を分岐してください
    # playerとcomputerが等しいとき、文字列'引き分け'を戻り値として返してください。  
    # ・playerの値が0、computerの値が1 ・playerの値が1、computerの値が2 ・playerの値が2、computerの値が0
    # 上記３つの条件のとき、それぞれ文字列'勝ち'を戻り値として返してください。
    # ただし、それぞれの条件は「or」 ではなく、１つずつ「elif」を用いてください。
    # 上記以外の場合、文字列'負け'を戻り値として返してください。


    

print('じゃんけんをはじめます')
player_name = input('名前を入力してください：')
print('何を出しますか？（0: グー, 1: チョキ, 2: パー）')
player_hand = int(input('数字で入力してください：'))

if validate(player_hand):
    computer_hand = 1
   
    if player_name == '':
        print_hand(player_hand)
    else:
        print_hand(player_hand, player_name)
    
    print_hand(computer_hand, 'コンピューター')
    
    # 変数 result に関数 judge の戻り値を代入してください(第１引数は変数player_hand、第２引数は変数computer_handとしてください。)
    result = judge(player_hand,computer_hand)
    # 変数 result を出力してください(結果は○○でしたとなるように出力してください。○○には変数resultを入れてください。)
    
    print('結果は' + str(result) + 'でした')

else:
    print('正しい数値を入力してください')