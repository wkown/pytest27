__author__ = 'weijie'
import calendar, SimpleXMLRPCServer
#The server object
class Calendar:
    def getMonth(self, year, month):
        return calendar.month(year, month)

    def getYear(self, year):
        return calendar.calendar(year)


calendar_object = Calendar()
server = SimpleXMLRPCServer.SimpleXMLRPCServer(("localhost", 6888))
server.register_instance(calendar_object)
#Go into the main listener loop
print "Listening on port 8888"
server.serve_forever()