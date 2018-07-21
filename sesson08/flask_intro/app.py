# 1 Create a flask app
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello C4T4, this is homepage"

@app.route("/about-me")
def about_me():
    return """
    A bit about me(the developer):
    Hello, my name is Nguyen Mai Phuong or some people call me MP.
    I am 15 years old when i develop this website.
    I am studying at grade 11 at HN-Amsterdam high school for the gifted """
@app.route("/hello/<name>")
def hello(name):
    return "Hello " + name
# 2 Run app
if __name__ == "__main__":
    app.run(debug=True)