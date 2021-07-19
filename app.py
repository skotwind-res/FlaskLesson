from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)
temp = """
'<a href="/">Main</a>'
'<a href="/xuiart">Start</a>'
"""

@app.route('/main')  # 127.0.0.1:5000
def main():
    return render_template('index.html', page_name='Main')

@app.route('/xuiart')
def xuiart():
    return render_template('index.html', page_name='Start')

@app.route('/hello/<name>')
def hello_name(name):
    names = {
        'user_name': name,
        'page_name': 'Start',
    }
    return render_template('index.html', **names)

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    print(request.args)
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):

            return redirect(url_for('main'))
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

def valid_login(name, pswd):
    if name.lower() == 'tim' and str(pswd) == '1234':
        return True


@app.route('/test')
def test():
    return request.args

if __name__ == '__main__':
    app.run()