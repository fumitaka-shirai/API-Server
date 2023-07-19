import requests
import time
from bs4 import BeautifulSoup
import sqlite3
import logging

conn = sqlite3.connect('drugs.db')
c = conn.cursor()
logging.basicConfig(filename='error_log.txt', level=logging.ERROR)

try:
    urls = []
    for i in range(380, 15000):
        japic_code = str(i).zfill(8)  # 8桁の0パディングされたJapicコードを生成
        url = f'https://www.kegg.jp/medicus-bin/japic_med?japic_code={japic_code}'
        urls.append(url)

    for url in urls:
        res = requests.get(url)
        res.encoding = 'UTF-8'
        soup = BeautifulSoup(res.text, 'html.parser')

        title_element = soup.title
        if title_element is not None:
            title_text = title_element.get_text()
            if " : " in title_text:
                name = title_text.split(" : ")[1]
            else:
                name = "No Title Available"
        else:
            name = "No Title Available"

        category = ''

        th_tags = soup.find_all('th')
        td_tags = soup.find_all('td')

        for th in th_tags:
            if th.get_text() == '薬効分類名':
                next_td = th.find_next_sibling('td')
                if next_td:
                    category = next_td.get_text()
                    print(category)

        td_tags = soup.find_all('td', class_='title')

        for td in td_tags:
            if td.get_text() == '薬効分類名':
                next_td = td.find_next_sibling('td', class_='item')
                if next_td:
                    category = next_td.get_text()
                    print(category)

        dose = ""

        h5_tags = soup.find_all('h5')
        h4_tags = soup.find_all('h4', class_='contents-title', id='par-6')
        div_tags = soup.find_all('div', class_='contents-block')

        for h5 in h5_tags:
            if '用法及び用量' in h5.get_text():
                next_div = h5.find_next_sibling('div', class_='block1')
                if next_div:
                    dose = next_div.get_text()
                    print(dose)

        for h4 in h4_tags:
            if '用法及び用量' in h4.get_text():
                next_div = h4.find_next_sibling('div', class_='contents-block')
                if next_div:
                    dose = next_div.get_text()
                    print(dose)

        h5_tags = soup.find_all('h5')
        div_tags = soup.find_all('div', class_='block1')

        for h5 in h5_tags:
            if '用法用量' in h5.get_text():
                next_div = h5.find_next_sibling('div', class_='block1')
                if next_div:
                    for p in next_div.find_all('p'):
                        dose += p.get_text() + "\n"  # 各段落を改行で連結
                    print(dose.strip())

        for h5 in h5_tags:
            if '用法・用量' in h5.get_text():
                next_div = h5.find_next_sibling('div', class_='block1')
                if next_div:
                    for p in next_div.find_all('p'):
                        dose += p.get_text() + "\n"  # 各段落を改行で連結
                    print(dose.strip())
        

                    

        c.execute("INSERT INTO drugs (name, category, dose) VALUES (?, ?, ?)", (name, category, dose))
        conn.commit()

        time.sleep(5)

except Exception as e:
    # エラーメッセージをログに書き込む
    logging.error("書き込みが出来ませんでした")

conn.close()
