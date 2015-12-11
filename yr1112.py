from urllib import urlopen
import lxml.html
import urllib
import csv

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
    r1=urlopen('http://www.occ.gov/topics/licensing/interpretations-and-actions/interpretations-and-actions-2011-2015.html')
    soup1=BeautifulSoup(r1,"html.parser")
    list12=[]
    for j in soup1.find_all('h3'):
        if j.text=='2012':
            for i in (soup1.findAll('p')[66]).find_all('a'):
                list12.append(i.get('href'))
        if j.text=='2011':
            for i in (soup1.findAll('p')[67]).find_all('a'):
                list12.append(i.get('href'))
       
