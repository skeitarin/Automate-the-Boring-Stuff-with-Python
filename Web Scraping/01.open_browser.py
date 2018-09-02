#! python3
import pyperclip, re, webbrowser, urllib.parse

address = urllib.parse.quote(str(pyperclip.paste()))

re_url = re.compile(r'{add}')
address = re_url.sub(address, 'https://www.google.co.jp/maps/place/{add}')

webbrowser.open(address)