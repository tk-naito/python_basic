fruits = {'apple': 'りんご', 'banana': 'バナナ', 'grape': 'ぶどう'}

# for 文を用いて、辞書のキーを1つずつ取り出し、繰り返しの中で「 ◯◯は△△という意味です 」と出力させてください
for fruits_key in fruits :
    print(fruits_key + 'は' + fruits[fruits_key] + 'という意味です')