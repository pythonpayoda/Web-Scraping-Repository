#Traversal

#importing the required packages

from bs4 import BeautifulSoup
from urllib import urlopen
import lxml.html
import urllib
import csv

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



