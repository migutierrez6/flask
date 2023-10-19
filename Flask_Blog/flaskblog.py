from flask import Flask
app = Flask(__name__)
app.debug = True
@app.route("/")
def hello():
    return "<h1>Home page</h1>"

@app.route("/about")
def about():
    return "<h1>about page</h1>"

if __name__ == '__main__':
    app.run(debug=True)