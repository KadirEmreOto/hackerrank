import os
import codecs
# from time import sleep
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class HackerRank(object):
    def __init__(self):
        self.site = 'http://www.hackerrank.com'
        self.delay = 10

        self.username = None
        self.password = None

        self.browser = webdriver.Firefox()

    def login(self, username, password):
        url = 'https://www.hackerrank.com/login'
        self.browser.get(url)

        user_input = self.browser.find_element_by_xpath('//input[@name="login"]')
        user_input.send_keys(username)

        pass_input = self.browser.find_elements_by_css_selector('input[name="password"]')[1]
        pass_input.send_keys(password)

        submit = self.browser.find_element_by_xpath('//button[@class="btn btn-primary login-button auth"]')
        submit.click()

        WebDriverWait(self.browser, self.delay).until(
            lambda x: x.find_element_by_xpath('//div[@class="dropdown dropdown dropdown-auth profile-menu"]')
        )

        self.username = username
        self.password = password

        print("[+] Logged In!")

    def get_domains(self):
        url = 'https://www.hackerrank.com/domains/algorithms'
        self.browser.get(url)

        ul = WebDriverWait(self.browser, self.delay).until(
            lambda x: x.find_element_by_id('challengeAccordion')
        )

        domains = map(lambda x: x.get_attribute('data-attr1'), ul.find_elements_by_tag_name('a'))

        return list(domains)

    def get_solved_challenges(self, category):
        url = 'https://www.hackerrank.com/domains/algorithms/{}/{}?filters=status%3Asolved'
        self.browser.get(url.format(category, 1))

        try:
            last = int(WebDriverWait(self.browser, self.delay).until(
                lambda x: x.find_element_by_xpath('//li[@class="page-item last-item"]')
            ).text.strip())
        except:
            last = 1

        challenges = set()

        for page in range(1, last + 1):
            if page != 1:
                self.browser.get(url.format(category, page))

            c_list = WebDriverWait(self.browser, self.delay).until(
                lambda x: x.find_element_by_class_name('challenges-list')
            )
            a_list = c_list.find_elements_by_tag_name('a')

            for a in a_list:
                challenges.add(a.get_attribute('data-attr1'))

        return challenges

    def save_all(self):
        domains = self.get_domains()

        for domain in domains:
            problems = self.get_solved_challenges(domain)

            for problem in problems:
                try:
                    self.save(domain, problem)
                except:
                    print('[-] Error: Cannot saved:', domain, problem)

    def save(self, category, problem):
        url = 'https://www.hackerrank.com/challenges/{}/submissions'.format(problem)

        for ext in ['.c', '.cpp', '.py']:
            if os.path.isfile(os.path.join(category, problem + ext)):
                return

        self.browser.get(url)
        WebDriverWait(self.browser, self.delay).until(
            lambda x: x.find_element_by_xpath('//div[@class="submissions-list-view"]')
        )

        soup = BeautifulSoup(self.browser.page_source, "html.parser")
        divs = soup.findAll('div', {'class': 'submissions-list-view'})

        surl = None
        ext = None
        for div in divs:
            if 'Accepted' in div.text:
                if 'Python' in div.text:
                    ext = '.py'
                elif 'PyPy' in div.text:
                    ext = '.py'
                else:
                    ext = '.cpp'
                surl = self.site + '/' + div.findAll('a')[1]['href']
                break

        if surl is None:
            print('[-] Error: {} -> {} cannot be opened!'.format(category, problem))
            return

        self.browser.get(surl)
        WebDriverWait(self.browser, self.delay).until(
            lambda x: x.find_element_by_xpath('//div[@class="CodeMirror-code"]')
        )

        soup = BeautifulSoup(self.browser.page_source, "html.parser")
        pres = soup.findAll('pre')

        source = u''
        for pre in pres:
            source += pre.text.replace(u'\u200b', u'') + '\n'

        if not os.path.isdir(category):
            os.mkdir(category)

        with codecs.open(os.path.join(category, problem + ext), 'w', 'utf-8') as stream:
            stream.write(source)

        print('[+] Saved:', category, '->', problem + ext)

    def close(self):
        self.browser.close()


if __name__ == '__main__':
    hackerrank = HackerRank()
    hackerrank.login('username', 'password')
    # hackerrank.save_all()
    hackerrank.save('game-theory', 'stone-piles')
    hackerrank.save('greedy', 'fighting-pits')
    hackerrank.save('recursion', 'k-factorization')
    hackerrank.close()
