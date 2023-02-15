# デシジョンテーブル練習問題

def get_discount(items):
    percentage = 0.0
    if len(items) >= 7:
        percentage += 0.07

    if 'y-shirt' in items: #配列の中身を確認
        if 'necktie' in items:
            percentage += 0.05

    return percentage

items = ['necktie', 'y-shirt', 'pants', 'shoes', 'belt', 'sox', 'y-shirt', 'handkerchief']

print(get_discount(items[:7])) #0.12
print(get_discount(items[1:])) #0.07
print(get_discount(items[:2])) #0.05
print(get_discount(items[-3:])) #0.0