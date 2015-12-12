from urllib import urlopen
import lxml.html
import urllib
import csv
from bs4 import BeautifulSoup
class Range4:
    #creating list for storing the scraped data
    topic_list=[]
    lno_list=[]
    href_list=[]
    list11_12=[]
    def fetch_url4:
        #opening the url 
        r=urlopen("http://www.occ.gov/topics/licensing/interpretations-and-actions/index-interpretations-and-actions.html")

        #assigning to the bs4 object
        soup=BeautifulSoup(r,"html.parser")
    
        #list created for saving the links of src link
        list2=['2015 - 2011','2010 - 2005','2004 - 1999','1998 - 1996']
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
                            list12.append(a)
                    if j.text=='2011':
                        for i in (soup1.findAll('p')[70]).find_all('a'):
                            a="http://www.occ.gov"+i.get('href')
                            list12.append(a)
                for i in list12:
                    print i
   
    for i in list12:
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
                lno_list.append(ltr)
            except:
                pass
        
        for j in tr:
            try:
                #print tr.select('td')[1].text
                topic=j.select('td')[1].text
                topic=topic.encode('utf-8')
                #print topic
                for i in topic:
                    topic = topic.replace('\r\n', "")
                    topic=topic.replace('\t',"")
                    #ltr=ltr.replace('\n', "")
                    #topic_list.extend(topic)
                topic_list.append(topic)
                
                
            except:
                pass
        
        for j in tr:
            try:
                ltr=j.select('td')[0]
                a=ltr.find('a')['href']
                a=a.encode('utf-8')
                href_list.append(a)
            
                
            except:
                pass
categoryfinal4=[]
for i in list12:
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
                #for j in cat:
                    #cat=cat.replace('\r\n\t','')
                
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
                    categoryfinal4.append(cat)
                    #print cat
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
                        categoryfinal4.append(cat)
                        #print cat
                        i = i + 1
                        
                        csvrecord = ""
                        csvrecord_final = ""
#for i in categoryfinal:
    #i=i.replace('\r\n\r\n','')
    #print i
print categoryfinal4
   

with open("newout3.csv", "wb") as f:
    csv.writer(f,delimiter=',').writerows(zip(categoryfinal4,lno_list,href_list,topic_list))
            
   
            

