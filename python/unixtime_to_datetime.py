# -*- coding: utf-8 -*-

import pandas as pd
import time
from datetime import datetime


def datetime_to_epoch(d):
    return int(time.mktime(d.timetuple()))

def epoch_to_datetime(epoch):
    return datetime(*time.localtime(epoch)[:6])


# 現在時刻取得
now = datetime.now()
print (now)

# 日時をepoch表記に変換
epoch = datetime_to_epoch(now)
print (epoch)

# epoch表記から日時表記に変換
print ( epoch_to_datetime(epoch) )

print("-----------------------------------")

# データフレーム作成
df1 = pd.DataFrame(
    {'No': ['1', '2', '3', '4', '5'],
     'epoch': [1485812560, 1485812961, 1485813000, 1485813020, 1485813100]
     })

df2 = pd.DataFrame(
    {'No': ['1', '2', '3', '4', '5'],
     'epoch': [1485812560, 1485812560, 1485813000, 1485813020, 1485813100]
     })

df3 = pd.DataFrame(
    {'No': ['1', '2', '3', '4', '5'],
     'epoch': ["1485812561", "1485812562", "1485813003", "1485813024", "1485813100"]
     })

# データフレームのepoch表記を全て日時表記に変換
for i in range(0, len(df1.index)):
    T = df1.ix[i, 'epoch']
#    print(T)
    df1.ix[i, 'date'] = epoch_to_datetime(T)
#    print ( df1 )

print("-----------------------------------")

# データフレームの日時表記を秒単位切り捨て
for i in range(0, len(df1.index)):
    T = df1.ix[i, 'epoch']
    # print(T)
    U = df1.ix[i, 'date']
    # print(U)
    # print(type(U))
    # datetimeから文字列型への変換
    V = U.strftime("%Y-%m-%d %H:%M")
    # print(V)
    # print(type(V))
    df1.ix[i, 'date_YMDHM'] = V

del df1['No']

# print(df1)


### start joinテストのためにデータフレーム2を作成 #####################################################################
# データフレームのepoch表記を全て日時表記に変換
for i in range(0, len(df2.index)):
    T = df2.ix[i, 'epoch']
#    print(T)
    df2.ix[i, 'date'] = epoch_to_datetime(T)
#    print ( df2 )

print("-----------------------------------")

# データフレームの日時表記を秒単位切り捨て
for i in range(0, len(df2.index)):
    T = df2.ix[i, 'epoch']
    # print(T)
    U = df2.ix[i, 'date']
    # print(U)
    # print(type(U))
    # datetimeから文字列型への変換
    V = U.strftime("%Y-%m-%d %H:%M")
    # print(V)
    # print(type(V))
    df2.ix[i, 'date_YMDHM'] = V

del df2['No']

# print(df2)
### end joinテストのためにデータフレーム2を作成 #####################################################################

# 2つのデータフレームを連結
W = pd.merge(df1, df2, how = 'left', left_on = 'date_YMDHM', right_on = 'date_YMDHM')
# print(W)
# マージしたデータフレームからデータセット作成
Q = W[['epoch_x', 'date_YMDHM']].head()
# print(Q)


### データフレーム3 エポックタイムが文字列だった場合 ###
# エポックタイムを全てint型に変換する
for i in range(0, len(df3.index)):
    df3.ix[i, 'epoch'] = int(df3.ix[i, 'epoch'])

# 理由はわからないが、float型で入ってしまうので 列ごとint型に型変換する
df3['epoch'] = df3['epoch'].astype(int)

# エポックタイムを日付表記に変換する
for i in range(0, len(df3.index)):
    R = df3.ix[i, 'epoch']
#    print(T)
    df3.ix[i, 'date'] = epoch_to_datetime(R)
    X = df3.ix[i, 'date']
    Y = X.strftime("%Y-%m-%d %H:%M")
    df3.ix[i, 'date_YMDHM'] = Y
# print(df3)
