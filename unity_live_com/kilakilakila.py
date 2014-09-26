import sys
from twisted.internet.task import LoopingCall
from twisted.internet import reactor
from twisted.internet import defer
from twisted.web import client

# @note Social media APIs.

def mark_the_service_unavail(ip):
    print ip


def service_avail_check():
    ip_list = ['localhost']
    for i in ip_list:
        url = "http://" + i[0] + ":8000/dm/"
        print url
        server_ip = i[0]
        client\
            .getPage(url)\
            .addCallback(service_avail_handler, server_ip)\
            .addErrback(service_avail_error, server_ip)


def service_avail_handler(data, server_ip):
    if data.strip() == 'pong':
        mark_the_service_avail(server_ip)
        crawler_avail_check(server_ip)
    else:
        mark_the_service_unavail(server_ip)


def service_avail_error(failure, server_ip):
    print >> sys.stderr, "Error:", failure.getErrorMessage()
    print 'server ping error sever ip: ' + server_ip
    mark_the_service_unavail(server_ip)


lc = LoopingCall(service_avail_check)
lc.start(120)
reactor.run()
