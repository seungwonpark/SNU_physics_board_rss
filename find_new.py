# import libraries
import urllib.request
from feedgen.feed import FeedGenerator
from post_parser import post_title

# info
baseurl = 'http://phya.snu.ac.kr/xe/underbbs/'
url ='http://phya.snu.ac.kr/xe/index.php?mid=underbbs&category=371' # notices only

# make FeedGenerator
fg = FeedGenerator()
fg.id('asdf')
fg.title('RSS Feed of SNU Physics Board - physics.snu.ac.kr')
fg.author({'name':'Seungwon Park','email':'yyyyy@snu.ac.kr'})
fg.link(href='asdf')
fg.subtitle('SNU Physics RSS')
fg.language('ko')

f = open('srl_list.txt','r')
num = f.read().split(',')
f.close()
f = open('srl_list.txt','a')


response = urllib.request.urlopen(url)
data = response.read()
text = data.decode('utf-8')

text_splitted = text.split('document_srl=')
for i in range(1,len(text_splitted)):
	srl = text_splitted[i].split('">')[0].split('#comment')[0]
	if(srl not in num):
		f.write(',' + srl)
		print('New post found : ' + srl)
		fe = fg.add_entry()
		fe.id(baseurl + srl)
		fe.title('Test')
		fe.author({'name':'Seungwon Park','email':'yyyyy@snu.ac.kr'})
		fe.link(href = baseurl + srl)


f.close()

atomfeed = fg.atom_str(pretty=True)
fg.atom_file('atom.xml')
