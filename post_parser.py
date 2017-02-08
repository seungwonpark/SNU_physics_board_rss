import urllib.request
baseurl = 'http://phya.snu.ac.kr/xe/underbbs/'

def post_title(srl):
	post_url = baseurl + srl
	response = urllib.request.urlopen(post_url)
	data = response.read()
	text = data.encode('utf-8')
	return text.split('<title>')[1].split('</title>')[0]

def post_author(srl):
	post_url = baseurl + srl
	response = urllib.request.urlopen(post_url)
	data = response.read()
	text = data.encode('utf-8')
	return text.split('author" onclick="return false">')[1].split('</a>')[0]

def post_time(srl):
	post_url = baseurl + srl
	response = urllib.request.urlopen(post_url)
	data = response.read()
	text = data.encode('utf-8')
	return text.split('<p class="time">')[1].split('</p>')[0].replace('\t','')