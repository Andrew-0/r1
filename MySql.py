config = {'user': 'root',
          'password': 'root',
          'host': 'localhost',
          'port': '3306',
          'database': 'test'}

"""
with open('C:\\Users\\user1\\Desktop\\Ѕаланс подушек сент€брь 2016 переработанный.csv') as csvfile:
    rr = csv.reader(csvfile, delimiter=';', quotechar='"')
    for row in rr:
        print (', '.join(row))
"""

conn = mysql.connector.connect(**config)
cur = conn.cursor()
cur.execute('select * from test.feeds')
for s in cur.fetchall():
    print(s)
conn.close()