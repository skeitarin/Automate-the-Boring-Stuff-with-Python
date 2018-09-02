#! python3

# pip install beautifulsoup4
import requests, bs4, urllib.parse, webbrowser, pyperclip

words = urllib.parse.quote(str(pyperclip.paste())) #クリップボードから検索するキーワードを取得し、URLエンコード
res = requests.get('http://google.com/search?q=' + words)
try:
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "lxml")
    elems = soup.select('.r a')
    num_open = min(3, len(elems))
    for i in range(num_open):
        print('http://google.com' + elems[i].get('href'))
        webbrowser.open('http://google.com' + elems[i].get('href'))
except Exception as e:
    print('ERROR : {}'.format(e))