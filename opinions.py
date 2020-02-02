import os

from flask import Flask, request

from random import choice

app = Flask(__name__)

opinions = ["Looks good", "Ummm I'm not really sure", "Ask Tom", "That looks stupid", "I'd do it a different way", "Looks great!"]
new_opinions = []


@app.route('/add-opinion', methods=['GET', 'POST'])
def add_opinion(opinions = opinions, new_opinions = new_opinions):

    opinion = request.args.get('opinion')

    new_op = str(opinion).replace("_", " ")

    if new_op not in opinions:

        opinions.append(new_op)
        new_opinions.append(new_op)

        return f'<h1 style = "text-align: center">You have added {new_op}</h1>'

    else:
       return f'<h1 style = "text-align: center">{new_op} is already included</h1>' 


@app.route('/opinion')
def opinion_func(opinions = opinions):

    opinion = choice(opinions)

    return f'<h1 style = "text-align: center">{opinion}</h1>'


@app.route('/remove-opinion', methods=['GET', 'POST'])
def remove_opinion(opinions = opinions):

    opinion = request.args.get('opinion')

    rem_op = str(opinion).replace("_", " ")

    if rem_op in opinions:
        opinions.pop(rem_op)
        return f'<h1 style = "text-align: center"> You have removed {rem_op}</h1>'

    else:
        return f'<h1 style = "text-align: center"> {rem_op} not found, please check your spelling</h1>'


@app.route('/reset-opinions')
def reset_opinions(opinions = opinions, new_opinions = new_opinions):

    for i in new_opinions:

        opinions.pop(i)

    return f'<h1 style = "text-align: center"> Reset to original opinions!</h1>'


@app.route('/num-opinions')
def num_opinions(opinions = opinions):

    return(f'<h1 style = "text-align: center">There is a choice of {len(opinions)} opinions</h1>')
    
if __name__ == '__main__':
    if 'PORT' in os.environ:
        app.run(host='0.0.0.0', port=int(os.environ['PORT']))
    else:
        app.run(debug=True)