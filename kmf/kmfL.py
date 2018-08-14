from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

site = "https://toefl.kmf.com/listen/ets/order"
site0 = "https://toefl.kmf.com/"
qsites ={}
off = 1
set = 1
for cl in ['/1/0','/2/0','/3/0','/4/0','/5/0']:
    for i in ['/0','/1','/2','/3']:
        html = urlopen(site+cl+i).read().decode('utf-8')
        soup = BeautifulSoup(html, features="html.parser")
        for link in soup.findAll('a', {'class': "practice-title js-practice-title"}):
            ah = link.get('href')
            qsites[off, set] = ','+site0+ah
            print(qsites[off,set])
            set += 1
            if set > 6:
                set = 1
                off += 1
