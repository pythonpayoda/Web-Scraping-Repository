from bs4 import BeautifulSoup
import urllib
import lxml.html
categoryfinal=[]
from yr9698 import list98


for i in list98:
    connection = urllib.urlopen(i)


    doc =  lxml.html.fromstring(connection.read())

    page = lxml.html.tostring(doc,pretty_print=True,method="html")



    soup = BeautifulSoup(page,'html.parser')
    
    tab=soup.find_all('table',{'class':'table_brdr'})
    print len(tab)
    if tab!=[]:
        for i in tab:
            if i.findPrevious('strong'):
                #if i.findPrevious('p').findChild('strong'):
                cat=i.findPrevious('strong').text
                tableRecord =  i.findAll('tr')
                i = 0
                length = len(tableRecord)
                csvrecord = ""
                while i <  length-1 :
                    #categoryfinal.append[cat]
                    print cat
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
                    tableRecord =  i.findAll('tr')
                    i = 0
                    length = len(tableRecord)
                    csvrecord = ""
                    while i <  length-1 :
                        #categoryfinal.append[cat]
                        print cat
                        i = i + 1
                        
                        csvrecord = ""
                        csvrecord_final = ""
for i in categoryfinal:
    print i
        
    #print tab[0].findPrevious('p').findChild('strong').text
    #print tab[1].findPrevious('p').findChild('strong').text
    #print tab[2].findPrevious('p').findChild('strong').text
    '''
    l=len(tab)
    j=1
    for i in tab:
        tab[i]
        cat=tab[i].findPrevious('p').findChild('strong').text
        print cat
     '''  
  
