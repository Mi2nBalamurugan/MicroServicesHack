from flask import Flask, request, jsonify,  make_response
import random
from flask import jsonify
import os

#app intialization
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hey'



@app.route('/hello', methods=['GET'])
def create_user():
    return jsonify("Hello from the process "+str(os.getpid()));

if __name__ == '__main__':
    app.run(debug=True)