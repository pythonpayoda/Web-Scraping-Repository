from bs4 import BeautifulSoup
from urllib import urlopen
import lxml.html
import urllib
import csv
import unicodedata
import re

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
    list99_04=[]
    for j in soup1.find_all('h3'):
        if j.text=='1999':
            for i in (soup1.findAll('p')[71]).find_all('a'):
                list99_04.append(i.get('href'))
        if j.text=='2000':
            for i in (soup1.findAll('p')[70]).find_all('a'):
                list99_04.append(i.get('href'))
        if j.text=='2001':
            for i in (soup1.findAll('p')[69]).find_all('a'):
                list99_04.append(i.get('href'))
        if j.text=='2002':
            for i in (soup1.findAll('p')[68]).find_all('a'):
                list99_04.append(i.get('href'))
        if j.text=='2003':
            for i in (soup1.findAll('p')[67]).find_all('a'):
                list99_04.append(i.get('href'))
        if j.text=='2004':
            for i in (soup1.findAll('p')[66]).find_all('a'):
                list99_04.append(i.get('href'))

       
                 
import lxml.html
import urllib

#creating list for storing the scraped data
topic_list=[]
lno_list=[]
href_list=[]
cat_list=[]
for month in list99_04:
    connection = urllib.urlopen(month)
    dom =  lxml.html.fromstring(connection.read())
    
    page = lxml.html.tostring(dom,pretty_print=True,method="html")
    soup = BeautifulSoup(page,'html.parser')
    table = soup.findAll('table',{'class':'table_brdr'})
    #cat=dom.xpath('//table/tr/td/p/strong/text()')
    #print cat
    exp='//table/tr/td/a[contains(@href,".pdf")]/@href'
    ltr=dom.xpath('//table/tr/td/a[contains(@href,".pdf")]/text()')
    ln=len(ltr)
    for i in range(ln):
        ltr[i]=ltr[i].replace('\r\n\t\t\t\t\t\t\t\t\t\t',"")
        ltr[i]=ltr[i].replace('\t',"")
        ltr[i]=ltr[i].replace(' ',"")
        ltr[i]=ltr[i].replace('WORD',"")
        ltr[i]=ltr[i].replace('\r\n',"")
    while '' in ltr:
        ltr.remove('')
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
        topic[i] = topic[i].encode('utf-8')
    while ''  in topic:
        topic.remove('')
    while ' '  in topic:
        topic.remove(' ')
    while '            '  in topic:
        topic.remove('            ')
    l1= len(topic)  
    try:
        for i in range(l1):
            patern='([/][\d\w]+)+'
            obj=re.search(patern,topic[i])
            if obj:
                topic[i-1]=topic[i-1]+topic[i]
                topic.remove(topic[i])
    except:
        pass
    
        
    lnk=dom.xpath(exp)
    lnk=list(set(lnk))
    if lnk!=[]:
        href_list.extend(lnk)
    if topic!=[]:
        topic_list.extend(topic)
    if ltr!=[]:
        lno_list.extend(ltr)
    '''for i in ltr:
        print i
    for h in lnk:
        print h
    for t in topic:
        print t'''
with open("list9904.csv", "wb") as f:
    csv.writer(f,delimiter=',').writerows(zip(lno_list,href_list,topic_list))

    
#letter number
print len(lno_list)
print len(href_list)
print len(topic_list)
print "\n\n"

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
#creating a list of tuples to convert vertical into horizontal
whole_list = []

for i in range(len(topic_list)):
    [a for a in zip(topic_list[i], lno_list[i], href_list[i])]
    whole_list.append(a)
#writing to csv file   
with open("out04.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(whole_list)

'''


    
    
    
        
    
    
    
