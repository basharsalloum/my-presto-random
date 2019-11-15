# By Bashar 14-11-2019
#
import prestodb
from collections import OrderedDict

from flask import Flask, request
from flask_restful import Resource, Api

#
# Functions
def connect(host,port,user,catalog,schema):
    conn=prestodb.dbapi.connect(
    host=host,
    port=port,
    user=user,
    catalog=catalog,
    schema=schema,
    )
    return conn
#    
def query(conn,query):
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows
#   
def to_json(rows):    
    payload = []
    content = {}
    for row in rows:         
        content = OrderedDict([('ride_id', str(row[0])), ('driver_id', str(row[1])), ('passenger_id', str(row[2])), ('created_at', str(row[3]))])
                   
        payload.append(content)
        content = {}
    return payload
#    
# Rest API
class Random(Resource):
    def get(self):
        conn=connect('localhost',7000,'root','mysql','sampledb')
        rows=query(conn,'SELECT * from sampledata order by RAND() limit 1')
        return(to_json(rows))
#
app = Flask(__name__)
api = Api(app)
api.add_resource(Random, '/myapp/random') # Router
#       
# main
if __name__ == '__main__':
   app.run(port='5002')
			