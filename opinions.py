import os

from flask import Flask, request

from random import choice

app = Flask(__name__)

opinions = ["Looks good", "Ummm I'm not really sure", "Ask Tom", "That looks stupid", "I'd do it a different way", "Looks great!"]

@app.route('/add-opinion', methods=['GET', 'POST'])
def add_opinion(opinions = opinions):

    opinion = request.args.get('opinion')

    new_op = str(opinion).replace("_", " ")

    opinions = opinions.append(new_op)

    return opinions
    

@app.route('/opinion')
def opinion_func(opinions = opinions):

    opinion = choice(opinions)

    return f"<h1>{opinion}</h1>"


@app.route('/list-opinions')
def list_opinions(opinions = opinions):

    print(f"<h1>There's a choice of {len(opinions)} opinions</h1>")
    
if __name__ == '__main__':
    if 'PORT' in os.environ:
        app.run(host='0.0.0.0', port=int(os.environ['PORT']))
    else:
        app.run(debug=True)