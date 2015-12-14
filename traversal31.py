from bs4 import BeautifulSoup
import urllib
import lxml.html
from yr9698 import list98
count=0
for i in range(len(list98)):
    count+=1
    print count
    try:
        connection = urllib.urlopen(list98[i])
        doc =  lxml.html.fromstring(connection.read())
        page = lxml.html.tostring(doc,pretty_print=True,method="html")
        soup = BeautifulSoup(page,'html.parser')
        record = []
        table = []
        td = ""
        table = soup.findAll('table',{'class':'table_brdr'})
        for ta in table:
            print "=========================================="
            tableRecord =  ta.findAll('tr')
            category = ta.findPrevious('p').findChild('strong').text
            i = 0
            length = len(tableRecord)
            csvrecord = ""
            while i <  length-1 :
                tableRecordData = tableRecord[i].findChildren('td')
                for td in tableRecordData:
                    csvrecord = csvrecord
                csvrecord_final = category + csvrecord +'\r\n'
                i = i + 1
                print csvrecord_final
                csvrecord = ""
                csvrecord_final = ""
    except:
        print "wrong"

