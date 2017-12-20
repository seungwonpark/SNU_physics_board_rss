# import libraries
import urllib.request
from feedgen.feed import FeedGenerator
from post_parser import post_title, post_author, post_time, post_files_num
from misc import is_number

# info
baseurl = 'http://phya.snu.ac.kr/xe/underbbs/'
url ='http://phya.snu.ac.kr/xe/index.php?mid=underbbs&category=372' # notices + general


f = open('srl_notices.txt','r')
num_notices = f.read().split(',')
f.close()

g = open('srl_general.txt','r')
num_general = g.read().split(',')
g.close()
g = open('srl_general.txt','a')

response = urllib.request.urlopen(url)
data = response.read()
text = data.decode('utf-8')

count_new = 0
srl_arr_general = []


text_splitted = text.split('document_srl=')
for i in range(1,len(text_splitted)):
	srl = text_splitted[i].split('">')[0].split('#comment')[0]
	if(is_number(srl)):
		if(srl not in num_notices and srl not in srl_arr_general): # second statement : to prevent duplication
			srl_arr_general.append(srl)
			if(srl not in num_general):
				count_new += 1
				g.write(',' + srl)
				print('New post found : ' + srl)

g.close()

if(count_new != 0):
	print('Started generating feed...')
	# make FeedGenerator
	fg = FeedGenerator()
	fg.id('asdf')
	fg.title('SNU Physics Board RSS feed - general')
	fg.author({'name':'Seungwon Park','email':'yyyyy at snu dot ac dot kr'})
	fg.link(href='asdf')
	fg.subtitle('SNU Physics Board RSS - general')
	fg.language('ko')
	for srl in srl_arr_general:
		print('Parsing post #' + srl + '...')
		fe = fg.add_entry()
		fe.id(baseurl + srl)
		fe.title(post_title(srl))
		fe.author({'name':post_author(srl),'email':'unknown'})
		fe.link(href = baseurl + srl)

	atomfeed = fg.atom_str(pretty=True)
	fg.atom_file('general.xml')
	print('Added ' + str(count_new) + ' posts to feed.')

else:
	print('Posts are up-to-date.')