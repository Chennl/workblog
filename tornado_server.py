# 创建Tornado WEB服务器
# 使用Tornado wsgi模块WSGIContiner类运行其他WSGI应用，如, Flask,Django.
# 即，Flask由Tornado托管

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop 
from workblog import app
 

container = WSGIContainer(app)
http_server = HTTPServer(container)
http_server.listen(8008)
http_server.listen(8009)
IOLoop.current().start()