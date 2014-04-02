import tornado.ioloop
import tornado.web
import json

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello World")

def main():
    application = tornado.web.Application([(r"/", MainHandler),])
    port = 8080
    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()