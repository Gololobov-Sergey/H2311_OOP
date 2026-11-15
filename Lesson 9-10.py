import sqlite3
import hashlib

connection = sqlite3.connect("db.sl3", 5)
cur = connection.cursor()

# ======= CREATE TABLE ========
# cur.execute("CREATE TABLE users (login TEXT, password TEXT, name TEXT)")
# connection.commit()


# ======= INSERT ========
# login = input("Login    : ")
# passw = input("Password : ")
# name = input("NickName : ")
#
# h = hashlib.sha256()
# h.update(b"{passw}")
# h_passw = h.hexdigest()
#
# cur.execute(f"INSERT INTO users (login, password, name) VALUES ('{login}', '{h_passw}', '{name}')")
# connection.commit()

# ======= SELECT ========
# cur.execute(f"SELECT * FROM users")
# cur.execute(f"SELECT * FROM users WHERE login = 'serg'")
# connection.commit()
# res = cur.fetchall()
# print(res)
# print(res[0])
# print(res[0][0])
# for l, p, n in res:
#     print("L: ", l, "P: ", p, "N: ", n)

# ======= UPDATE ========
# cur.execute(f"UPDATE users SET login='anna' WHERE rowid=2")
# connection.commit()


# ======= DELETE ========
# cur.execute("DELETE FROM users WHERE rowid=2")
# connection.commit()

connection.close()