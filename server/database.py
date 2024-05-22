import sqlite3

con = sqlite3.connect('database.db', check_same_thread=False)
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS tema(
            id INTEGER PRIMARY KEY NOT NULL,
            tema TEXT NOT NULL,
            fag TEXT NOT NULL
)""")
con.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS guides(
            id INTEGER PRIMARY KEY NOT NULL,
            tema_id INTEGER NOT NULL,
            bruker_id INTEGER NOT NULL,
            bruker_navn TEXT NOT NULL,
            innhold TEXT NOT NULL,
            tittel TEXT NOT NULL,
            dato TIMESTAMP
)""")
con.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS brukere(
            id INTEGER PRIMARY KEY NOT NULL,
            navn TEXT NOT NULL,
            passord TEXT NOT NULL
)""")
con.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS kommentarer(
            id INTEGER PRIMARY KEY NOT NULL,
            bruker_id INTEGER NOT NULL,
            guide_id INTEGER NOT NULL,
            innhold TEXT NOT NULL,
            rating INTEGER NOT NULL,
            dato TIMESTAMP
)""")
con.commit()

