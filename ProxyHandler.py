# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 21:00:47 2016

@author: composersyf
"""

import time
import os
os.chdir('/home/composersyf/Documents/Google Civic Information API')

import socks
import socket
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
socket.socket = socks.socksocket

import urllib2
import requests
from bs4 import BeautifulSoup
import re

import pandas as pd


def modify_address(address):
    string1=re.sub("-","%2D",address)
    string2=re.sub("#","%23",string1)
    string3=re.sub("[^0-9a-zA-Z '%]","",string2)
    string4=re.sub(" ","+",string3)
    return string4

address_data=pd.read_csv("civicnation_address_vote_wave1_clean.csv")


html_pages=[]
for i in range(2):
    if i%80==0:
        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
        socket.socket = socks.socksocket
    proxy_handler = urllib2.ProxyHandler({"tcp":"http://127.0.0.2:9050"})
    opener = urllib2.build_opener(proxy_handler)
    urllib2.install_opener(opener)
    url_part1="https://www.melissadata.com/lookups/AddressCheck.asp?exprbox="
    url_part2=modify_address(address_data.iloc[2000+i,5])
    url=url_part1+url_part2
    html_pages.append(urllib2.urlopen(url).read())
    

with Controller.from_port(port = 9051) as controller:
  controller.authenticate()
  controller.signal(Signal.NEWNYM)


