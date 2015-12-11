import csv
from bs4 import BeautifulSoup
from urllib import urlopen
r=urlopen("http://www.occ.gov/topics/licensing/interpretations-and-actions/index-interpretations-and-actions.html")
soup=BeautifulSoup(r,"html.parser")
list2=['1998 - 1996','2004 - 1999','2010 - 2005','2015 - 2011']
list1=[]
for i in soup.find_all('a'):
    if i.text in list2:
        list1.append(i.get('href'))
'''for i in list1:
    print i'''

for i in list1:
    if i=='/topics/licensing/interpretations-and-actions/interpretations-and-actions-1998-1996.html':
        r1=urlopen('http://www.occ.gov/topics/licensing/interpretations-and-actions/interpretations-and-actions-1998-1996.html')
        soup1=BeautifulSoup(r1,"html.parser")
        list98=[]
        list97=[]
        list96=[]
        for j in soup1.find_all('h3'):
            if j.text=='1998':
                for i in (soup1.findAll('p')[66]).find_all('a'):
                    list97.append(i.get('href'))
            if j.text=='1997':
                for i in (soup1.findAll('p')[67]).find_all('a'):
                    list97.append(i.get('href'))
            if j.text=='1996':
                for i in (soup1.findAll('p')[68]).find_all('a'):
                    list97.append(i.get('href'))
       
                 
import lxml.html
import urllib

#creating list for storing the scraped data
topic_list=[]
lno_list=[]
href_list=[]
cat_list=[]
i=1
for month in list97:
    connection = urllib.urlopen(month)
    dom =  lxml.html.fromstring(connection.read())
    '''
    page = lxml.html.tostring(dom,pretty_print=True,method="html")
    soup = BeautifulSoup(page,'html.parser')
    table = soup.findAll('table',{'class':'table_brdr'})
    try:
        for ta in table:
            print ta.findPrevious('p').findChild('strong').text
    except:
        print "skip"
                    
    
        
    
        
    try:
        soup = BeautifulSoup(page,'html.parser')
        record = []
        table = []
        td = ""
        table = soup.findAll('table',{'class':'table_brdr'})

        for ta in table:
            tableRecord =  ta.findAll('tr')
            category = ta.findPrevious('p').findChild('strong').text
            i = 0
            length = len(tableRecord)
            csvrecord = ""
            
            while i <  length-1 :
            
                tableRecordData = tableRecord[i].findChildren('td')
        
                for td in tableRecordData:
                    csvrecord=csvrecord#+','+td.getText()
                csvrecord_final = category+ csvrecord +'\r\n'
                i = i + 1
                print csvrecord_final
                csvrecord = ""
                csvrecord_final = ""
        
    except:
        pass'''
    cat=dom.xpath('//table/tr/td/p/strong/text()')
    print cat
    exp='//table/tr/td/a[contains(@href,".pdf")]/@href'
    ltr=dom.xpath('//table/tr/td/a[contains(@href,".pdf")]/text()')
    #ltr=dom.xpath('//table/tr/td')[1]
    
    ln=len(ltr)
    for i in range(ln):
        ltr[i]=ltr[i].replace('\r\n\t\t\t\t\t\t\t\t\t\t',"")
        ltr[i]=ltr[i].replace('\t',"")
        ltr[i]=ltr[i].replace(' ',"")
    topic=dom.xpath('//table[@class=string("table_brdr")]/tr/td/text()')
    if topic==[]:
        topic = dom.xpath('//table[@width]/tr/td/text()')       
    l= len(topic)  
    for i in range(l):
        topic[i] = topic[i].replace('\r\n', "")
        topic[i] = topic[i].replace('\t\t\t\t\t\t\t\t\t', "")
        topic[i] = topic[i].replace('\t\t\t\t\t', "")
        topic[i] = topic[i].replace('\t\t\t\t\t\t\t\t', "")
        topic[i] = topic[i].replace('\t\t\t\t\t\t\t\t            ', "")
        topic[i] = topic[i].replace('\t\t\t\t\t\t\t', "")
        topic[i] = topic[i].replace('\t\t', "")
        topic[i] = topic[i].replace('\t', "")
    while ''  in topic:
        topic.remove('')
    while ' '  in topic:
        topic.remove(' ')
    while '            '  in topic:
        topic.remove('            ')
        
    lnk=dom.xpath(exp)
    href_list.extend(lnk)
    topic_list.extend(topic)
    lno_list.extend(ltr)
    
    '''for i in lnk:
        print i'''
    '''for i in topic:
        print i'''
    '''for i in ltr:
        print i'''
    
    '''print len(ltr)
    print len(lnk)
    print len(topic)'''
    
#letter number
print len(lno_list)
print len(href_list)
print len(topic_list)
print "\n\n"
'''
#letter No
for i in lno_list:
    print i

#pdf link of letter number
for j in href_list:
    print j

#topic
for elem in topic_list:
    print elem
'''
'''
#creating a list of tuples to convert vertical into horizontal
whole_list = []

for i in range(len(topic_list)):
    [a for a in zip(topic_list[i], lno_list[i], href_list[i])]
    whole_list.append(a)
#writing to csv file   
with open("ou.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(whole_list)'''




    
    
    
        
    
    
    
