# -*- coding: utf-8 -*-
import socket

from SimpleXMLRPCServer import SimpleXMLRPCServer
from SocketServer import ThreadingMixIn
class ThreadXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):pass
from multiprocessing import Process
from network.dzt_crawler import DztCrawler


class CrawlerServer:
    ADDR = 'localhost'
    PORT = 15000
    def __init__(self):
        pass

    def run(self):
        if CrawlerServer.is_living():
            print ("Server already running")
            return
        obj = DztCrawler()
        server = ThreadXMLRPCServer((CrawlerServer.ADDR, CrawlerServer.PORT), allow_none=True)
        server.register_instance(obj)

        server.serve_forever()

    @classmethod
    def is_living(cls):
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sk.settimeout(1)
        ret = False
        try:
            sk.connect((cls.ADDR, cls.PORT))
            ret =  True
        except Exception:
            pass
        sk.close()
        return ret


if __name__ == '__main__':
    CrawlerServer().run()
