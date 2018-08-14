from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

site = "https://toefl.kmf.com/speak/ets/order"
site0 = "https://toefl.kmf.com"
qsites ={}
fw = open('speak.csv','w')

for cl in ['/1/0','/2/0','/3/0','/4/0','/5/0']:
    for i in ['/1','/2','/3','/4']:
        html = urlopen(site+cl+i).read().decode('utf-8')
        soup = BeautifulSoup(html, features="html.parser")
        for link in soup.findAll('a', {'class': "practice-title js-practice-title"}):
            ah = link.get('href')
            off_set=link.string
            qsites[off_set] = site0+ah
            print(off_set+',\t'+qsites[off_set]+',\n')

fw.close()



'''
with open("listen.csv",'w',newline="") as csvfile:
    fieldname =['off_set','link']
    writer = csv.DictWriter(csvfile,fieldnames=fieldname)
    writer.writer
'''