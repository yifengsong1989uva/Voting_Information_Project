# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 21:39:23 2016

@author: composersyf
"""

import sys
import os
import csv
import re

os.chdir("/home/ec2-user")
#os.chdir('/home/composersyf/Documents/Google Civic Information API/Second_Batch')

def main():
    #with open("../Scripts/API_Keys.csv") as key_file:
    with open("mydata/API_Keys.csv") as key_file:
        key_data=csv.reader(key_file,delimiter=",")
        Keys=[]
        for row in key_data:
            Keys.append(row[0])
    with open(sys.argv[1]) as csvfile:
        mydata=csv.reader(csvfile,delimiter="\t")
        count=0
        for row in mydata:
            cleaned_address=re.sub("[^a-zA-Z0-9# \'\-]","",row[1])
            cleaned_address=re.sub("[#]","%23",cleaned_address)
            cleaned_address=re.sub("[\-]","%2D",cleaned_address)
            cleaned_address=re.sub("[\']","%27",cleaned_address)
            cleaned_address=re.sub("[ ]","%20",cleaned_address)
            print cleaned_address+","+str(row[0])+","+Keys[count%40]
            #print(cleaned_address+","+str(row[0])+","+Keys[count%40])
            count+=1
            
if __name__ == '__main__':
    main()
