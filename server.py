# handle POST requests that we get from requests.py

# import libraries
import numpy as np 
from flask import Flask, request, render_template
import pickle 

# create instance of Flask() and load model into model
app = Flask(__name__, template_folder='templates')
model = pickle.load(open('model.pkl', 'rb'))

# default route set as home
@app.route('/home')
def home():
	return render_template('home.html') # render index.html

@app.route('/classify', methods=['GET'])
def classify_type():
	try:
		sepal_len = request.args.get('slen')
		sepal_wid = request.args.get('swid')
		petal_len = request.args.get('plen')
		petal_wid = request.args.get('pwid')

		# get output from classification model
		variety = model.classify(sepal_len, sepal_wid, petal_len, petal_wid)

		# render output in new HTML page
		return render_template('output.html', variety=variety)
	except:
		return 'Error'

if __name__ == '__main__':
	app.run(port=5000, debug=True)