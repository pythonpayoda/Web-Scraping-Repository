

#importing the required packages

from bs4 import BeautifulSoup
from urllib import urlopen
import lxml.html
import urllib
import csv
class Range1:
    #creating list for storing the scraped data
    list98_96=[]
    topic_list=[]
    lno_list=[]
    href_list=[]
    categoryfinal=[]
    def fetch_url1(self):
        #opening the url 
        r=urlopen("http://www.occ.gov/topics/licensing/interpretations-and-actions/index-interpretations-and-actions.html")

        #assigning to the bs4 object
        soup=BeautifulSoup(r,"html.parser")

        #list created for saving the links of src link
        list2=['1998 - 1996']
        list1=[]
        for i in soup.find_all('a'):
            if i.text in list2:
                list1.append(i.get('href'))

        #Testing
        for i in list1:
            print i

        #Iterating  over the home page links   
        for i in list1:
            r1=urlopen('http://www.occ.gov/topics/licensing/interpretations-and-actions/interpretations-and-actions-1998-1996.html')
            soup1=BeautifulSoup(r1,"html.parser")
    
        for j in soup1.find_all('h3'):
            if j.text=='1998':
                for i in (soup1.findAll('p')[66]).find_all('a'):
                    Range1.list98_96.append(i.get('href'))
            if j.text=='1997':
                for i in (soup1.findAll('p')[67]).find_all('a'):
                    Range1.list98_96.append(i.get('href'))
            if j.text=='1996':
                for i in (soup1.findAll('p')[68]).find_all('a'):
                    Range1.list98_96.append(i.get('href'))

    def fetchdata_1(self):
        for month in Range1.list98_96: 
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
                        Range1.lno_list.append(ltr)
                    except:
                        pass
   
                for tr in t.findAll('tr'):
                    try:
                        topic=tr.select('td')[1].text
                        topic=topic.encode('utf-8')
                        for i in topic:
                            topic = topic.replace('\r\n', "")
                            topic=topic.replace('\t',"")
                        Range1.topic_list.append(topic)
                    
                    except:
                        pass
   
                for tr in t.findAll('tr'):
                    try:
                        td=tr.select('td')[0]
                        a=td.find('a')
                        if a==None:
                            Range1.href_list.append("None")
                        else:
                            href=td.find('a')['href']
                            href=href.encode('utf-8')
                            for i in href:
                                href = href.replace('\r\n', "")
                            Range1.href_list.append(href)
                    except:
                        pass

        for i in Range1.list98_96:
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
                            Range1.categoryfinal.append(cat)
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
                                Range1.categoryfinal.append(cat)
                                i = i + 1
                        
                                csvrecord = ""
                                csvrecord_final = ""

        with open("newout.csv", "wb") as f:
            csv.writer(f,delimiter=',').writerows(zip(Range1.categoryfinal,Range1.lno_list,Range1.href_list,Range1.topic_list))
    









