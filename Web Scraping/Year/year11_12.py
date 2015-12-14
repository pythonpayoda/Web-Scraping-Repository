from urllib import urlopen
import lxml.html
import urllib
import csv
from bs4 import BeautifulSoup
class Range11_12:
    '''creating list for storing the scraped data'''
    topic_list=[]
    lno_list=[]
    href_list=[]
    list11_12=[]
    categoryfinal4=[]
    i=0
    num_of_letters=0
    year_ltr=[]
    year=[2012,2011]
    year_list=[]
    date_list=[]
    topic_list_sep=[]
    def __init__(self,url):
        self.url=url
    def fetchurl11_12(self):
        #opening the url 
        r=urlopen(self.url)

        #assigning to the bs4 object
        soup=BeautifulSoup(r,"html.parser")
    
        #list created for saving the links of src link
        list2=['2015 - 2011']
        list1=[]
        for i in soup.find_all('a'):
            if i.text in list2:
                list1.append(i.get('href'))

        #Testing
        for i in list1:
            print i
 
        #Iterating  over the home page links   
        for i in list1:
            if i=='/topics/licensing/interpretations-and-actions/interpretations-and-actions-2011-2015.html':
                r1=urlopen('http://www.occ.gov/topics/licensing/interpretations-and-actions/interpretations-and-actions-2011-2015.html')
                soup1=BeautifulSoup(r1,"html.parser")
                for j in soup1.find_all('h3'):
                    if j.text=='2012':
                        for i in (soup1.findAll('p')[69]).find_all('a'):
                            a="http://www.occ.gov"+i.get('href')
                            Range11_12.list11_12.append(a)
                    if j.text=='2011':
                        for i in (soup1.findAll('p')[70]).find_all('a'):
                            a="http://www.occ.gov"+i.get('href')
                            Range11_12.list11_12.append(a)
                
    def fetchdata11_12(self):
        '''fetches data from 2011 2012'''
        for i in Range11_12.list11_12:
            url=urlopen(i)
            soup1=BeautifulSoup(url,"html.parser")
            table=soup1.findAll('table',{'class':'table_brdr'})
            for i in table:
                tr=i.find_all('tr')
        
                for j in tr:
                    try:
                        ltr=j.select('td')[0].text
                        ltr=ltr.encode('utf-8')
                        for i in ltr:
                            ltr = ltr.replace('\r\n', "")
                            ltr=ltr.replace('\n', "")
                            ltr=ltr.replace('\t',"")
                        Range11_12.lno_list.append(ltr)
                        Range11_12.num_of_letters+=1
                    except:
                        pass
        
                for j in tr:
                    try:
                        topic=j.select('td')[1].text
                        topic=topic.encode('utf-8')
                        for i in topic:
                            topic = topic.replace('\r\n', "")
                            topic=topic.replace('\t',"")
                        Range11_12.topic_list.append(topic)
                
                
                    except:
                        pass
          
        
                for j in tr:
                    try:
                        ltr=j.select('td')[0]
                        a=ltr.find('a')['href']
                        a=a.encode('utf-8')
                        Range11_12.href_list.append(a)
            
                    except:
                        pass
            Range11_12.i+=1
            if Range11_12.i==12:
               Range11_12.i=0
               Range11_12.year_ltr.append(Range11_12.num_of_letters)
               Range11_12.num_of_letters=0
        #print Range11_12.year_ltr

        for i in Range11_12.list11_12:
            connection = urllib.urlopen(i)

            doc =  lxml.html.fromstring(connection.read())

            page = lxml.html.tostring(doc,pretty_print=True,method="html")

            soup = BeautifulSoup(page,'html.parser')
    
            tab=soup.find_all('table',{'class':'table_brdr'})
            c=len(tab)
            if tab!=[]:
                for i in tab:
                    if i.findPrevious('h3'):
                        #if i.findPrevious('p').findChild('strong'):
                        cat=i.findPrevious('h3').text
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
                            Range11_12.categoryfinal4.append(cat)
                            i = i + 1
                            csvrecord = ""
                            csvrecord_final = ""

            else:
                tab=soup.find_all('table',{'width':'100%'})
                for i in tab:
                    if i.findPrevious('h3'):
                        if i.findPrevious('h3').text != 'Topics':
                            #if i.findPrevious('p').findChild('strong'):
                            cat=i.findPrevious('h3').text
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
                                Range11_12.categoryfinal4.append(cat)
                                i = i + 1
                                csvrecord = ""
                                csvrecord_final = ""
        k,j=0,0                       
        for i in Range11_12.year_ltr:
            
            while i>0:
                Range11_12.year_list.append(Range11_12.year[k])
                i-=1
            k+=1
        #print Range11_12.year_list
        for i in Range11_12.topic_list:
            try:
                import re
                length_data = len(i)
                datepat = re.compile(r'(\d+/\d+/\d+)')
                date = datepat.findall(i)
                length_date = len(date[0])
                length_of_topic = length_data - length_date
                n=(length_data - length_date)-2
                topic = i[0:n]
                Range11_12.date_list.append(date[0])
                Range11_12.topic_list_sep.append(topic)
            except:
                pass

   
        #wrires to csv file
        with open("newout3.csv", "wb") as f:
            csv.writer(f,delimiter=',').writerows(zip(Range11_12.year_list,Range11_12.categoryfinal4,Range11_12.lno_list,Range11_12.href_list,Range11_12.topic_list_sep,Range11_12.date_list))
            
   

                       

