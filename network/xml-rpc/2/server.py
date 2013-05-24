__author__ = 'weijie'
from SimpleXMLRPCServer import SimpleXMLRPCServer


def add(a, b):
    return a + b


server = SimpleXMLRPCServer(("", 8003))
server.register_function(add)
server.register_instance
server.serve_forever()