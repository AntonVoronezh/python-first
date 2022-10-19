from bs4 import BeautifulSoup
import urllib.request
# help('modules')

req = urllib.request.urlopen('https://dvmn.org/modules/')

html = req.read()
soup = BeautifulSoup(html, features="html.parser")
# print(soup)
news = soup.findAll('div', class_='module-card')
# print(news)

results = []

for item in news:
    aaa = 0
    bbb = 0
    if item.find('div', class_='title'):
        aaa = item.find('div', class_='title').get_text(strip=True)
        # print(aaa)
    if item.find('div', class_='subtitle'):
        bbb = item.find('div', class_='subtitle').get_text(strip=True)
        # print(bbb.replace('\n', ''))
    ccc = item.a.get('href')
    # print(ccc)
    results.append({'aaa': aaa, 'bbb': bbb, 'ccc': ccc})

print(results, end='\n')

f = open('ffff.txt', 'w', encoding='utf-8')
for i in results:
    f.write(f'{i["aaa"]} \n')
    f.write(f'{i["bbb"]} \n')
    f.write(f'{i["ccc"]} \n')
    f.write(f'********* \n\n\n')
f.close()