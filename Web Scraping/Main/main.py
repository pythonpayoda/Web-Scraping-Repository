import os
from Year import Range98_96
from Year import Range04_99
from Year import Range05_10
from Year import Range11_12
from Year import Merge
os.putenv('PYTHONPATH','C:\Documents and Settings\tsc10\Desktop\Web Scraping')


def main():
    url="http://www.occ.gov/topics/licensing/interpretations-and-actions/index-interpretations-and-actions.html"
    
    r1=Range98_96(url)
    r2=Range04_99(url)
    r3=Range05_10(url)
    r4=Range11_12(url)
    m=Merge()
    print "Fetching the url for range 1996-1998:"
    r1.fetchurl98_96()
    print "Fetching the url for range 1999-2004:"
    r2.fetchurl04_99()
    print "Fetching the url for range 2005-2010:"
    r3.fetchurl05_10()
    print "Fetching the url for range 2011-2012:"
    r4.fetchurl11_12()
    print "fetching data from 1996-1998"
    r1.fetchdata98_96()
    print "fetching data from 1999-2004"
    r2.fetchdata04_99()
    print "fetching data from 2005-2010"
    r3.fetchdata05_10()
    print "fetching data from 2011-2012"
    r4.fetchdata11_12()
    print "merging all the csv files"
    m.categories_find()
    m.find_files()
    

main()

