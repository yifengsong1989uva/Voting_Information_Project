# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 21:39:23 2016

@author: composersyf
"""

import sys
import os
import csv
import re

#os.chdir("~/mydata")
os.chdir('/home/composersyf/Documents/Google Civic Information API')

def main():
    with open(sys.argv[1]) as csvfile:
        mydata=csv.reader(csvfile,delimiter=",")
        count=0
        for row in mydata:
            count+=1
            cleaned_address=re.sub("[^a-zA-Z0-9# \'\-]","",row[0])
            cleaned_address=re.sub("[#]","%23",cleaned_address)
            cleaned_address=re.sub("[\-]","%2D",cleaned_address)
            cleaned_address=re.sub("[\']","%27",cleaned_address)
            cleaned_address=re.sub("[ ]","%20",cleaned_address)
            print cleaned_address+","+str(count)
            
if __name__ == '__main__':
    main()
