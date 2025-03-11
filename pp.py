import sqlite3

class Def_:
    def __init__(self, db):
        self.con = sqlite3.Connection('C:/Users/Pc38/Desktop/hossien/login.db')
        self.cur = self.con.cursor()
        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS person
        (id INTEGER PRIMARY KEY, fname text, lname text, email text, password text)
        ''')
        self.con.commit()

    def insert(self, fname, lname, email, password):
        self.cur.execute('INSERT INTO person VALUES(NULL,?,?,?,?)', (fname, lname, email, password))
        self.con.commit()

    def serch(self, email, password):
        self.cur.execute('select * from person where email=? or password=?', (email, password))
        return self.cur.fetchall()