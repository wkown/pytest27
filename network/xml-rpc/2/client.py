__author__ = 'weijie'
from xmlrpclib import ServerProxy

server = ServerProxy("http://192.168.135.95:8003")

try:
    ret = server.add(156, 156)
    print 'result', ret
    print 'result type', type(ret)
except Exception as ex:
    print "execption", ex