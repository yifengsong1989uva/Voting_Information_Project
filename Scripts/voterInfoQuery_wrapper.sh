#!/bin/bash

#cd '/home/composersyf/Documents/Google Civic Information API/Scripts'
cd /home/ec2-user/mydata

echo ""
echo "Step 2: Querying the Google Civic API..."

start=`date +%s`

cat cleaned_addresses.txt | parallel --jobs $1 "./voterInfoQuery_new.sh" > ../output/final_result_mail_round2.json
#cat ../First_Batch/cleaned_addresses.txt | parallel --jobs $1 "./voterInfoQuery_new.sh" > ../First_Batch/final_result_batch1_late.json
#cat ../Second_Batch/cleaned_addresses.txt | parallel --jobs $1 "./voterInfoQuery_new.sh" > ../Second_Batch/final_result_batch2_text.json
end=`date +%s`

runtime=$((end-start))
echo "Number of parallel jobs: $1; Runtime: $runtime s."

cd ~
