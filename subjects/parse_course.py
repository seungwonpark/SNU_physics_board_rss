#-*- coding: utf-8 -*-
import urllib.request
from feedgen.feed import FeedGenerator
#from bs4 import BeautifulSoup

baseurl = 'http://physics.snu.ac.kr/php/subject_list/Notice/list.php?id='
subject_list = [
	'qphy1',
	'gp1_001',
	'gp1_002',
	'gp1_003',
	'gp1_004',
	'gp1_005',
	'gp1_006',
	'gp1_007',
	'gp1_008',
	'gp1_009',
	'gp1_010',
	'gp1_011',
	'gp1_012',
	'fp001',
	'fp002',
	'bp',
	'hphy',
	'phy001',
	'phy002',
	'phy003',
	'cpfhp',
	'qthc', # 미시세계와 거시세계는 모르겠음
	'energy',
	'mech_s',
	'mech1',
	'fmp',
	'qp_s',
	'qphy1',
	'emwave',
	'mmp',
	'ipl',
	'ibp',
	'is1',
	'rst',
	'ps',
	'ao',
	'spb'
]



for s in subject_list:
	subject = '2017_' + s

	url = baseurl + subject

	response = urllib.request.urlopen(url)
	data = response.read()
	html_doc = data.decode('utf-8')

	#soup = soup = BeautifulSoup(html_doc, 'html.parser')

	#print(soup.find_all(align="center"))


	fg = FeedGenerator()
	fg.id(subject)
	fg.title('SNU Physics Board RSS feed - ' + subject)
	fg.author({'name':'Seungwon Park','email':'yyyyy at snu dot ac dot kr'})
	fg.link(href=subject)
	fg.subtitle('SNU Physics Board RSS - ' + subject)
	fg.language('ko')


	notices = html_doc.split('</td><td>&nbsp;<a href="')
	for i in range(1,len(notices)):
		title = notices[i].split('&key=">')[1].split('</a>')[0].replace('\n','')
		author = notices[i].split('<td align="center">')[1].split('</td>')[0]
		date = notices[i].split('<td align="center">')[2].split('</td>')[0]
		post_url = 'http://physics.snu.ac.kr/php/subject_list/Notice/' + notices[i].split('">')[0]

		fe = fg.add_entry()
		fe.id(post_url)
		fe.title(title)
		fe.author({'name':author,'email':'unknown'})
		fe.link(href = post_url)


	atomfeed = fg.atom_str(pretty=True)
	fg.atom_file(subject + '.xml')