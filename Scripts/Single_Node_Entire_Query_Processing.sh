#!/bin/bash

#cd '/home/composersyf/Documents/Google Civic Information API/Scripts'
cd /home/ec2-user/mydata #change the current working directory to where this Bash script is stored

#load the voter addresses .csv file into Python, and change the addresses to the format which is suitable for querying the Google Civic API using cURL program in Linux Shell (Bash) scripting
filename_1="$1"
echo "Step 1: Loading voter addresses data..."
#python Address_Data_Cleaning.py $filename_1 > "../Second_Batch/cleaned_addresses.txt"
python Address_Data_Cleaning.py $filename_1 > cleaned_addresses.txt
echo "Step 1 completed!"

./voterInfoQuery_wrapper.sh 6
echo "Step 2 completed!" 

#run the Python program to parse the .json file and then save the polling location results into a .csv file
#python Extract_Polling_Locations.py "10_test_addresses.csv" "final_result.json"
#echo ""
#echo "##################################################"
#echo "Step 3: Saving the polling location results to file..."
#echo "Step 3 finished: Results have been saved to polling_location.csv!!!"

#rm "cleaned_addresses.txt"
