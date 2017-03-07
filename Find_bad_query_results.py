# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 01:09:30 2016

@author: composersyf
"""

import os
os.chdir('/home/composersyf/Documents/Google Civic Information API/')

import pandas as pd
import numpy as np
mydata=pd.read_csv("Address_Check_Results.csv",header=None)
mydata=mydata.sort_values(by=[0])

mydata_good=mydata[(np.array(mydata.iloc[:,1])=="Address Verified ") | (np.array(mydata.iloc[:,1])=="Address NOT Verified") | (np.array(mydata.iloc[:,1])=="Not Available")]
#bad_results=pd.read_csv("Bad_results.csv",header=None)
#bad_results=bad_results.reset_index([0])
#mydata_good.merge(bad_results,how="inner",left_on=[0],right_on=['index']).iloc[:,[4,2]].to_csv("Address_Check_Results_Cleaned_2.csv",index=False,header=False)

mydata_good.to_csv("Address_Check_Results_Cleaned.csv",index=False,header=False)

bad_results=np.setdiff1d(np.array(range(20000)),np.array(mydata_good.iloc[:,0]))
pd.DataFrame(bad_results).to_csv("Bad_results.csv",index=False,header=False)

address_data=pd.read_csv("civicnation_address_vote_wave1_clean.csv")
address_data.iloc[bad_results,:].to_csv("second_round.csv",header=True,index=False)