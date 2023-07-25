# API-server

### データベース作成方法

sqlite3ターミナル内で以下のコードを実行することでdrug.dbが作成される。
```
.open drug.db
```


### データベースのテーブル作成

SQLITE EXPLORERでNew　Queryを選択。
SQLite.sql内で以下のSQL文を入力し、Run Queryを実行。
```
-- SQLite
CREATE TABLE drug(
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 category TEXT,
 name TEXT,
 dose TEXT,
 taste TEXT
);
```
SQLITE　EXPLORERを更新するとこれにより`drug`という名前のテーブルが作成される。

### テーブルへのデータの挿入

SQLite.sql内で以下のSQL文を入力し、Run Queryを実行。
```
INSERT INTO drug (category, name,dose,taste)
VALUES('去痰薬','ムコダインDS50%','体重あたり1回10㎎/㎏　1日3回まで',	'ピーチ'),
      ('去痰薬','ムコソルバンDS1.5%','体重あたり1日0.06g/㎏　1日3回まで','ヨーグルト'),
      ('抗生剤','セフゾン細粒小児用10%','体重あたり1日9~18㎎/㎏　1日3回まで','ストロベリー'),
      ('抗生剤','メイアクトMS小児用細粒10%','体重あたり1日3㎎/㎏　1日3回まで','ヨーグルト'),
      ('鎮咳薬','メジコン配合シロップ','年齢により8~14歳1日9~16ml、3か月~7歳1日3~8ml　1日3~4回まで','チェリー'),
      ('鎮咳薬','アスベリン散10%','年齢により1歳未満5~20㎎、1歳以上3歳未満10~25㎎、3歳以上6歳未満15~40㎎'1日3回まで','甘い'),
      ('抗アレルギー薬','シングレア細粒4㎎','年齢により1歳以上6歳未満4㎎　1日1回まで','なし'),
      ('抗アレルギー薬','オノンドライシロップ10%','体重あたり7㎎/㎏　1日2回まで','ヨーグルト'),
      ('鎮痛薬','カロナール細粒20%','体重あたり10~15㎎/㎏　1日60㎎/㎏まで','オレンジ'),
      ('鎮痛薬','ポンタール散50%','体重あたり6.5㎎/㎏　1日2回まで','なし')
```
SQLITE　EXPLORERを更新するとこれにより`drug`という名前のテーブル内にデータが挿入される。

### APIサーバーの実行方法
ターミナル内で以下のコードを実行し、APIサーバーを立ち上げる。
```
python app.py

```

###　chatのデーターベース作成

```
CREATE TABLE chat (
    id INTEGER PRIMARY KEY,
    text TEXT,
    date TEXT,
    username TEXT,
    drug_id INTEGER,
    FOREIGN KEY (drug_id) REFERENCES drug(id)
);

```

SQLITE　EXPLORERを更新するとこれにより`chat`という名前のテーブルが作成される。