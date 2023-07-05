import requests
from bs4 import BeautifulSoup
import sqlite3

conn = sqlite3.connect('drugs.db')
c = conn.cursor()

urls = [
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00059041',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00067912',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00055886',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00056315',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00050617',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00057119',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00053562',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00051194',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00058267',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00054823',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00070777',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00048083',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00065375',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00059506',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00062726',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00054178',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00068210',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00065322',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00061681',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00052038',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00062425',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00062803',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00066927',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00068932',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00067321',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00061194',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00060553',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00061470',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00060545',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00052465',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00060549',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00066181',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00062255',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00063406',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00067494',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00061859',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00063434',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00062589',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00058959',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00060048',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00059507',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00070761',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00056791',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00070477',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00059233',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00068720',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00070070',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00067659',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00067301',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00061180',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00061213',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00058280',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00061437',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00062353',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00070680',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00056175',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00060403',
    'https://www.kegg.jp/medicus-bin/japic_med?japic_code=00012985',

]

for url in urls:
    res = requests.get(url)
    res.encoding = 'UTF-8'
    soup = BeautifulSoup(res.text, 'html.parser')

    name = soup.title.get_text().split(" : ")[1]
    print(name)


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
    
    h4_tags = soup.find_all('h4', class_='contents-title', id='par-6')
    div_tags = soup.find_all('div', class_='contents-block')


    dose_list = []

    for h4 in h4_tags:
        if '用法及び用量' in h4.get_text():
           next_div = h4.find_next_sibling('div', class_='contents-block')
           if next_div:
            dose = next_div.get_text()
            print(dose)

    h5_tags = soup.find_all('h5')
    div_tags = soup.find_all('div',class_='block1')

    for h5 in h5_tags:
        if '用法用量' in h5.get_text():
          next_div = h5.find_next_sibling('div', class_='block1')
          if next_div:
            for p in next_div.find_all('p'):
                    dose += p.get_text() + "\n"  # 各段落を改行で連結
            print(dose.strip())
             
    c.execute("INSERT INTO drugs (name, category,dose) VALUES (?, ?, ?)",(name, category, dose))
    conn.commit()

conn.close()