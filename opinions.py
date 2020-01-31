import os

from flask import Flask, request

from random import choice

app = Flask(__name__)

@app.route('/add-opinion', methods = ['get'])
def add_opinion(opinions):

    new_op = request.args.get('new_op')

    new_op = str(new_op)

    opinions = opinions.append(new_op)

    return opinions
    
@app.route('/opinion')
def opinion_func(opinions):

    opinion = choice(opinions)

    return f"<h1>{opinion}</h1>"
    
if __name__ == '__main__':
    if 'PORT' in os.environ:
        opinions = ["Looks good", "Ummm I'm not really sure", "Ask Tom", "That looks stupid", "I'd do it a different way", "Looks great!"]
        app.run(host='0.0.0.0', port=int(os.environ['PORT']))
    else:
        app.run(debug=True)