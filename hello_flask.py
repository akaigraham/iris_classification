# minimal flask application looks like this

# import Flask class
from flask import Flask

# create an instance of the class
# first argument is the name of the app's module or package
# __name__ is a convenient shortcut for this that is appropriate in most cases
app = Flask(__name__) 

# route decorator to tell Flask what url should trigger our function
# the url "/" is associated with the root URL.  If site's domain 
# was example.org and we want to add routing to example.org/hello,
# we would use '/hello'
@app.route('/') 
def hello_world():
	return '<p>Hello, World!</p>'