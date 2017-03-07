#!/bin/bash

#cd '/home/composersyf/Documents/Google Civic Information API/Scripts'
#cd 'Documents/Google Civic Information API' #change the current working directory to where this Bash script is stored

#query the Google Civic API using the provided voter addresses, one by one; the results are aggregated and saved as a .json file
#PART2="&electionId=5000&fields=pollingLocations"
PART2="&electionId=5000"

address="$1"
ADD1=`echo $address | cut -d \, -f 1`
ADD2=`echo $address | cut -d \, -f 2`
API_KEY=`echo $address | cut -d \, -f 3`

PART1="https://www.googleapis.com/civicinfo/v2/voterinfo?key=$API_KEY&address="

query_url="$PART1$ADD1$PART2"
query_result=`curl -s $query_url`
echo "{\"$ADD2\":[$query_result]},"
