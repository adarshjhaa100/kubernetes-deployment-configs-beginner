import os
from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop 
from datetime import datetime

class SimpleRequestHandler(RequestHandler):
    def get(self):
        print(datetime.now())
        self.write(f"Node Info : \n{os.uname()}\n")
        self.set_header("Access-Control-Allow-Origin","*")

class PingRequestHandler(RequestHandler):
    def get(self):
        self.write(f" Hello from: {os.uname().nodename} ")


if __name__=="__main__":
    print("Computer Name :", os.uname() ) # gets computer info
    app =Application([
        (r'/',SimpleRequestHandler),
        (r'/ping',PingRequestHandler)
    ])

    port = 8081
    app.listen(port)
    print("listening on :",port)
    IOLoop.current().start() # start server
