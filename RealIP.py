# -*- coding: UTF-8 -*-
import sys
import requests
import socket
from lxml import etree


class MOdule(object):
    def __init__(self):
        self.url = str(sys.argv[1])
        self.source1 = "https://ping.chinaz.com/%s"%self.url
        self.xpath = "/html/body/div[5]/div[2]/div[2]/div[2]/a"
        self.source2 = "https://tool.chinaz.com/nslookup"
    #内部检测
    def getIP(self):
        if self.url.startswith("http://"):
            self.url = self.url[7:]
        elif self.url.startswith("https://"):
            self.url = self.url[8:]
        myaddr = socket.getaddrinfo(self.url,'http')
        print(myaddr[0][4][0])

    def nslookup(self):
        data = {
            "host": self.url,
            "server": "8.8.8.8",
            "t": 0
        }
        res = requests.post(self.source2,data).text
        path = "/html/body/div[2]/div[2]/div/ul/li/div[2]/span/text()"
        tree = etree.HTML(res)
        for i in iter(tree.xpath(path)):print("nslookup 解析的IP：",i)


        #print(res)

    def MorePing(self):
        pass





m = MOdule()
m.nslookup()
m.getIP()