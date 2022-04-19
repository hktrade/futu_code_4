'''
@ WECHAT / TELEGRAM    :   MGSJZLS
@ Youtube Channel      :   youtube.com/c/美股数据张老师
'''
from bs4 import BeautifulSoup
import bs4 as bs
import json
import urllib
import urllib.request
import requests
import sys,time

# >Earnings</td><td width="8%" class="snapshot-td2" align="left"><b>Apr 15 BMO</b></td>
def get_earn(symbol):
	symbol=symbol.replace('US.','')
	symbol=symbol.upper()
	url = 'https://finviz.com/quote.ashx?t='+symbol

	user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
	headers={'User-Agent':user_agent,}
	request=urllib.request.Request(url,None,headers)
	response = urllib.request.urlopen(request)
	data = response.read()
	soup = BeautifulSoup(data,'html.parser')

	# soup = soup.decode()

	# for k in soup.find_all('td'):
		# if k.get_text().find('Earnings')!=-1 and k.find('Earnings</td><td width="8%" class="snapshot-td2" align="left"><b>')!=-1:
			# print(k.get_text())

	ret='None'
	for k in soup.find_all('tr', attrs={'class' : 'table-dark-row'}):
		if k.get_text().find('Earnings')!=-1 and k.find('Earnings</td><td width="8%" class="snapshot-td2" align="left"><b>')!=-1:
			ret=k.get_text().split('Earnings')[1]
			ret=ret.split('Payout')[0]
	print(ret)

print('\n get earnings day (VX 1013001850):\n')

if len(sys.argv)>1:
	for i,symbol in enumerate(sys.argv):
		if symbol.isupper():	
			print(sys.argv[i])
			get_earn(str(sys.argv[i]))
else:
	print('Invalid input')