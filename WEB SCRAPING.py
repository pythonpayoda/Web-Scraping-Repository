#Traversal

#importing the required packages

from bs4 import BeautifulSoup
from urllib import urlopen
import lxml.html
import urllib

#opening the url 
r=urlopen("http://www.occ.gov/topics/licensing/interpretations-and-actions/index-interpretations-and-actions.html")

#assigning to the bs4 object
soup=BeautifulSoup(r,"html.parser")

#list created for saving the links of src link
list2=['1998 - 1996','2004 - 1999','2010 - 2005','2015 - 2011']
list1=[]
for i in soup.find_all('a'):
    if i.text in list2:
        list1.append(i.get('href'))

#Testing
for i in list1:
    print i
 
#Iterating  over the home page links   
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
                    list98.append(i.get('href'))
            if j.text=='1997':
                for i in (soup1.findAll('p')[67]).find_all('a'):
                    list97.append(i.get('href'))
            if j.text=='1996':
                for i in (soup1.findAll('p')[68]).find_all('a'):
                    list96.append(i.get('href'))
        print "Links of 1998"
        for i in list98:
            print i
        print "links of 1997"
        for i in list97:
            print i
        print "links of 1996"
        for i in list96:
            print i
    if i=='/topics/licensing/interpretations-and-actions/interpretations-and-actions-2004-1999.html':
        r1=urlopen('http://www.occ.gov/topics/licensing/interpretations-and-actions/interpretations-and-actions-2004-1999.html')
        soup1=BeautifulSoup(r1,"html.parser")
        list99=[]
        list00=[]
        list01=[]
        list02=[]
        list03=[]
        list04=[]
        for j in soup1.find_all('h3'):
            if j.text=='1999':
                for i in (soup1.findAll('p')[71]).find_all('a'):
                    list99.append(i.get('href'))
            if j.text=='2000':
                for i in (soup1.findAll('p')[70]).find_all('a'):
                    list00.append(i.get('href'))
            if j.text=='2001':
                for i in (soup1.findAll('p')[69]).find_all('a'):
                    list01.append(i.get('href'))
            if j.text=='2002':
                for i in (soup1.findAll('p')[68]).find_all('a'):
                    list02.append(i.get('href'))
            if j.text=='2003':
                for i in (soup1.findAll('p')[67]).find_all('a'):
                    list03.append(i.get('href'))
            if j.text=='2004':
                for i in (soup1.findAll('p')[66]).find_all('a'):
                    list04.append(i.get('href'))
                    
        print "Links of 1999"
        for i in list99:
            print i
        print "links of 2000"
        for i in list00:
            print i
        print "links of 2001"
        for i in list01:
            print i
        print "links of 2002"
        for i in list02:
            print i
        print "links of 2003"
        for i in list03:
            print i
        print "links of 2004"
        for i in list04:
            print i
            
    if i=='/topics/licensing/interpretations-and-actions/interpretations-and-actions-2010-2005.html':
        r1=urlopen('http://www.occ.gov/topics/licensing/interpretations-and-actions/interpretations-and-actions-2010-2005.html')
        soup1=BeautifulSoup(r1,"html.parser")
        list05=[]
        list06=[]
        list07=[]
        list08=[]
        list09=[]
        list10=[]
        for j in soup1.find_all('h3'):
            if j.text=='2010':
                for i in (soup1.findAll('p')[66]).find_all('a'):
                    list10.append(i.get('href'))
            if j.text=='2009':
                for i in (soup1.findAll('p')[67]).find_all('a'):
                    list09.append(i.get('href'))
            if j.text=='2008':
                for i in (soup1.findAll('p')[68]).find_all('a'):
                    list08.append(i.get('href'))
            if j.text=='2007':
                for i in (soup1.findAll('p')[69]).find_all('a'):
                    list07.append(i.get('href'))
            if j.text=='2006':
                for i in (soup1.findAll('p')[70]).find_all('a'):
                    list06.append(i.get('href'))
            if j.text=='2005':
                for i in (soup1.findAll('p')[71]).find_all('a'):
                    list05.append(i.get('href'))
                    
        print "Links of 2010"
        for i in list10:
            print i
        print "links of 2009"
        for i in list09:
            print i
        print "links of 2008"
        for i in list08:
            print i
        print "links of 2007"
        for i in list07:
            print i
        print "links of 2006"
        for i in list06:
            print i
        print "links of 2005"
        for i in list05:
            print i
    if i=='/topics/licensing/interpretations-and-actions/interpretations-and-actions-2011-2015.html':
        r1=urlopen('http://www.occ.gov/topics/licensing/interpretations-and-actions/interpretations-and-actions-2011-2015.html')
        soup1=BeautifulSoup(r1,"html.parser")
        list11=[]
        list12=[]
        for j in soup1.find_all('h3'):
            if j.text=='2012':
                for i in (soup1.findAll('p')[66]).find_all('a'):
                    list12.append(i.get('href'))
            if j.text=='2011':
                for i in (soup1.findAll('p')[67]).find_all('a'):
                    list11.append(i.get('href'))
                    
        print "Links of 2012"
        for i in list12:
            print i
        print "links of 2011"
        for i in list11:
            print i

#RETRIEVING DATA FROM TABLE
#creating list for storing the scraped data
topic_list=[]
lno_list=[]
href_list=[]
i=1
for month in list98:
    connection = urllib.urlopen(month)
    dom =  lxml.html.fromstring(connection.read())
    exp='//a[contains(@href,"pdf")]/@href'
    ltr=dom.xpath('//a[contains(@href,"pdf")]/text()')
    topic = dom.xpath('//table[@class=string("table_brdr")]/tr/td/text()')
    l= len(topic)
    for i in range(l):
        topic[i] = topic[i].replace('\r\n', "")
    while ''  in topic:
        topic.remove('')
    while ' '  in topic:
        topic.remove(' ')
    lnk=dom.xpath(exp)
    href_list.append(lnk)
    topic_list.append(topic)
    lno_list.append(ltr)

#creating a list of tuples to convert vertical into horizontal
whole_list = []
for i in range(len(topic_list)):
    [list(a) for a in zip(topic_list[i], lno_list[i], href_list[i])]
    whole_list.append(a)

#letter number
for i in lno_list:
    print i

#pdf link of letter number
for j in href_list:
    print j

#topic
for elem in topic_list:
    print elem
#writing to csv file   
with open("output.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(whole_list)
        
