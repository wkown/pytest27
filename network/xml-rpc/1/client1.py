__author__ = 'weijie'
import xmlrpclib

server = xmlrpclib.ServerProxy("http://localhost:8888")
month = server.getMonth(2002, 8)
print month