#! python3

import requests, bs4, os

url = 'https://xkcd.com/'
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    #ページをダウンロード
    print('ページをダウンロード中...{}'.format(url))
    res = requests.get(url)
    try:
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text)

        #画像のURLを見つける
        comic_elem = soup.select('#comic img')
        if comic_elem == []:
            print('コミック画像が見つかりませんでした。')
        else:
            comic_url = 'http:' + comic_elem[0].get('src')
            #画像をダウンロード
            print('画像をダウンロード中...{}'.format(comic_url))
            res = requests.get(comic_url)
            res.raise_for_status()

            #画像を保存
            with open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb') as image_file:
                for chunk in res.iter_content(10000):
                    image_file.write(chunk)
        
        #PrevボタンのURLを取得
        prev_link = soup.select('a[rel="prev"]')[0]
        url = 'https://xkcd.com/' + prev_link.get('href')

    except Exception as e:
        print('ERROR : {}'.format(e))
