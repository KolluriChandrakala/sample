from flask import Flask
app = Flask(__name__)
@app.route('/')
def firstApp():
    return "Hello world to github"
app.run(debug = True)


