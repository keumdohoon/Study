from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello333():
    return "<h1>hello dohoon world</h1>"

@app.route('/bit')
def hello334():
    return "<h1>hello bit computer world</h1>"

@app.route('/gema')
def hello335():
    return "<h1>hello GEMA world</h1>"


@app.route('/bit/bitcamp')
def hello336():
    return "<h1>hello bit computer world</h1>"


if __name__ =='__main__':
    app.run(host = '127.0.0.1', port=8888, debug=True)


##########################################

@app.route('/gema')
def hello335():
    return "<h1>hello GEMA world</h1>"

# @app.route('/bit')
# def hello334():
#     return "<h1>hello bit computer wirld</h1>"

# if __name__ =='__main__':
#     app.run(host = '127.0.0.1', port=8888, debug=True)


