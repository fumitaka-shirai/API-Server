import requests
from bs4 import BeautifulSoup
import sqlite3

conn = sqlite3.connect('drugs.db')
c = conn.cursor()

# 共通の処理を実行する関数
def process_common_info(soup):
    p_tags = soup.find_all('p')
    contents_block_div = soup.find_all('div', class_='contents-block')
    product_td = soup.find('td')
    a_tags = soup.find_all('a')
    td_tags = soup.find_all('td')

    category = ""  # カテゴリ変数を初期化
    dose = ""  # dose変数を初期化

    for p in p_tags:
        text = p.get_text()
        if "通常、" in text:
            print(text)
            dose = text

    for a in a_tags:
        href = a.get('href')
        if href is not None and "example.com" in href:
            print(a.get_text())
            category = a.get_text()

    if product_td is not None:
        print(product_td.get_text())

    for td in td_tags:
        text = td.get_text()
        if "気道" in text:
            print(text)
            category = text

    for div in contents_block_div:
        text = div.get_text()
        if "通常、" in text:
            print(text)
            dose = text

    return category, dose

urls = [
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00059041',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00067912',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00055886',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00056315',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00057119',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00053562',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00051194',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00058267',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00054823'
]

for url in urls:
    res = requests.get(url)
    res.encoding = 'UTF-8'
    soup = BeautifulSoup(res.text, 'html.parser')

    name = soup.title.get_text().split(" : ")[1]
    print(name)

    category, dose = process_common_info(soup)


    if url == 'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00056315':
        td_tags = soup.find_all('td')
        for td in td_tags:
            text = td.get_text()
            if "経口用" in text:
                print(text)
                category = text

    if url == 'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00053562':
        td_tags = soup.find_all('td')
        for td in td_tags:
            text = td.get_text()
            if "ロイコ" in text:
                print(text)
                category = text

    if url == 'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00051194':
        td_tags = soup.find_all('td')
        for td in td_tags:
            text = td.get_text()
            if "ロイコ" in text:
                print(text)
                category = text

    if url == 'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00058267':
        p_tags = soup.find_all('p')
        for p in p_tags:
            text = p.get_text()
            if "通常" in text:
                print(text)
                dose = text
        items = soup.find_all("td", class_="item")
        matching_items = [item for item in items if item.text.strip() == "小児用解熱鎮痛剤"]
        for item in matching_items:
            print(item.text)
            category = item.text

    if url == 'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00054823':
        td_tags = soup.find_all('td')
        for td in td_tags:
            text = td.get_text()
            if "鎮痛・消炎" in text:
                print(text)
                category = text

    c.execute("INSERT INTO drugs (name, category,dose) VALUES (?, ?, ?)",
              (name, category, dose))
    conn.commit()

# データベース接続をクローズ
conn.close()
