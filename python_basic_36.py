# 関数 validate を定義してください
# 数値が正しい場合にはTrueを、正しくない場合にはFalseを返すようにします。
# 引数を受け取れるようにしてください。仮引数はhandとしてください。
    
    # hand の値によって条件分岐してください
    # ifを用いて、handの値が「0より小さい」、またはhandの値が「2より大きい」とき、真偽値Falseを戻り値として返してください。
    # elseを用いて、上記以外の場合、真偽値Trueを戻り値として返してください。
def validate(hand) :
    if hand <0 or hand >2 :
        return False
    else :
        return True



def print_hand(hand, name='ゲスト'):
    hands = ['グー', 'チョキ', 'パー']
    print(name + 'は' + hands[hand] + 'を出しました')

print('じゃんけんをはじめます')
player_name = input('名前を入力してください：')
print('何を出しますか？（0: グー, 1: チョキ, 2: パー）')
player_hand = int(input('数字で入力してください：'))

# 関数 validate の戻り値が True の場合、以下の if~else 文が実行されるようにしてください
if validate(player_hand) == True:
    if player_name == '':
        print_hand(player_hand)
    else:
        print_hand(player_hand, player_name)
# 関数 validate の戻り値が False の場合「 正しい数値を入力してください 」と出力してください
if validate(player_hand) == False:
    print('正しい数値を入力してください')