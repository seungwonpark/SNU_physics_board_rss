# import libraries
import urllib.request
from feedgen.feed import FeedGenerator
from post_parser import post_title, post_author, post_time, post_files_num
from misc import is_number

# info
baseurl = 'http://physics.snu.ac.kr/xe/underbbs/'
url ='http://physics.snu.ac.kr/xe/index.php?mid=underbbs&category=371' # notices only


f = open('srl_notices.txt','r')
num = f.read().split(',')
f.close()
f = open('srl_notices.txt','a')

response = urllib.request.urlopen(url)
data = response.read()
text = data.decode('utf-8')

count_new = 0
srl_arr = []


text_splitted = text.split('document_srl=')
for i in range(1,len(text_splitted)):
	srl = text_splitted[i].split('">')[0].split('#comment')[0]
	if(is_number(srl) and srl not in srl_arr): # second statement : to prevent duplication
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
	fg.title('SNU Physics Board RSS feed - notices')
	fg.author({'name':'Seungwon Park','email':'yyyyy@snu.ac.kr'})
	fg.link(href='asdf')
	fg.subtitle('SNU Physics Board RSS - notices')
	fg.language('ko')
	for srl in srl_arr:
		print('Parsing post #' + srl + '...')
		fe = fg.add_entry()
		fe.id(baseurl + srl)
		fe.title(post_title(srl))
		fe.author({'name':post_author(srl),'email':'unknown'})
		fe.link(href = baseurl + srl)

	atomfeed = fg.atom_str(pretty=True)
	fg.atom_file('notices.xml')
	print('Added ' + str(count_new) + ' posts to feed.')

else:
	print('Posts are up-to-date.')