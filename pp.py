import sqlite3

class Def_:
    def __init__(self, db):
        self.con = sqlite3.Connection('D:/hossien/my  H O O M/p/examlogin.db')
        self.cur = self.con.cursor()
        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS person
        (id INTEGER PRIMARY KEY, fname text, lname text, email text, password text)
        ''')
        self.con.commit()

    def insert_(self, fname, lname, email, password):
        self.cur.execute('INSERT INTO person VALUES(NULL,?,?,?,?)', (fname, lname, email, password))
        self.con.commit()

    def serch_(self, email, password):
        self.cur.execute('select * from person where email=? or password=?', (email, password))
        return self.cur.fetchall()