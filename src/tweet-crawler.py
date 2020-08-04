import tweepy
import os

# 先ほど取得した各種キーを代入する
CK=os.environ['API_KEY']
CS=os.environ['API_SECRET_KEY']
AT=os.environ['ACCESS_TOKEN']
AS=os.environ['ACCESS_TOKEN_SECRET']

# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)

api = tweepy.API(auth)

#1ツイートずつループ
for status in api.home_timeline():
    #見映えのため区切る
    print('-------------------------------------------')
    #ユーザ名表示
    print('name:' + status.user.name)
    #内容表示
    print(status.text)