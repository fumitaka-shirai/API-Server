-- SQLite
CREATE TABLE member(
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 name TEXT,
 age INTEGER,
 created_date TIMESTAMP DEFAULT (datetime('now','localtime'))
);
 