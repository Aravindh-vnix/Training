#!flask/bin/python
from flask import Flask, jsonify, request
from cassandra.query import dict_factory
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import datetime

auth_provider = PlainTextAuthProvider(username='cassandra', password='cassandra')
cluster = Cluster(['172.17.0.1'],32000,auth_provider=auth_provider)
keyspace='sample_demo'
connection=cluster.connect(keyspace)
connection.row_factory = dict_factory

app = Flask(__name__)

@app.route('/users',methods=['GET'])
def all_users():
    users_list = []
    users=connection.execute("select * from users")
    for user in users:
        users_list.append(user)
    return jsonify(users_list)

@app.route('/users/<int:user_id>',methods=['GET'])
def get_user(user_id):
	users = connection.execute("select * from users where user_id =%d" %int(user_id))
	user = filter(lambda t: t['user_id'] == user_id, users)
	return jsonify({'user':user})

@app.route('/worklog',methods=['POST'])
def worklog():
	json_data = request.json
	user_id = json_data.get("user_id")
	user_name = json_data.get("user_name")
	status=json_data.get("status")
	prepare_stmt=connection.prepare("insert into worklogs(user_id, user_name, created_ts, Status) values (?,?,?,?)")
	bind_stmt = prepare_stmt.bind([user_id,user_name,datetime.datetime.now(), status])
	stmt = connection.execute(bind_stmt)
	return jsonify(json_data)

@app.route('/worklog/<int:user_id>',methods=['GET'])
def user_worklog(user_id):
	worklog_of_user=connection.execute("select * from worklogs where user_id=%d" %int(user_id))
	work = filter(lambda t:t['user_id'] == user_id, worklog_of_user)
	return jsonify({'work':work})

if __name__ == '__main__':
    app.run(debug=True)
