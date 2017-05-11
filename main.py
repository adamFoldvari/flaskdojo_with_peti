from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

count = 0
counts = {'GET': 0,
          'POST': 0,
          'PUT': 0,
          'DELETE': 0}


@app.route('/')
def homepage():
    return render_template('dojo.html')


@app.route('/request-counter', methods=['POST', 'GET'])
def counter():
    global count
    count += 1
    if request.method == 'GET':
        global counts
        counts['GET'] += 1
    else:
        global counts
        counts['POST'] += 1
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
