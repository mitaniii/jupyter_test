import pandas as pd

#CSVファイルを読み込む
df = pd.read_csv('../data/test.csv')
print(df)

# print(df['年齢'] >= 40)

# print(df.loc[df['年齢'] < 50])
# print(df.loc[df['年齢'] < 50] & ['年齢', '名前'])

print(df[['年齢', '名前']][(df['年齢'] < 50) & (df['性別'] == '男性')])