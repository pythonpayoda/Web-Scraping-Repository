import csv
from bs4 import BeautifulSoup
from urllib import urlopen
import lxml.html
import urllib
class Range04_99:
    list99_04=[]
    categoryfinal1=[]
    topic_list=[]
    lno_list=[]
    href_list=[]
    i=0
    num_of_letters=0
    year_ltr=[]
    year=[2004,2003,2002,2001,2000,1999]
    year_list=[]
    date_list=[]
    topic_list_sep=[]
    def __init__(self,url):
        self.url=url
    def fetchurl04_99(self):
        """This method fetches the URL of all the months from 1996 to 1998"""
        #opening the url 
        r=urlopen(self.url)

        #assigning to the bs4 object
        soup=BeautifulSoup(r,"html.parser")

        #list created for saving the links of src link
        list2=['2004 - 1999']
        list1=[]
        for i in soup.find_all('a'):
            if i.text in list2:
                list1.append(i.get('href'))

        #Testing
        for i in list1:
            print i
        for i in list1:
            r1=urlopen('http://www.occ.gov/topics/licensing/interpretations-and-actions/interpretations-and-actions-2004-1999.html')
            soup1=BeautifulSoup(r1,"html.parser")
            
            for j in soup1.find_all('h3'):
                if j.text=='1999':
                    for i in (soup1.findAll('p')[71]).find_all('a'):
                        Range04_99.list99_04.append(i.get('href'))
                if j.text=='2000':
                    for i in (soup1.findAll('p')[70]).find_all('a'):
                        Range04_99.list99_04.append(i.get('href'))
                if j.text=='2001':
                    for i in (soup1.findAll('p')[69]).find_all('a'):
                        Range04_99.list99_04.append(i.get('href'))
                if j.text=='2002':
                    for i in (soup1.findAll('p')[68]).find_all('a'):
                        Range04_99.list99_04.append(i.get('href'))
                if j.text=='2003':
                    for i in (soup1.findAll('p')[67]).find_all('a'):
                        Range04_99.list99_04.append(i.get('href'))
                if j.text=='2004':
                    for i in (soup1.findAll('p')[66]).find_all('a'):
                        Range04_99.list99_04.append(i.get('href'))

    def fetchdata04_99(self):
        """This method fetches the data from each month"""
        
        for month in Range04_99.list99_04: 
            connection = urllib.urlopen(month)
            dom =  lxml.html.fromstring(connection.read())
            page = lxml.html.tostring(dom,pretty_print=True,method="html")
            soup = BeautifulSoup(page,'html.parser')
            table=soup.findAll('table',{'class':'table_brdr'})
            #Iterating through the table
            for t in table:
                #getting the letter numbers
                for tr in t.findAll('tr'):
                    try:
                        #print tr.select('td')[0].text
                        ltr=tr.select('td')[0].text
                        ltr=ltr.encode('utf-8')
                        for i in ltr:
                            ltr = ltr.replace('\r\n', "")
                            ltr=ltr.replace('\n', "")
                            ltr=ltr.replace('\t',"")
                            if 'WORD' in ltr:
                                ltr.remove(ltr)
                            if '617' in ltr:
                                ltr.remove(ltr)
                        Range04_99.lno_list.append(ltr)
                        Range04_99.num_of_letters+=1
                    except:
                        pass
                #getting the topics
                for tr in t.findAll('tr'):
                    try:
                        #print tr.select('td')[1].text
                        topic=tr.select('td')[1].text
                        topic=topic.encode('utf-8')
                        for i in topic:
                            topic = topic.replace('\r\n', "")
                            topic=topic.replace('\t',"")
                            #ltr=ltr.replace('\n', "")
                            #Range04_99.topic_list.extend(topic)
                        Range04_99.topic_list.append(topic)
                    
                    except:
                        pass
                #getting the letter number links
                for tr in t.findAll('tr'):
                    try:
                        td=tr.select('td')[0]
                        a=td.find('a')
                        if a==None:
                            #print "none"
                           Range04_99. href_list.append("None")
                        else:
                            #print td.find('a')['href']
                            href=td.find('a')['href']
                            href=href.encode('utf-8')
                            for i in href:
                                href = href.replace('\r\n', "")
                                #ltr=ltr.replace('\n', "")
                                #href_list.append(href)
                            Range04_99. href_list.append(href)
                    except:
                        pass
            Range04_99.i+=1
            if Range04_99.i==12:
               Range04_99.i=0
               Range04_99.year_ltr.append(Range04_99.num_of_letters)
               Range04_99.num_of_letters=0
        #print Range04_99.year_ltr

        #getting the categories
        for i in Range04_99.list99_04:
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
                            Range04_99.categoryfinal1.append(cat)
                            #print cat
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
                                Range04_99.categoryfinal1.append(cat)
                                #print cat
                                i = i + 1
                        
                                csvrecord = ""
                                csvrecord_final = ""
        
        k,j=0,0                       
        for i in Range04_99.year_ltr:
            
            while i>0:
                Range04_99.year_list.append(Range04_99.year[k])
                i-=1
            k+=1
        #print Range04_99.year_list
        for i in Range04_99.topic_list:
            try:
                import re
                length_data = len(i)
                datepat = re.compile(r'(\d+/\d+/\d+)')
                date = datepat.findall(i)
                length_date = len(date[0])
                length_of_topic = length_data - length_date
                n=(length_data - length_date)-2
                topic = i[0:n]
                Range04_99.date_list.append(date[0])
                Range04_99.topic_list_sep.append(topic)
            except:
                pass
             

        #writing to a csv file
        with open("newout1.csv", "wb") as f:
            csv.writer(f,delimiter=',').writerows(zip(Range04_99.year_list,Range04_99.categoryfinal1,Range04_99.lno_list,Range04_99.href_list,Range04_99.topic_list_sep,Range04_99.date_list))


            

    
