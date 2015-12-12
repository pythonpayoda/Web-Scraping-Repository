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

class Range3:
    list05_10=[]
    topic_list=[]
    lno_list=[]
    href_list=[]
    categoryfinal2=[]
    def fetch_url3(self):
        #opening the url 
        r=urlopen("http://www.occ.gov/topics/licensing/interpretations-and-actions/index-interpretations-and-actions.html")

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
                        Range3.list05_10.append(i.get('href'))
                if j.text=='2009':
                    for i in (soup1.findAll('p')[67]).find_all('a'):
                        Range3.list05_10.append(i.get('href'))
                if j.text=='2008':
                    for i in (soup1.findAll('p')[68]).find_all('a'):
                        Range3.list05_10.append(i.get('href'))
                if j.text=='2007':
                    for i in (soup1.findAll('p')[69]).find_all('a'):
                        Range3.list05_10.append(i.get('href'))
                if j.text=='2006':
                    for i in (soup1.findAll('p')[70]).find_all('a'):
                        Range3.list05_10.append(i.get('href'))
                if j.text=='2005':
                    for i in (soup1.findAll('p')[71]).find_all('a'):
                        Range3.list05_10.append(i.get('href'))


    def fetchdata_3(self):
        for month in Range3.list05_10: 
            connection = urllib.urlopen(month)
            dom =  lxml.html.fromstring(connection.read())
            page = lxml.html.tostring(dom,pretty_print=True,method="html")
            soup = BeautifulSoup(page,'html.parser')
            table=soup.findAll('table',{'class':'table_brdr'})
            for t in table:
                for tr in t.findAll('tr'):
                    try:
                        ltr=tr.select('td')[0].text
                        ltr=ltr.encode('utf-8')
                        for i in ltr:
                            ltr = ltr.replace('\r\n', "")
                            ltr=ltr.replace('\n', "")
                            ltr=ltr.replace('\t',"")
                        Range3.lno_list.append(ltr)
                    except:
                        pass
   
                for tr in t.findAll('tr'):
                    try:
                        topic=tr.select('td')[1].text
                        topic=topic.encode('utf-8')
                        for i in topic:
                            topic = topic.replace('\r\n', "")
                            topic=topic.replace('\t',"")
                            Range3.topic_list.append(topic)
                    
                    except:
                        pass
   
                for tr in t.findAll('tr'):
                    try:
                        td=tr.select('td')[0]
                        a=td.find('a')
                        if a==None:
                            Range3.href_list.append("None")
                        else:
                            href=td.find('a')['href']
                            href=href.encode('utf-8')
                        for i in href:
                            href = href.replace('\r\n', "")
                        Range3.href_list.append(href)
                    except:
                        pass

        for i in Range3.list05_10:
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
                            Range3.categoryfinal2.append(cat)
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
                                        Range3.categoryfinal2.append(cat)      
                                        i = i + 1
                                        csvrecord = ""
                                        csvrecord_final = ""

        with open("newout2.csv", "wb") as f:
            csv.writer(f,delimiter=',').writerows(zip(Range3.categoryfinal2,Range3.lno_list,Range3.href_list,Range3.topic_list))


            
