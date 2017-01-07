import os, codecs
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup

class HackerRank(object):
	def __init__(self, username, password):
		self.username = username
		self.password = password

		self.site = 'http://www.hackerrank.com'
		self.delay = 5

		self.browser = webdriver.Firefox()

	def Login(self):
		url = 'https://www.hackerrank.com/login'
		self.browser.get(url)

		username = self.browser.find_element_by_xpath('//input[@name="login"]')
		username.send_keys(self.username)

		password = self.browser.find_elements_by_css_selector('input[name="password"]')[1]
		password.send_keys(self.password)

		submit = self.browser.find_element_by_xpath('//button[@class="btn btn-primary login-button auth"]')
		submit.click()

		self.browser.implicitly_wait(5)

	def List(self, name, i):
		url = 'https://www.hackerrank.com/domains/algorithms/{}/page:{}'.format(name, i)
		self.browser.get(url)
		sleep(5)

		soup = BeautifulSoup(self.browser.page_source, "html.parser")
		prbs = soup.findAll('div', {'class': 'content--list_body'})
		
		c = 1
		for prb in prbs:
			if prb.find('i', {'class': 'icon-ok'}):
				n = prb.find('a', {'data-attr1': True })['data-attr1']
				self.Save(n, name)
				c += 1

	def Save(self, name, d):
		url = 'https://www.hackerrank.com/challenges/{}/submissions'.format(name)

		if name + '.py' in os.listdir(d): return
		if name + '.cpp' in os.listdir(d): return

		self.browser.get(url)
		sleep(5)

		soup = BeautifulSoup(self.browser.page_source, "html.parser")
		divs = soup.findAll('div', {'class': 'submissions-list-view'})

		surl = None
		ext = None
		for div in divs:
			if 'Accepted' in div.text:
				if 'Python' in div.text: ext = '.py'
				elif 'PyPy' in div.text: ext = '.py'
				else: ext = '.cpp'
				surl = self.site + '/' + div.findAll('a')[1]['href']
				break

		self.browser.get(surl)
		sleep(5)

		soup = BeautifulSoup(self.browser.page_source, "html.parser")
		pres = soup.findAll('pre')

		source = u''
		for pre in pres:
			source += pre.text.replace(u'\u200b', u'') + '\n'

		with codecs.open(d + '/' + name + ext, 'w', 'utf-8') as file:
			file.write(source)
		print d + '/' + name + ext

if __name__ == '__main__':
	hackerrank = HackerRank('username', 'password')
	hackerrank.Login()

	# Page Numbers
	l = { 'implementation': 5, 'warmup': 1, 'constructive-algorithms': 1,
		  'strings': 4, 'arrays-and-sorting': 2, 'search':2, 'graph-theory': 6,
		  'greedy': 3, 'dynamic-programming': 9, 'bit-manipulation': 3,
		  'game-theory': 3, 'np-complete-problems': 1, 'recursion': 1}

	for name in l:
		try: os.mkdir(name)
		except: pass

		for i in xrange(l[name]):
			hackerrank.List(name, i+1)
	#hackerrank.Save('solve-me-first')
