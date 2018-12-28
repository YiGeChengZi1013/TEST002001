import urllib
import requests

def write_file(file_name,text):
    print('正在存储文件'+file_name)
    f = open(file_name,'w+')
    f.write(text)
    f.close()

def load_page(url):
    req = requests.request(url)
    response = urllib.urlopen(req)
    html = response.read()

    return html