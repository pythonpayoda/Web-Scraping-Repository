import csv
from bs4 import BeautifulSoup
from urllib import urlopen
import lxml.html
import urllib
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
    list98=[]
    for j in soup1.find_all('h3'):
        if j.text=='1998':
            for i in (soup1.findAll('p')[66]).find_all('a'):
                list98.append(i.get('href'))
        if j.text=='1997':
            for i in (soup1.findAll('p')[67]).find_all('a'):
                list98.append(i.get('href'))
        if j.text=='1996':
            for i in (soup1.findAll('p')[68]).find_all('a'):
                list98.append(i.get('href'))

topic_list=[]
lno_list=[]
href_list=[]
for month in list98: 
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
                lno_list.append(ltr)
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
                    #topic_list.extend(topic)
                topic_list.append(topic)
                    
            except:
                pass
   
        for tr in t.findAll('tr'):
            try:
                td=tr.select('td')[0]
                a=td.find('a')
                if a==None:
                    #print "none"
                    href_list.append("None")
                else:
                    #print td.find('a')['href']
                    href=td.find('a')['href']
                    href=href.encode('utf-8')
                    for i in href:
                        href = href.replace('\r\n', "")
                        #ltr=ltr.replace('\n', "")
                    #href_list.append(href)
                    href_list.append(href)
            except:
                pass

with open("newout.csv", "wb") as f:
    csv.writer(f,delimiter=',').writerows(zip(lno_list,href_list,topic_list))

            
'''print "letterno:"
print lno_list
print "topic"
print topic_list
print "href"
print href_list'''
print len(topic_list)
print len(href_list)
print len(lno_list)


'''for i in topic_list:
    print i
for j in href_list:
    print j
for k in lno_list:
    print k
    
 '''       
    
