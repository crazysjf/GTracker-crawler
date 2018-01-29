# -*- coding: utf-8 -*-


from crawler_daemon import *
import xmlrpc.client

class CrawlerServerProxy:
    def __init__(self):
        self.proxy = xmlrpc.client.ServerProxy('http://localhost:15000')

    def close(self):
        pass

if __name__ == "__main__":
    if not CrawlerServer.is_living():
        print "Server not runnin"
    else:
        p = CrawlerServerProxy().proxy
        if p.need_log_in():
            b64 =  p.get_captcha()
            with open(r"captcha.jpg", 'wb') as f:
                f.write(base64.b64decode(b64))

