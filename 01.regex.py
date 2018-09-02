#! python3
import pyperclip, re

re_phone = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            #3桁の市外局番（カッコがついていても良い）
    (\s|-|\.)?                    #区切り（スペースorハイフンorドット）
    (\d{3,4})                     #3桁の市内局番
    (\s|-|\.)?                    #区切り（スペースorハイフンorドット）
    (\d{4})                       #4桁の番号
    (\s*(ext|x|ext.)\s*\d{2,5})?  #2~5桁の内線番号
    )''', re.VERBOSE)

re_mailaddress = re.compile(r'''(
    [a-zA-Z0-9._%+-]+             #ユーザー名
    @
    [a-zA-Z0-9._]+                #ドメイン名
    (\.[a-zA-Z.]{2,5})
    )''', re.VERBOSE)

# クリップボードのテキストを取得
clip_text = str(pyperclip.paste())

matches = []
for groups in re_phone.findall(clip_text):
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    matches.append(phone_num)

for groups in re_mailaddress.findall(clip_text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('クリップボードにコピーしました：')
    print('\n'.join(matches))
else:
    print('電話番号やメールアドレスは見つかりませんでした。')
