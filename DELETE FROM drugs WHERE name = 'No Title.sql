-- DELETE FROM drugs WHERE name = 'No Title Available';
-- DROP TABLE message;
CREATE TABLE chat (
    id INTEGER PRIMARY KEY,
    text TEXT,
    date TEXT,
    username TEXT,
    drug_id INTEGER,
    FOREIGN KEY (drug_id) REFERENCES drug(id)
);