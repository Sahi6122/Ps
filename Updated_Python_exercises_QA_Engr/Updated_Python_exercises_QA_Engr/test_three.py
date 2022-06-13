
from datetime import datetime
from pytz import timezone
import csv


def parse_files(file_name):
    '''
    This function opens the csv file
    and finds values which are not equal to 200
    for the response code col and process 
    the time into pst
    '''
    print('\n reading file:', file_name)
    with open(file_name, newline='') as csvfile:

        next(csvfile) # skiiping first file
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')

        for row in spamreader:
            if int(row[3]) != 200:
                date_format='%m/%d/%Y %H:%M:%S %Z'
                d = int(row[0])/1000.0
                date = datetime.fromtimestamp(d)
                date = date.astimezone(timezone('US/Pacific')) # time zone converted to PST
                row[0] = date.strftime(date_format)

                print("filename: ",file_name, ",label:", row[2], ",response code:", row[3], ",response message:", row[4], ",failure message:", row[8], ",timezone:", row[0])


files = ['Jmeter_log1.jtl', 'Jmeter_log2.jtl']
for file in files:
    parse_files(file)
    