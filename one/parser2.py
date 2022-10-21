from bs4 import BeautifulSoup
import urllib.request


class Parser:
    raw_html = ''
    html = ''
    results = []

    def __init__(self, url, path):
        self.url = url
        self.file = path

    def get_html(self):
        req = urllib.request.urlopen(self.url)
        self.raw_html = req.read()
        self.html = BeautifulSoup(self.raw_html, features="html.parser")

    def parsing(self):
        news = self.html.findAll('div', class_='module-card')

        for item in news:
            res = 0
            if item.find('div', class_='title'):
                res = item.find('div', class_='title').get_text(strip=True)

            self.results.append({'res': res})

    def save(self):
        f = open(self.file, 'w', encoding='utf-8')
        for i in self.results:
            f.write(f'{i["res"]} \n')
            f.write(f'********* \n')
        f.close()

    def run(self):
        self.get_html()
        self.parsing()
        self.save()
