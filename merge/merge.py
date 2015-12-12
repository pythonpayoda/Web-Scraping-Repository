import csv
import glob
import logging
#import sys
#import mylib
import logging
import datetime
import logging.config

def categories(topic_name):
    #create logger
    logger = logging.getLogger("categories")

    #create console handler and set level to DEBUG
    logging.basicConfig(filename='categories.log',level=logging.DEBUG,
            format='%(asctime)s.%(msecs)d %(levelname)s %(module)s - %(funcName)s: %(message)s')
    
    logging.info('groping the data')
    #logging.info(format)

    try:
        for row in categories.csv_f:
            if(row[0] == topic_name.strip()):
                air=csv.writer(categories.new_csv, delimiter=',')
                air.writerow(row)
   
    except:
        print "Sorry for the inconvience\nWe Will Rectify soon"

        #Exception will be stored in area_gender_pass
        logger.exception("Unexpected Error:")
                
                
        
def find_files():
    total_csv = []
    for files in glob.glob("*.csv"):
        total_csv.append(files)
    return total_csv

categories.new_csv = open('final.csv','wb',0)
total_csv = find_files()
total_csv.remove('final.csv')

for list_of_files in total_csv:
    f=open(list_of_files,'r')
    categories.csv_f = csv.reader(f)
    categories('Interpretive Letters')
   
for list_of_files in total_csv:
    f=open(list_of_files,'r')
    categories.csv_f = csv.reader(f)
    categories('Corporate Decisions')
    f.flush()
for list_of_files in total_csv:
    f=open(list_of_files,'r')
    categories.csv_f = csv.reader(f)
    categories('Approvals with conditions enforceable under 12 U.S.C. 1818')
    
for list_of_files in total_csv:
    f=open(list_of_files,'r')
    categories.csv_f = csv.reader(f)
    categories('CRA Decisions')
    
f.close()
          
if __name__ == '__categories__':
    categories()

