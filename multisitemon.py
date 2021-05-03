import pandas as pd
import requests
import time
import smtplib
from csv import DictWriter

# Email Address and Password for notify_user function, whenever the site is down
EMAIL_ADDRESS = 'myemailid@gmail.com'
EMAIL_PASSWORD = 'mypassword'

# Time to be published in csv results file to know when the website was tested
timemachine = time. strftime('%d-%m-%Y %H:%M:%S')

# List to gather results of response time for individual sites
responsetime=[]

# Function to write the results collected in list, to results.csv file for respective time stamp
def writeresults(responsetimevalueslist):
    field_names = ['SomeRandomSite', 'IT_HelpDesk_Portal', 'Conf_Booking_Portal','DateTime']
    dict = {'SomeRandomSite':responsetimevalueslist[0],'IT_HelpDesk_Portal':responsetimevalueslist[1],
            'Conf_Booking_Portal':responsetimevalueslist[2],'DateTime': timemachine}
    with open('results.csv','a', newline='\n') as f_object:
        dictwriter_object = DictWriter(f_object,fieldnames=field_names)
        dictwriter_object.writerow(dict)
        f_object.close()

# Function to send an email to defined email address in case of connectivity issues
def notify_user(mysite):
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

            subject = f' {mysite} Portal IS DOWN!'
            body = f'Please troubleshoot to get the services for {mysite} Portal up and running'
            msg = f'Subject: {subject}\n\n{body}'

            # logging.info('Sending Email...')
            smtp.sendmail(EMAIL_ADDRESS, 'sendfailurreport@gmail.com', msg)

# Pandas dataframe to read the spreadsheet for configured URLs for connection check
# Iterate through the sites.xlsx file to iteratively request url and collect the response time in responsetimelist
# If connection fails, it will send a notification to designated emails through notify_user function
sites = pd.read_excel(r'sites.xlsx') #sheet_name='sites',header='URL')
for i, site in sites.iterrows():
      #print(i, site['URL'], site['App Name'])
      siteName = site['AppName']
      try:
            r = requests.get(site['URL'], timeout=5)
            str1 = str(r.elapsed.total_seconds())
            responsetime.append(str1)
      except Exception as e:
             notify_user(siteName)
             responsetime.append("ConnectionFailed")

# Function call to write results to results.csv, based on results collected in responsetime list
writeresults(responsetime)
