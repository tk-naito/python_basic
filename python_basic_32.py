#関数print_handがnameという第2引数を受け取れるようにしてください。
def print_hand(hand, name):
    # 「 ◯◯は□□を出しました 」と出力されるように書き換えてください
    print(name + 'は' + hand + 'を出しました')

# 第2引数に文字列「 ATラボ 」を入れてください
print_hand('グー','ATラボ')

# 第2引数に文字列「 コンピューター 」を入れてください
print_hand('パー','コンピューター')