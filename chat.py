#!/usr /bin/env python
# -*- coding: utf-8 -*-
# Created by qiu on 16-7-4
#
from wxbot import WXBot
import os
import tornado.web
import tornado.httpserver
import tornado.ioloop


class BaseHandler(tornado.web.RequestHandler):
    @property
    def bot(self):
        return self.settings["bot"]

class LoginHandler(BaseHandler):
    def get(self):
        self.bot.run()
        self.render("login.html")
    def post(self):
        self.bot.wait_after()
        self.write("登录成功哦！")

class MainHandler(BaseHandler):
    def get(self):
        contacts = self.bot.contact_list
        myself = self.bot.my_account["UserName"]
        # print self.bot.my_account["NickName"]

        self.bot.get_icon(myself)
        for item in contacts:
            self.bot.get_icon(item["UserName"])

        self.render("index.html", contacts=contacts, myself=myself)

    def post(self):
        nickname = self.get_argument("nick", None)
        msg = self.get_argument("msg", None)

        if not nickname:
            self.write("好友不存在")
            return
        if not msg:
            self.write("消息失败")
            return
        self.bot.send_msg(nickname.encode("utf-8"), msg.encode("utf-8"), isfile=False)
        print msg, nickname

        msg = self.bot.proc_msg()

        self.write(msg["content"]['data'])



class Application(tornado.web.Application):
    def __init__(self):
        headlers = [
            (r"/", LoginHandler),
            (r"/chat", MainHandler),
        ]
        settings = {
            # "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
            # "xsrf_cookies": True,
            "bot" : WXBot(),
            "debug": True,
            "template_path": os.path.join(os.path.dirname(__file__), "templates"),
            "static_path": os.path.join(os.path.dirname(__file__), "static"),
        }

        super(Application, self).__init__(headlers, **settings)

if __name__ == '__main__':

    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(8008)
    tornado.ioloop.IOLoop.current().start()




