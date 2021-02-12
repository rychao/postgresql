from flask import Flask, jsonify
app = Flask(__name__)
import psycopg2
import psycopg2.extras

@app.route('/summoner_by_name')
def hello_world():
    conn = psycopg2.connect( user="admin", password=<REDACTED>, host=<REDACTED>, port="5432", database="my-postgres")
    cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    cur.execute("SELECT * from summoner_by_name")
    rows = cur.fetchall()
    # print(type(rows))
    return jsonify(rows)

if __name__ == '__main__':
   app.run()
