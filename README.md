# MultiSitemonitoring Latency Check :
1. This python script takes an input from site.xlsx for list of URL's to be monitored
2. Monitoring results are stored in results.csv file
3. Please match AppName in site.xlsx file with row headers in results.csv file
4. within multisitemon.py "writeresults" function contains title names of the sites to monitored for latency. Please change it as per your portal names
5. notify_user function is used to send an email to intended recipient incase connection to the site fails. This is for Administrators to be notified in case of outages
