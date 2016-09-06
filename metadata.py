import requests
from flask import Flask
app = Flask(__name__)

@app.route('/')
def get_data():
	return requests.get('http://169.254.169.254/latest/meta-data/')
if __name__=='__main__':
	app.run(host='0.0.0.0')

