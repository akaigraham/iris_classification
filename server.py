# import libraries
import numpy as np 
from flask import Flask, request, render_template
import pickle 
from sklearn import datasets

iris = datasets.load_iris()
target_names = list(iris.target_names)

# create instance of Flask() and load model
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

# default route set as home
@app.route('/home')
def home():
	return render_template('home.html') # render index.html

# classify input
@app.route('/classify')
def classify():
	
	# get entered values
	slen = request.args.get('slen')
	swid = request.args.get('swid')
	plen = request.args.get('plen')
	pwid = request.args.get('pwid')

	# run prediction
	inputs = np.array([slen, swid, plen, pwid])
	pred = model.predict(inputs.reshape(1,-1))
	variety=target_names[pred[0]]
	return render_template('output.html', variety=variety)

# run the flask server
if __name__ == '__main__':
	app.run(debug=True)