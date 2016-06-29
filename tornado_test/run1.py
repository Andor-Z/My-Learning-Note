import tornado.httpserver 
# 这个模块就是用来解决web服务器的http协议问题，它提供了不少属性方法，实现客户端和服务器端的互通。Tornado的非阻塞、单线程的特点在这个模块中体现。
import tornado.ioloop
# 这个也非常重要，能够实现非阻塞socket循环，不能互通一次就结束呀。
import tornado.options
# 这是命令行解析模块，也常用到
import tornado.web
# 这是必不可少的模块，它提供了一个简单的Web框架与异步功能，从而使其扩展到大量打开的连接，使其成为理想的长轮询。

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ', welcome you to read: my web')

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()