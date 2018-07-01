"""测试下OTCBTC的ＡＰＩ"""
import requests

url = "https://bb.otcbtc.com/api/v2/depth?market=eoseth&limit=2"
response = requests.get(url)
#返回ｐｙｔｈｏｎ数据类型
print(response.json())
print(type(response.json()))
#返回ｊｓｏｎ　ｂｙｔｅ字符串
print(response.content)
#返回ｊｓｏｎ字符串
print(response.text)
print(type(response.text))
#发现没有场外交易ＡＰＩ，这是一点遗憾
url = "https://bb.otcbtc.com/api/v2/markets"
response = requests.get(url)
for i in response.json():
	print(i['id'])