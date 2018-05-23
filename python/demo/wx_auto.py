#不要抄下源码就运行，你需要改动几个地方

from __future__ import unicode_literals
from threading import Timer
from wxpy import *
import requests
from wechat_sender import Sender

bot = Bot()
# bot = Bot(console_qr=2,cache_path="botoo.pkl")
#这里的二维码是用像素的形式打印出来！，如果你在win环境上运行，替换为  bot=Bot()
#获取金山词霸每日一句，英文和翻译
def get_news1():
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    contents = r.json()['content']
    translation= r.json()['translation']
    return contents,translation

def get_news2():
    url = "https://www.sojson.com/open/api/weather/json.shtml?city=杭州"
    r = requests.get(url)
    print(r.json())
    # contents = r.json()['data'].json()['ganmao']
    translation= r.json()['data']
    return translation

def send_news():
    try:
        my_friend = bot.friends().search(u'叶田')[0]    #你朋友的微信名称，不是备注，也不是微信帐号。
        print('my_friend',my_friend)
        # my_friend.send(get_news2())
        # my_friend.send(get_news1()[0])
        # my_friend.send(get_news1()[1][5:])
        # my_friend.send(u"小橙子机器人-3.2!")
       	my_friend.send(u"I miss you ！！")
        # for friend in bot.friends():
        #     print(friend)
        #     if 
        #     friend.send(u"智简生活·慧创未来")
        #     friend.send(u"来自鸿雁电器有限公司!")
        t = Timer(60, send_news)
#每86400秒（1天），发送1次，不用linux的定时任务是因为每次登陆都需要扫描二维码登陆，很麻烦的一件事，就让他一直挂着吧
        t.start()
    except:
#你的微信名称，不是微信帐号。
        print(bot.friends())
        my_friend = bot.friends().search('常念')[0]
        my_friend.send(u"今天消息发送失败了")
        

    
if __name__ == "__main__":
    send_news()
