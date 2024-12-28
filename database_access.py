import psycopg2
import json

t = ''
with open('env.json', 'r') as f:
    t = f.read()

env = json.loads(t)
conn = psycopg2.connect(dbname='hospital', user=env['user'], password=env['password'], host=env['host'], port=env['port'])
cur = conn.cursor()

def select(query):
    cur.execute(query)
    records = cur.fetchall()
    return records



                                                 