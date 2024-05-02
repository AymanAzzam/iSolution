from flask import Flask, request, render_template
from flask.logging import create_logger
import os
import logging
import mysql.connector

host = os.environ['DB_HOST']
port = os.environ['DB_PORT']
user = os.environ['DB_USERNAME']
password = os.environ['DB_PASSWORD']

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)


@app.route('/')
def welcome():
    return render_template('form.html')


@app.route('/', methods=['POST'])
def result():
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
    result
    return render_template('form.html', entry=result)


if __name__ == "__main__":
    app.run(debug=True)

    LOG.info("db-host = %s, db-port = %s, db-user = %s\n", host, port, user)
    db = mysql.connector.connect(user=user, password=password, host=host, port=port)
    LOG.info(db)
    db.close()
