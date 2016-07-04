#!/usr /bin/env python
# -*- coding: utf-8 -*-
# Created by qiu on 16-7-4
#


from wxbot import *
import threading

class MyWXBot(WXBot):
    def handle_msg_all(self, msg):
        if msg['msg_type_id'] == 4 and msg['content']['type'] == 0:
            print msg["content"]["data"] + u" from: " + msg["user"]["name"]

            # re_msg = raw_input(u"from :")
            # self.send_msg(msg["user"]["name"], re_msg, isfile=False)

'''
    def schedule(self):
        self.send_msg(u'张三', u'测试')
        time.sleep(1)
'''


def main():
    bot = MyWXBot()
    # bot.DEBUG = True
    bot.conf['qr'] = 'png'
    re_msg = raw_input(u"msg: ")
    bot.send_msg(msg["user"]["name"], re_msg, isfile=False)
    bot.run()

    # threading.Thread(target=bot.send_msg(u"一个人的好天气", u"哈罗")).start()


if __name__ == '__main__':
    main()