#importing the required packages
from bs4 import BeautifulSoup
import unicodedata
from urllib import urlopen
import lxml.html
import urllib
import csv
import re
import lxml.html
import urllib


class Range05_10:
    """This class writes data of range 2005 to 1010 to csv"""
    list05_10=[]
    topic_list=[]
    href_list=[]
    categoryfinal2=[]
    i=0
    num_of_letters=0
    year_ltr=[]
    year=[2010,2009,2008,2007,2006,2005]
    year_list=[]
    date_list=[]
    topic_list_sep=[]
    lno_list2=[]
    def __init__(self,url):
        self.url=url
    def fetchurl05_10(self):
        '''fetches the url '''
        #opening the url 
        r=urlopen(self.url)

        #assigning to the bs4 object
        soup=BeautifulSoup(r,"html.parser")

        #list created for saving the links of src link
        list2=['2010 - 2005']
        list1=[]
        for i in soup.find_all('a'):
            if i.text in list2:
                list1.append(i.get('href'))

        #Testing
        for i in list1:
            print i
 
        #Iterating  over the home page links   
        for i in list1:
            r1=urlopen('http://www.occ.gov/topics/licensing/interpretations-and-actions/interpretations-and-actions-2010-2005.html')
            soup1=BeautifulSoup(r1,"html.parser")
            
            for j in soup1.find_all('h3'):
                if j.text=='2010':
                    for i in (soup1.findAll('p')[66]).find_all('a'):
                        Range05_10.list05_10.append(i.get('href'))
                if j.text=='2009':
                    for i in (soup1.findAll('p')[67]).find_all('a'):
                        Range05_10.list05_10.append(i.get('href'))
                if j.text=='2008':
                    for i in (soup1.findAll('p')[68]).find_all('a'):
                        Range05_10.list05_10.append(i.get('href'))
                if j.text=='2007':
                    for i in (soup1.findAll('p')[69]).find_all('a'):
                        Range05_10.list05_10.append(i.get('href'))
                if j.text=='2006':
                    for i in (soup1.findAll('p')[70]).find_all('a'):
                        Range05_10.list05_10.append(i.get('href'))
                if j.text=='2005':
                    for i in (soup1.findAll('p')[71]).find_all('a'):
                        Range05_10.list05_10.append(i.get('href'))


    def fetchdata05_10(self):
        '''extract the data from the html page'''
        for month in Range05_10.list05_10: 
            connection = urllib.urlopen(month)
            dom =  lxml.html.fromstring(connection.read())
            page = lxml.html.tostring(dom,pretty_print=True,method="html")
            soup = BeautifulSoup(page,'html.parser')
            table=soup.findAll('table',{'class':'table_brdr'})
            for t in table:        
                for tr in t.findAll('tr'):
                    try:
                        #print tr.select('td')[1].text
                        topic=tr.select('td')[1].text
                        topic=topic.encode('utf-8')
                        for i in topic:
                            topic = topic.replace('\r\n', "")
                            topic=topic.replace('\t',"")
                            #ltr=ltr.replace('\n', "")
                            #topic_list.extend(topic)
                        Range05_10.topic_list.append(topic)
                      
                    except:
                        pass
           
                for tr in t.findAll('tr'):
                    try:
                        td=tr.select('td')[0]
                        a=td.find('a')
                
                        if a==None:
                            #print "none"
                            Range05_10.href_list.append("None")
                            #lno_list2.append(a.text)
                        else:
                            #print td.find('a')['href']
                            href=td.find('a')['href']
                            href=href.encode('utf-8')
                            for i in href:
                                href = href.replace('\r\n', "")
                                #ltr=ltr.replace('\n', "")
                            #href_list.append(href)
                            Range05_10.href_list.append(href)
                            lno=a.text
                            if '1084' in a.text:
                                a.text.remove(a.text)
                            Range05_10.lno_list2.append(a.text)
                            Range05_10.num_of_letters+=1
                            
                    except:
                        pass
            Range05_10.i+=1
            if Range05_10.i==12:
               Range05_10.i=0
               Range05_10.year_ltr.append(Range05_10.num_of_letters)
               Range05_10.num_of_letters=0
        #print Range05_10.year_ltr

        for i in Range05_10.list05_10:
            connection = urllib.urlopen(i)

            doc =  lxml.html.fromstring(connection.read())

            page = lxml.html.tostring(doc,pretty_print=True,method="html")

            soup = BeautifulSoup(page,'html.parser')
    
            tab=soup.find_all('table',{'class':'table_brdr'})
            c=len(tab)
            if tab!=[]:
                for i in tab:
                    if i.findPrevious('strong'):
                        #if i.findPrevious('p').findChild('strong'):
                        cat=i.findPrevious('strong').text
                        cat=cat.encode('utf-8')                
                        cat=cat.replace('\r\n\r\n','')
                        cat=cat.replace('\n','')
                        cat=cat.replace('\r\n\t\t\t\t\t\t\t\t\t\t','')
                        cat=cat.replace('\n\n\n','')
                        cat=cat.replace('\n\n\n\n','')
                        cat=cat.replace('\r\t\t\t\t\t\t\t\t\t\t','')
                        tableRecord =  i.findAll('tr')
                        i = 0
                        length = len(tableRecord)
                        csvrecord = ""
                        while i <  length-1 :
                            Range05_10.categoryfinal2.append(cat)
                            i = i + 1
                            csvrecord = ""
                            csvrecord_final = ""

                    else:
                        tab=soup.find_all('table',{'width':'100%'})
                        for i in tab:
                            if i.findPrevious('strong'):
                                if i.findPrevious('strong').text != 'Topics':
                                    #if i.findPrevious('p').findChild('strong'):
                                    cat=i.findPrevious('strong').text
                                    cat=cat.encode('utf-8')
                                    cat=cat.replace('\r\n\r\n','')
                                    cat=cat.replace('\n','')
                                    cat=cat.replace('\r\n\t\t\t\t\t\t\t\t\t\t','')
                                    cat=cat.replace('\n\n\n','')
                                    cat=cat.replace('\n\n\n\n','')
                                    cat=cat.replace('\r\t\t\t\t\t\t\t\t\t\t','')
                                    tableRecord =  i.findAll('tr')
                                    i = 0
                                    length = len(tableRecord)
                                    csvrecord = ""
                                    while i <  length-1 :
                                        Range05_10.categoryfinal2.append(cat)      
                                        i = i + 1
                                        csvrecord = ""
                                        csvrecord_final = ""
        k,j=0,0                       
        for i in Range05_10.year_ltr:
            
            while i>0:
                Range05_10.year_list.append(Range05_10.year[k])
                i-=1
            k+=1
        #print Range05_10.year_list
        print Range05_10.href_list
        '''print Range05_10.lno_list2'''
        for i in Range05_10.topic_list:
            try:
                import re
                length_data = len(i)
                #print "Length of data :",length_data

                datepat = re.compile(r'(\d+/\d+/\d+)')
                date = datepat.findall(i)
                #print date

                length_date = len(date[0])
                length_of_topic = length_data - length_date
                n=(length_data - length_date)-2
                #print "Length of topic :",length_of_topic
                topic = i[0:n]
                Range05_10.date_list.append(date[0])
                Range05_10.topic_list_sep.append(topic)
            except:
                pass

        print Range05_10.year_list
        print Range05_10.date_list
        with open("newoutnew.csv", "wb") as f:
            csv.writer(f,delimiter=',').writerows(zip(Range05_10.year_list,Range05_10.categoryfinal2,Range05_10.lno_list2,Range05_10.href_list,Range05_10.topic_list_sep,Range05_10.date_list))

        




    
    
