import urllib.request
baseurl = 'http://physics.snu.ac.kr/xe/underbbs/'

def post_title(srl):
	post_url = baseurl + srl
	response = urllib.request.urlopen(post_url)
	data = response.read()
	text = data.decode('utf-8')
	return text.split('<title>')[1].split('</title>')[0]

def post_author(srl):
	post_url = baseurl + srl
	response = urllib.request.urlopen(post_url)
	data = response.read()
	text = data.decode('utf-8')
	try:
		return text.split('<p class="meta">')[1].split('<span class="sum">')[0].split('">')[1].split('</a>')[0]
	except:
		return text.split('<p class="meta">')[1].split('<span class="sum">')[0].replace('\t','').replace('\n','')

def post_time(srl):
	post_url = baseurl + srl
	response = urllib.request.urlopen(post_url)
	data = response.read()
	text = data.decode('utf-8')
	return text.split('<p class="time">')[1].split('</p>')[0].replace('\t','').replace('\n','')


def post_files_num(srl): 
	post_url = baseurl + srl
	response = urllib.request.urlopen(post_url)
	data = response.read()
	text = data.decode('utf-8')
	try:
		return text.split('[<strong>')[1].split('</strong>]')[0]
	except:
		return 0