# import libraries
import urllib.request
from feedgen.feed import FeedGenerator
from post_parser import post_title, post_author, post_time, post_files_num
from misc import is_number

# info
baseurl = 'http://phya.snu.ac.kr/xe/underbbs/'
url ='http://phya.snu.ac.kr/xe/index.php?mid=underbbs&category=371' # notices only


f = open('srl_list.txt','r')
num = f.read().split(',')
f.close()
f = open('srl_list.txt','a')

response = urllib.request.urlopen(url)
data = response.read()
text = data.decode('utf-8')

count_new = 0
srl_arr = []


text_splitted = text.split('document_srl=')
for i in range(1,len(text_splitted)):
	srl = text_splitted[i].split('">')[0].split('#comment')[0]
	if(is_number(srl)):
		srl_arr.append(srl)
		if(srl not in num):
			count_new += 1
			f.write(',' + srl)
			print('New post found : ' + srl)

f.close()

if(count_new != 0):
	print('Started generating feed...')
	# make FeedGenerator
	fg = FeedGenerator()
	fg.id('asdf')
	fg.title('RSS Feed of SNU Physics Board - physics.snu.ac.kr')
	fg.author({'name':'Seungwon Park','email':'yyyyy@snu.ac.kr'})
	fg.link(href='asdf')
	fg.subtitle('SNU Physics Board RSS')
	fg.language('ko')
	for srl in srl_arr:
		print('Parsing post #' + srl + '...')
		fe = fg.add_entry()
		fe.id(baseurl + srl)
		fe.title(post_title(srl))
		fe.author({'name':post_author(srl),'email':'yyyyy@snu.ac.kr'})
		fe.link(href = baseurl + srl)

	atomfeed = fg.atom_str(pretty=True)
	fg.atom_file('atom.xml')
	print('Added ' + str(count_new) + ' posts to feed.')

else:
	print('Posts are up-to-date.')