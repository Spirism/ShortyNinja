import sqlite3


def insert_url(conn, url):
    data = conn.execute('INSERT INTO urls (original_url) VALUES (?)', (url,))
    conn.commit()
    conn.close()

    return data


def get_url_data(conn, id, hashids):
    original_id = hashids.decode(id)
    if original_id:
        original_id = original_id[0]
        data = conn.execute('SELECT * FROM urls WHERE id = (?)', (original_id,))
        data = data.fetchone()
        conn.commit()

        return data


def find_old_url(conn, id, hashids):
    original_id = hashids.decode(id)
    if original_id:
        original_id = original_id[0]

        old_url = conn.execute('SELECT original_url FROM urls WHERE id = (?)', (original_id,)).fetchone()
        conn.commit()

        return old_url[0]


def get_clicks_data(conn, url):
    data = conn.execute("SELECT date, ip FROM clicks WHERE url = (?)", (url,)).fetchall()

    conn.commit()
    conn.close()

    return data


def update_clicks(conn, id, hashids, url, ip):
    original_id = hashids.decode(id)
    if original_id:
        original_id = original_id[0]

        clicks = conn.execute('SELECT clicks FROM urls WHERE id = (?)', (original_id,)).fetchone()[0]

        conn.execute('UPDATE urls SET clicks = (?) WHERE id = (?)', (clicks+1, original_id))

        conn.commit()

        conn.execute('INSERT INTO clicks (url, ip) VALUES (?, ?)', (url, ip))

        conn.commit()

        conn.close()


