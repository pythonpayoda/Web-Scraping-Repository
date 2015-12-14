import csv
import glob
import logging
#import sys
#import mylib
import logging
import datetime
import logging.config
class Merge:
    total_csv = []
    new_csv=0
    def __init__(self):
        self.new_csv = open('final.csv','wb',0)
        self.csv_f='NULL'


    def categories_find(self,topic_name):
        """This function writes the csv file according to the category"""
        #create logger
        logger = logging.getLogger("category")
        

        logger.info('Started Grouping Data')
        logger.info('Finished Grouping Data')
        
        #logging.info(format)

        try: 
            for row in self.csv_f:
                if(row[1] == topic_name.strip()):
                
                    air=csv.writer(self.new_csv, delimiter=',')
                    air.writerow(row)
        except:
            
        
            print "Sorry for the inconvience"

            #Exception will be stored in find_files.log
            logger.exception("Unexpected Error:")
                    
                    
            
    def find_files(self):
        """This function displays all the csv files """

        
        #create logger
        logger = logging.getLogger("find_files")

        #create console handler and set level to DEBUG
        logging.basicConfig(filename='find_files.log',level=logging.DEBUG,
                format='%(asctime)s.%(msecs)d %(levelname)s %(module)s - %(funcName)s: %(lineno)s %(message)s')
        
        logging.info('Started collecting all CSV Files')
        logging.info('Finished collecting all CSV Files')
        
       
                   
        try:
            for files in glob.glob("*.csv"):
                Merge.total_csv.append(files)
                
            return Merge.total_csv
        except:
            print "Sorry for the inconvience"

            #Exception will be stored in find_files.log 
            logger.exception("Unexpected file Error:")


        
            
    def call(self):                
        
        #main outputfile for grouping csv files 
       
        Merge.total_csv = self.find_files()
        
        
        #category list forInterpretive Letters
        for list_of_files in Merge.total_csv:
            f=open(list_of_files,'r')
            self.csv_f = csv.reader(f)
            self.categories_find('Interpretive Letters')
         
        #category list for Corporate Decisions  
        for list_of_files in Merge.total_csv:
            f=open(list_of_files,'r')
            self.csv_f = csv.reader(f)
            self.categories_find('Corporate Decisions')
           
        #category list for Approvals with conditions enforceable under 12 U.S.C. 1818    
        for list_of_files in Merge.total_csv:
            f=open(list_of_files,'r')
            self.csv_f = csv.reader(f)
            self.categories_find('Approvals with conditions enforceable under 12 U.S.C. 1818')
            
        #category list for CRA Decisions    
        for list_of_files in Merge.total_csv:
            f=open(list_of_files,'r')
            self.csv_f = csv.reader(f)
            self.categories_find('CRA Decisions')
        for list_of_files in Merge.total_csv:
            f=open(list_of_files,'r')
            self.csv_f = csv.reader(f)
            self.categories_find('No-Objection Letters')
        for list_of_files in Merge.total_csv:
            f=open(list_of_files,'r')
            self.csv_f = csv.reader(f)
            self.categories_find('Community Development Investment Letters')
        			       
        #close file
        
        f.close()





