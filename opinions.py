import os

from flask import Flask, jsonify

from random import choice

app = Flask(__name__)


@app.route('/opinion', methods = ['get'])
def get_param():
    
    opinions = ["Looks good", "Ummm I'm not really sure", "Ask Tom", "That looks stupid", "I'd do it a different way", "Looks great!"]

    opinion = choice(opinions)

    return jsonify(opinion)
    
if __name__ == '__main__':
    if 'PORT' in os.environ:
        app.run(host='0.0.0.0', port=int(os.environ['PORT']))
    else:
        app.run(debug=True)