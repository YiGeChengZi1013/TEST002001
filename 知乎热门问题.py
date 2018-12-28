import requests
from pyquery import PyQuery as pq

url = 'http://www.zhihu.com/explore'
headers = {
    'User-Agent': 'Mozilla/5.0(Mactintosh;Intel Mac OS X 10_13_3)AppleWebkit/537.36 (KHTML,like Gecko)Chrome/65.0.3325.162 Safari/537.36'
}
html = requests.get(url,headers=headers).text
doc = pq(html)
items = doc('.explore-tab .feed-item').items()
for item in items:
    question = item.find('h2').text()
    author = item.find('.author-link-line').text()
    answer = pq(item.find('.content').html()).text()
    file = open('知乎爬取热门问题.txt', 'a', encoding='utf-8')
    file.write('\n'.join([question,author,answer]))
    file.write('\n' + '=' * 50 + '\n')
    file.close()