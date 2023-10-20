from flask import Flask, render_template
app = Flask(__name__)
app.debug = True

posts = [
    {
        'author': 'Ivan Gutierrez',
        'title': 'Flask project 1',
        'content': 'first post content',
        'date_posted': 'october 19 2023'
    },
    {
        'author': 'Manuel Flores',
        'title': 'Flask project 2',
        'content': 'second post content',
        'date_posted': 'october 19 2023'
    }
]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)