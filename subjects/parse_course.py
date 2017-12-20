#-*- coding: utf-8 -*-
import urllib.request
from feedgen.feed import FeedGenerator
#from bs4 import BeautifulSoup

baseurl = 'http://phya.snu.ac.kr/php/subject_list/Notice/list.php?id='
subject_list = [
	# 'qphy1',
	# 'gp1_001',
	# 'gp1_002',
	# 'gp1_003',
	# 'gp1_004',
	# 'gp1_005',
	# 'gp1_006',
	# 'gp1_007',
	# 'gp1_008',
	# 'gp1_009',
	# 'gp1_010',
	# 'gp1_011',
	# 'gp1_012',
	# 'fp001',
	# 'fp002',
	# 'bp',
	# 'hphy',
	# 'phy001',
	# 'phy002',
	# 'phy003',
	# 'cpfhp',
	# 'qthc', # 미시세계와 거시세계는 모르겠음
	# 'energy',
	# 'mech_s',
	# 'mech1',
	# 'fmp',
	# 'qp_s',
	# 'qphy1',
	# 'emwave',
	# 'mmp',
	# 'ipl',
	# 'ibp',
	# 'is1',
	# 'rst',
	# 'ps',
	# 'ao',
	# 'spb',
	# 'idra',
	# 'qm',
	# 'electro',
	# 'cm',
	# 'alab',
	# 'cmp1',
	# 'bnpp',
	# 'lp',
	# 'ptcp',
	# 'qft1',
	# 'atap1',
	# 'atcmp1',
	# 'atfp',
	# 'acmp',
	# 'sphy1',
	# 'sphy2'
	'gp2_006',
	'gp2_005',
	'fp2_003',
	'bp2',
	'pfh_ss',
	'mi_ma',
	'gp2_009',
	'gp2_008',
	'phy2_002',
	'hphy2',
	'gp2_012',
	'gp2_010',
	'gp2_007',
	'fp2_002',
	'gp2_003',
	'gp2_004',
	'phy2_001',
	'gp2_002',
	'phy2_003',
	'gp2_001',
	'gp2_011',
	'emtse',
	'exer_em',
	'exer_mech2',
	'rmmp',
	'mech2',
	'em',
	'qp2',
	'tsp',
	'cp',
	'iplab2',
	'esc',
	'exer_qp2',
	'pnt',
	'shap',
	'f_mech',
	'is2',
	'iap',
	'nap',
	'cpcmp',
]

course_materials = []
homework = []

for s in subject_list:
	course_materials.append(s+'.c')
	homework.append(s+'.h')

subject_list = subject_list + course_materials + homework

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
	fg.title(subject + ' - SNU Physics Board RSS feed')
	fg.author({'name':'Seungwon Park','email':'yyyyy at snu dot ac dot kr'})
	fg.link(href=subject)
	fg.subtitle(subject + ' - SNU Physics Board RSS feed')
	fg.language('ko')


	notices = html_doc.split('</td><td>&nbsp;<a href="')
	for i in range(1,len(notices)):
		title = notices[i].split('&key=">')[1].split('</a>')[0].replace('\n','')
		author = notices[i].split('<td align="center">')[1].split('</td>')[0]
		date = notices[i].split('<td align="center">')[2].split('</td>')[0]
		post_url = 'http://phya.snu.ac.kr/php/subject_list/Notice/' + notices[i].split('">')[0]

		fe = fg.add_entry()
		fe.id(post_url)
		fe.title(title)
		fe.author({'name':author,'email':'unknown'})
		fe.link(href = post_url)


	atomfeed = fg.atom_str(pretty=True)
	fg.atom_file(subject.replace('.c','_c').replace('.h','_h') + '.xml')