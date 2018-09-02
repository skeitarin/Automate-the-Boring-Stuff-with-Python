#! python3
import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
try:
    res.raise_for_status()
    print(res.text[:250])

    with open('RemeoAndJuliet.txt', 'wb') as play_file:
        for chunk in res.iter_content(100000):
            play_file.write(chunk)

except Exception as e:
    print('ERROR : {}'.format(e))
