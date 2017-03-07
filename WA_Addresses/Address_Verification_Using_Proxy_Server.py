# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 22:43:02 2016

@author: composersyf
"""

import os
os.chdir('/home/composersyf/Documents/Google Civic Information API/WA Addresses')
import time

import urllib2
from bs4 import BeautifulSoup
import re
import pandas as pd

import socket
import socks
from stem import Signal
from stem.control import Controller


#read in the address data
address_data=pd.read_csv("sample_WA_Addresses_5.csv",header=None)
#address_data=address_data.iloc[:,0]


#create the second part of the url query which contains the transformed address
def modify_address(address):
    #create the second part of the address verification url query which contains the transformed address
    string1=re.sub("-","%2D",address)
    string2=re.sub("#","%23",string1)
    string3=re.sub("[^0-9a-zA-Z '%]","",string2)
    string4=re.sub(" ","+",string3)
    return string4


def connect_tor_proxy():
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5 , "127.0.0.1", 9050, True)
    socket.socket = socks.socksocket


def change_tor_identity():
    #to overcome the 80 queries per day limit of Melissa DATA
    controller.authenticate()
    controller.signal(Signal.NEWNYM)


def show_current_ip():
    return urllib2.urlopen("http://checkip.amazonaws.com/").read()


def initialize_proxy():
    global controller
    controller = Controller.from_port(port = 9051)
    change_tor_identity()
    connect_tor_proxy()


def address_verification_queries():
    #initialize the entire query
    i=1
    nrow=address_data.shape[0]
    url_part1="https://www.melissadata.com/lookups/AddressCheck.asp?exprbox="
    all_used_ip=[]
    query_result=[]
    initialize_proxy()

    
    while i<=nrow:
        #change tor identity after every 80 queries finished
        if i%80==0:
            time.sleep(10)
            pd.DataFrame(query_result).to_csv("../Address_Verification_Results_2/"+str(i)+".csv",header=False,index=False)
            query_result=[]            
            change_tor_identity()
            while show_current_ip() in all_used_ip: #if an old IP address is picked up upon changing the identify, it will keep changing until a brand-new ip is found
                time.sleep(5)
                change_tor_identity()
            all_used_ip.append(show_current_ip())
            
        #should skip the empty address entry
        if pd.isnull(address_data.iloc[i-1,0])==True or address_data.iloc[i-1,0]=='':
            print str(i-1)+","+"Not Available"            
            query_result.append((i-1,"Not Available"))
            i+=1
        else:
            url_part2=modify_address(address_data.iloc[i-1,0])
            url=url_part1+url_part2
            #use BeautifulSoup to parse the resulting HTML file and extract the query results
            try:
                user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
                headers={'User-Agent':user_agent,} 
                request=urllib2.Request(url,None,headers)
                result_html=urllib2.urlopen(request).read() #Query the Melissa DATA web application       
                result_soup=BeautifulSoup(result_html,'html.parser')
                try:
                    result_table_tags=result_soup.findAll("table")[3] #The query results are stored in the 4th HTML table
                except IndexError:
                    print str(i-1)+","+"Error"
                    query_result.append((i-1,"Error"))
                    i+=1
                    continue
                result_table_first_row=result_table_tags.findAll("tr")[0] #The query results are always within the 1st row of the table
                try: #if result is "Address Verified", the text is enclosed by the <div></div> tag
                    result=result_table_first_row.findAll("div",text=True)[0].contents[0]
                except IndexError: #if result is "Address NOT Verified", the text is enclosed by the <b></b> tag
                    result=result_table_first_row.findAll("b",text=True)[0].contents[0]            
                print str(i-1)+","+result
                query_result.append((i-1,result))
                i+=1
            except (urllib2.HTTPError,urllib2.URLError): #to avoid the error caused by temporarily failed Internet Connection
                i+=1
                continue


if __name__=="__main__":
    address_verification_queries()
