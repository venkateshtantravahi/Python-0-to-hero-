import json
import sqlite3

conn = sqlite3.connect("roasterdb.sqlite")
curr = conn.cursor()

curr.executescript(
    """
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
"""
)

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "roster_data_sample.json"

str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:

    name = entry[0]
    title = entry[1]
    role = entry[2]

    print((name, title, role))

    curr.execute(
        """INSERT OR IGNORE INTO User (name)
        VALUES ( ? )""",
        (name,),
    )
    curr.execute("SELECT id FROM User WHERE name = ? ", (name,))
    user_id = curr.fetchone()[0]

    curr.execute(
        """INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )""",
        (title,),
    )
    curr.execute("SELECT id FROM Course WHERE title = ? ", (title,))
    course_id = curr.fetchone()[0]

    curr.execute(
        """INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ? )""",
        (user_id, course_id, role),
    )

    conn.commit()
