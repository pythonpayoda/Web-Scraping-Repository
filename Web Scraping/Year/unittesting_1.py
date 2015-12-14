import unittest
from bs4 import BeautifulSoup
from urllib import urlopen
import lxml.html
import urllib

def fun(url):
    r=urlopen(url)
    soup=BeautifulSoup(r,"html.parser")
    
    for i in soup.find_all('a'):
        if i.text=='1998 - 1996':
            return (i.get('href'))
    
        
class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun("http://www.occ.gov/topics/licensing/interpretations-and-actions/index-interpretations-and-actions.html"),'/topics/licensing/interpretations-and-actions/interpretations-and-actions-1998-1996.html')

if __name__ == '__main__':
    unittest.main()
    
