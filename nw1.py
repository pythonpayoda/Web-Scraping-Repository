import csv
from bs4 import BeautifulSoup
from urllib import urlopen
import lxml.html
import urllib
class Range2:
    list99_04=[]
    categoryfinal1=[]
    topic_list=[]
    lno_list=[]
    href_list=[]
    def fetch_url2(self):
    
        #opening the url 
        r=urlopen("http://www.occ.gov/topics/licensing/interpretations-and-actions/index-interpretations-and-actions.html")

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
                    Range2.list99_04.append(i.get('href'))
            if j.text=='2000':
                for i in (soup1.findAll('p')[70]).find_all('a'):
                    Range2.list99_04.append(i.get('href'))
            if j.text=='2001':
                for i in (soup1.findAll('p')[69]).find_all('a'):
                    Range2.list99_04.append(i.get('href'))
            if j.text=='2002':
                for i in (soup1.findAll('p')[68]).find_all('a'):
                    Range2.list99_04.append(i.get('href'))
            if j.text=='2003':
                for i in (soup1.findAll('p')[67]).find_all('a'):
                    Range2.list99_04.append(i.get('href'))
            if j.text=='2004':
                for i in (soup1.findAll('p')[66]).find_all('a'):
                    Range2.list99_04.append(i.get('href'))
    def fetchdata_2(self):

        
        for month in Range2.list99_04: 
            connection = urllib.urlopen(month)
            dom =  lxml.html.fromstring(connection.read())
            page = lxml.html.tostring(dom,pretty_print=True,method="html")
            soup = BeautifulSoup(page,'html.parser')
            table=soup.findAll('table',{'class':'table_brdr'})
            for t in table:
    
                for tr in t.findAll('tr'):
                    try:
                        #print tr.select('td')[0].text
                        ltr=tr.select('td')[0].text
                        ltr=ltr.encode('utf-8')
                        for i in ltr:
                            ltr = ltr.replace('\r\n', "")
                            ltr=ltr.replace('\n', "")
                            ltr=ltr.replace('\t',"")
                        Range2.lno_list.append(ltr)
                    except:
                        pass
   
                for tr in t.findAll('tr'):
                    try:
                        #print tr.select('td')[1].text
                        topic=tr.select('td')[1].text
                        topic=topic.encode('utf-8')
                        for i in topic:
                            topic = topic.replace('\r\n', "")
                            topic=topic.replace('\t',"")
                            #ltr=ltr.replace('\n', "")
                            #Range2.topic_list.extend(topic)
                        Range2.topic_list.append(topic)
                    
                    except:
                        pass
   
                for tr in t.findAll('tr'):
                    try:
                        td=tr.select('td')[0]
                        a=td.find('a')
                        if a==None:
                            #print "none"
                           Range2. href_list.append("None")
                        else:
                            #print td.find('a')['href']
                            href=td.find('a')['href']
                            href=href.encode('utf-8')
                            for i in href:
                                href = href.replace('\r\n', "")
                                #ltr=ltr.replace('\n', "")
                                #href_list.append(href)
                            Range2. href_list.append(href)
                    except:
                        pass
        
        for i in Range2.list99_04:
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
                            Range2.categoryfinal1.append(cat)
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
                                Range2.categoryfinal1.append(cat)
                                #print cat
                                i = i + 1
                        
                                csvrecord = ""
                                csvrecord_final = ""



        with open("newout1.csv", "wb") as f:
            csv.writer(f,delimiter=',').writerows(zip(Range2.categoryfinal1,Range2.lno_list,Range2.href_list,Range2.topic_list))


            

    
