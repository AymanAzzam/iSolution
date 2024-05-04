from flask import Flask, request, render_template
from flask.logging import create_logger
import os
import hvac
import logging
import mysql.connector

vault_url = os.environ['VAULT_ADDR']
vault_token = os.environ['VAULT_TOKEN']
db_host = os.environ['DB_HOST']
db_port = os.environ['DB_PORT']

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)
# Hashicorp Authentication
client = hvac.Client(url=vault_url, token=vault_token,)

def test_db():
    result = ""
    try:
        # Reading secrets
        read_response = client.secrets.kv.read_secret_version(path='db')
        username = read_response['data']['data']['username']
        password = read_response['data']['data']['password']
        
        LOG.info("db-host = %s, db-port = %s, db-user = %s\n", db_host, db_port, username)
        db = mysql.connector.connect(user=username, password=password, host=db_host, port=db_port)
        LOG.info(db)
        db.close()
    except:
        result = "Could not connect to database"
    return result

@app.route('/')
def welcome():
    return render_template('form.html')


@app.route('/', methods=['POST'])
def result():
    test = test_db()
    if test:
        return render_template('form.html', entry=test)

    x = request.form.get("x", type=int, default=0)
    y = request.form.get("y", type=int, default=0)
    operation = request.form.get("operation")
    LOG.info("x = %s, y = %s, operation = %s\n", x, y, operation)
    if(operation == 'Addition'):
        result = x + y
    elif(operation == 'Subtraction'):
        result = x - y
    elif(operation == 'Multiplication'):
        result = x * y
    elif(operation == 'Division'):
    	if(x==0 and y==0):
    		result = 0
    	else:
        	result = x / y
    else:
        result = 0
    return render_template('form.html', entry=result)


if __name__ == "__main__":
    app.run(debug=True)
