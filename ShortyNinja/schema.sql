DROP TABLE IF EXISTS urls;

CREATE TABLE urls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    original_url TEXT NOT NULL,
    clicks INTEGER NOT NULL DEFAULT 0
)