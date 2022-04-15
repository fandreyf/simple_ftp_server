import configparser
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from parse_ip import get_ip

config = configparser.ConfigParser()
config.read('settings.ini')

login = config['CONFIG']['login']
password = config['CONFIG']['password']
ftp_path = config['CONFIG']['ftp_path']
ip=get_ip(1)

def main():
    authorizer= DummyAuthorizer()
    authorizer.add_user(login,password,homedir=ftp_path, perm='elradfmwMT')
    handler = FTPHandler
    handler.authorizer = authorizer
    print(f'FTP_SERVER start on:\n{ip}')
    server = FTPServer(('',21),handler)
    server.serve_forever()

if __name__ == '__main__':
    main()