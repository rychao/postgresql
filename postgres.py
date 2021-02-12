import psycopg2
import json
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/summoner_by_name')

def query_db():
    conn = psycopg2.connect( user="admin", password="password123!", host="34.122.166.248", port="5432", database="my-postgres")
    cur = conn.cursor()
    cur.execute("select * from summoner_by_name limit %s", (1,))
    one = False
    r = [dict((cur.description[i][0], value) \
        for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.connection.close()
    query = (r[0] if r else None) if one else r
    return jsonify(query)

# postgres
