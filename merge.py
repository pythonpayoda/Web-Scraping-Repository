import csv
import glob

def categories(topic_name):
	"""This function writes the csv file according to the category"""
    for row in categories.csv_f:
            if(row[0] == topic_name):
                a= csv.writer(categories.new_csv, delimiter=',')
                a.writerow(row)
        
def find_files():
	""" This function displays all the csv files """

    total_csv = []
    for files in glob.glob("*.csv"):
        total_csv.append(files)
    return total_csv

#outputfile for grouping csv files 

categories.new_csv = open('final.csv','wb')
total_csv = find_files()
total_csv.remove('final.csv')

#category list forInterpretive Letters

for list_of_files in total_csv:
    f=open(list_of_files,'r')
    categories.csv_f = csv.reader(f)
    categories('Interpretive Letters')

#category list for Corporate Decisions

for list_of_files in total_csv:
    f=open(list_of_files,'r')
    categories.csv_f = csv.reader(f)
    categories('Corporate Decisions')

#category list for Approvals with conditions enforceable under 12 U.S.C. 1818
for list_of_files in total_csv:
    f=open(list_of_files,'r')
    categories.csv_f = csv.reader(f)
    categories('Approvals with conditions enforceable under 12 U.S.C. 1818')
    
    
f.close()
        
        
