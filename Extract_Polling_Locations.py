# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 23:25:02 2016

@author: composersyf
"""

import sys
import os
import json
import numpy as np
import pandas as pd

os.chdir("/home/composersyf/Documents/Google Civic Information API")

def load_json():
    with open(sys.argv[2]) as final_result_raw:
        mydata=final_result_raw.readlines()
        mydata_cleaned=""
        for line in mydata:
            mydata_cleaned+=line
        return json.loads(mydata_cleaned)

def to_DataFrame(df):
    location_array=[]
    for d in df:
        location_array.extend([list(d.keys())[0],list(d.values())[0]['pollingLocations'][0]])
    location_array=np.array(location_array)
    location_array=location_array.reshape(len(df),2)
    location_df=pd.DataFrame(location_array)
    location_df.columns=["id","polling_location"]
    return location_df

def main():
    data_cleaned=load_json()
    locations=to_DataFrame(data_cleaned)
    voter_addresses=pd.read_csv(sys.argv[1],header=None)
    voter_addresses.columns=["voter_address"]
    voter_addresses['id']=list(range(1,voter_addresses.shape[0]+1))
    voter_addresses['id']=voter_addresses['id'].astype(str)
    final_df=voter_addresses.merge(locations,on=["id"],how="inner")
    final_df=final_df.loc[:,["voter_address","polling_location"]]
    final_df.to_csv("polling_locations.csv",index=False)   
        
if __name__=="__main__":
    main()
    
