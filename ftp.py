import configparser
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


config = configparser.ConfigParser()
config.read('settings.ini')

login = config['CONFIG']['login']
password = config['CONFIG']['password']
ftp_path = config['CONFIG']['ftp_path']

authorizer= DummyAuthorizer()
authorizer.add_user(login,password,ftp_path, perm='elradfmwMT')

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(('',21),handler)
server.serve_forever()