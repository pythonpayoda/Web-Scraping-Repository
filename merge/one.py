import csv
import glob

def categories(topic_name):
    for row in categories.csv_f:
            if(row[0] == topic_name):
                a= csv.writer(categories.new_csv, delimiter=',')
                a.writerow(row)
        
def find_files():
    total_csv = []
    for files in glob.glob("*.csv"):
        total_csv.append(files)
    return total_csv

categories.new_csv = open('final.csv','wb')
total_csv = find_files()
print total_csv
total_csv.remove('final.csv')
for list_of_files in total_csv:
    f=open(list_of_files,'r')
    categories.csv_f = csv.reader(f)
    categories('Corporate Decisions')


    
    
f.close()
        
        
